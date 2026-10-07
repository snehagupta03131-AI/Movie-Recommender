from flask import Flask, request, jsonify
from src.recommender import recommend_movies_for_user

app = Flask(__name__)

@app.route('/')
def home():
    return "Movie Recommender API is running!"

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', type=int)
    n = request.args.get('n', default=10, type=int)
    
    if user_id is None:
        return jsonify({"error": "Please provide user_id parameter"}), 400
    
    recommendations = recommend_movies_for_user(user_id, n=n)
    return jsonify({"user_id": user_id, "recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)