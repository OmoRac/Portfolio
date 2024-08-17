# Game Reviews API

## Setup

### Install the required packages:

#### pip install: 
#### 	flask
#### 	mysql-connector-python

### Fill in the config.py file with the following content

#### USER = "your_username"

#### PASSWORD = "your_password"

#### HOST = "your_host"

#### These should match with your personal SQL details

### Ensure you MySQL database is set up with the reviews table and the games_reviews database


## Running the API

### Make sure the app.py file is running first otherwise the API will not work

### Then run the Flask application in the main.py file

### Make sure the these files have access to the db_utils.py file and the config.py file.


## API Endpoints

### - GET /reviews: Fetches all reviews
### - POST /reviews: Add a new review. Requires JSON body with "game_id", "game_title", "user_id", "username", "review_text", "rating"
#### 	- when adding a new review please make sure the game_id and the user_id are unique
### - Get /reviews/search: Search for review using the game_idThis is my portfolio

