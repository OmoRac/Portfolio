CREATE DATABASE games_reviews;
USE games_reviews;

CREATE TABLE reviews(
game_id INT ,
game_title VARCHAR (100),
user_id INT ,
username VARCHAR (100) ,
review_text TEXT,
rating INT,
created_at TIMESTAMP,
CONSTRAINT rating_check CHECK (rating >= 0 AND rating <= 10) 
);

INSERT INTO reviews 
(game_id, game_title, user_id, username, review_text, rating, created_at)
VALUES
(1, "Baldur's Gate 3", 1, "ForTheEmperor", "Very good. I could do anything I wanted and it was very expansive.", 10, CURRENT_TIMESTAMP),
(2, "Hogwarts Legacy", 2, "Aylin_Lover", "Such a good story and expansive plot. I loved the scenery and colours used.", 8, CURRENT_TIMESTAMP),
(3, "Blade and Soul", 3, "turnip_head", "It was pretty good but I don't know if I would regurlary play this", 6, CURRENT_TIMESTAMP),
(4, "Arknights", 4, "d0main-Xpansion", "The characters are cool.", 9, CURRENT_TIMESTAMP),
(5, "Darkest Dungeon", 5, "Shalem_Logos", "It was pretty fun but I don't think roguelikes are for me.", 7, CURRENT_TIMESTAMP),
(6, "Elden Ring", 1, "ForTheEmperor", "Amazing story and action.", 10, CURRENT_TIMESTAMP),
(7, "Minecraft", 2, "Aylin_Lover", "It was cute and fun. I loved the different blocks that allowed for unique builds and really stretched my creative side.", 7, CURRENT_TIMESTAMP),
(8, "Total War: Warhammer III", 3, "turnip_head", "Pretty nice story.", 8, CURRENT_TIMESTAMP),
(9, "Final Fantasy XVI", 4, "d0main-Xpansion", "It was fine.", 5, CURRENT_TIMESTAMP),
(10, "Reverse 1999", 5, "Shalem_Logos", "I really like it right now but something about turn based games does make mark it down for me.", 7, CURRENT_TIMESTAMP),
(11, "Punishing Gray Raven", 1, "ForTheEmperor", "Great action and the philosopy behind the story is really gripping.", 8, CURRENT_TIMESTAMP),
(12, "Fall Guys", 2, "Aylin_Lover", "Full of cheaters but otherwise pretty ok.", 4, CURRENT_TIMESTAMP);
