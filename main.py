import requests
import json

# def get_reviews():
#     result = requests.get(
#         'http://127.0.0.1:5001/reviews',
#         headers={'content-type': 'application/json'}
#     )
#     return result.json()
def get_reviews():
    response = requests.get(
        'http://127.0.0.1:5001/reviews',
        headers={'content-type': 'application/json'}
    )
    if response.status_code == 200:
        return response.json()
def add_review(game_id, game_title, user_id, username, review_text, rating):
    review = {
        "game_id": game_id,
        "game_title": game_title,
        "user_id": user_id,
        "username": username,
        "review_text": review_text,
        "rating": rating
    }
    response = requests.post(
        'http://127.0.0.1:5001/reviews',
        headers={'content-type': 'application/json'},
        data=json.dumps(review)
    )
    return response.json()

def search_reviews(game_id):
    response = requests.get(
        f'http://127.0.0.1:5001/reviews/search?game_id={game_id}',
        headers={'content-type': 'application/json'}
    )
    return response.json()

# def display_reviews(reviews):
#     print("{:<10} {:<20} {:<10} {:<15} {:<50} {:<5}".format('Game ID', 'Game Title', 'User ID', 'Username', 'Review Text', 'Rating'))
#     print('-' * 110)
#     for review in reviews:
#         print("{:<10} {:<20} {:<10} {:<15} {:<50} {:<5}".format(
#             review['game_id'], review['game_title'], review['user_id'], review['username'], review['review_text'], review['rating']))
def display_reviews(reviews):
    print("{:<10} {:<30} {:<10} {:<15} {:<120} {:<5}".format(
        'Game ID', 'Game Title', 'User ID', 'Username', 'Review Text', 'Rating'))
    print('-' * 300)
    for review in reviews:
        print("{:<10} {:<30} {:<10} {:<15} {:<120} {:<5}".format(
            review[0], review[1], review[2], review[3], review[4], review[5]))




def run ():
    print("#######################################")
    print()
    print("Hello.")
    print()
    print("Welcome to For the Gamers")
    print()
    print("#######################################")
    while True:
        print("Choose an option:")
        print("1. View Reviews")
        print("2. Add Review")
        print("3. Search Reviews by Game ID")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            reviews = get_reviews()
            display_reviews(reviews)
        elif choice == '2':
            game_id = int(input("Enter game ID: "))
            game_title = input("Enter game title: ")
            user_id = int(input("Enter user ID: "))
            username = input("Enter username: ")
            review_text = input("Enter review text: ")
            rating = int(input("Enter rating (0-10): "))
            new_review = add_review(game_id, game_title, user_id, username, review_text, rating)
            print("Response:", new_review)
        elif choice == '3':
            game_id = input("Enter game id to search: ")
            reviews = search_reviews(game_id)
            display_reviews(reviews)
        elif choice == '4':
            print("Goodbye!")
            print()
            print("Hope to see you again soon.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


if __name__ == '__main__':
    run()
