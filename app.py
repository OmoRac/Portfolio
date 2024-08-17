from flask import Flask, jsonify, request
from db_utils import add_review, search_reviews_by_id, view_reviews


app = Flask(__name__)


# VIEWING THE REVIEWS
@app.route("/reviews", methods=["GET"])
def get_reviews():
    result = view_reviews()
    return jsonify(result)


# ADDING A NEW REVIEW
@app.route("/reviews", methods=["POST"])
def post_review():
    review_data = request.get_json()
    add_review(
        game_id=review_data["game_id"],
        game_title=review_data["game_title"],
        user_id=review_data["user_id"],
        username=review_data["username"],
        review_text=review_data["review_text"],
        rating=review_data["rating"],
        )
    return jsonify(review_data)


@app.route("/reviews/search", methods=["GET"])
def search_reviews():
    game_id = request.args.get("game_id", "")
    reviews = search_reviews_by_id(game_id)
    return jsonify(reviews)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
