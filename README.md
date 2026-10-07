# 🎬 CineMatch — Hybrid Movie Recommendation System

A hybrid movie recommendation engine combining **Collaborative Filtering** (SVD) and **Content-Based Filtering** (genre similarity) to generate personalized movie recommendations, deployed as an interactive Streamlit web app.

**🔗 Live Demo:** [movie-recommender-alzvtonln6uq4lsqbt4nij.streamlit.app](https://movie-recommender-alzvtonln6uq4lsqbt4nij.streamlit.app)

---

## 📌 Overview

This project builds a movie recommender system using the **MovieLens 100K dataset**, combining two classic recommendation approaches into a hybrid model:

- **Collaborative Filtering (SVD):** Learns patterns from user rating history to predict how a user would rate unseen movies.
- **Content-Based Filtering:** Uses movie genres to find similar movies via cosine similarity.
- **Hybrid Scoring:** Combines both signals (70% collaborative, 30% content-based) for more robust recommendations.

## ✨ Features

- Personalized recommendations for any of the 610 users in the dataset
- Adjustable number of recommendations (5–20)
- Clean, interactive UI built with Streamlit
- Searchable user selection
- Proper train/test evaluation using Precision@K

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| ML — Collaborative Filtering | Surprise (SVD) |
| ML — Content-Based | scikit-learn (Cosine Similarity) |
| Web App | Streamlit |
| Deployment | Streamlit Community Cloud |

## 📊 Model Performance

- **Collaborative Filtering RMSE:** 0.88
- **Average Precision@10** (across sampled users, proper train/test split): ~0.08

## 📁 Project Structure

movie-recommender/
├── data/ # MovieLens dataset (CSV files)
├── models/ # Saved SVD model & processed data (pickle files)
├── notebook/ # Jupyter notebook with full EDA & model development
├── src/
│ └── recommender.py # Core recommendation logic
├── streamlit_app.py # Streamlit web app
├── app.py # Flask API (alternative interface)
└── requirements.txt # Python dependencies


## 🚀 Running Locally

```bash
# Clone the repository
git clone https://github.com/shriya240505/movie-recommender.git
cd movie-recommender

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
```

## 📈 Future Improvements

- Add TMDB API integration for real movie posters
- Experiment with deep learning-based recommendation approaches
- Add more evaluation metrics (Recall@K, NDCG)

---

Built as a learning project to explore end-to-end ML system design — from data exploration to a deployed, production-style application.