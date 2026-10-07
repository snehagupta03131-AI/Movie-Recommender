import pickle
import numpy as np
import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Current file ke relative path se models load karo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, '..', 'models')

with open(os.path.join(MODELS_DIR, 'svd_model.pkl'), 'rb') as f:
    svd_model = pickle.load(f)

movies = pd.read_pickle(os.path.join(MODELS_DIR, 'movies.pkl'))
ratings = pd.read_pickle(os.path.join(MODELS_DIR, 'ratings.pkl'))

# movies load hone ke BAAD hi similarity matrix calculate hoga
genres_split = movies['genres'].str.get_dummies(sep='|')
similarity_matrix = cosine_similarity(genres_split)


def recommend_movies_for_user(user_id, n=10, cf_weight=0.7, content_weight=0.3):
    all_movie_ids = movies['movieId'].values
    already_rated = set(ratings[ratings['userId'] == user_id]['movieId'].tolist())

    user_liked_movies = ratings[(ratings['userId'] == user_id) & (ratings['rating'] >= 4)]['movieId'].tolist()
    liked_indices = [movies[movies['movieId'] == m].index[0] for m in user_liked_movies if m in movies['movieId'].values]

    if len(liked_indices) > 0:
        content_scores_all = similarity_matrix[:, liked_indices].mean(axis=1)
    else:
        content_scores_all = np.zeros(len(movies))

    results = []
    for i, movie_id in enumerate(all_movie_ids):
        if movie_id in already_rated:
            continue
        cf_score = svd_model.predict(user_id, movie_id).est
        final_score = (cf_weight * cf_score) + (content_weight * content_scores_all[i] * 5)
        results.append((movie_id, final_score))

    results.sort(key=lambda x: x[1], reverse=True)
    top_movie_ids = [m[0] for m in results[:n]]

    result_df = movies[movies['movieId'].isin(top_movie_ids)][['movieId', 'title', 'genres']]
    return result_df.to_dict(orient='records')