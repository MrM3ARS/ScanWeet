import tweepy
import csv
import sqlite3
import pyautogui
from termcolor import colored 
from art import * 

# Brand and Info

tprint("Mr. M3ARS", font="big") 
tprint("ScanWeet v1", font="doom") 

# Twitter API
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Keywords
search_words = "keyword1 keyword2 keyword3"

conn = sqlite3.connect("tweets.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS tweets (
                    id INT PRIMARY KEY,
                    created_at TEXT,
                    full_text TEXT,
                    screenshot BLOB
                )""")


tweets = tweepy.Cursor(api.search_tweets,
              q=search_words,
              lang="en",
              tweet_mode='extended').items(100)



for tweet in tweets:
    screenshot = pyautogui.screenshot("tweet_" + str(tweet.id) + ".png")
    screenshot_data = screenshot.tobytes()
    cursor.execute("""INSERT INTO tweets (id, created_at, full_text, screenshot)
                      VALUES (?, ?, ?, ?)""",
                   (tweet.id, tweet.created_at, tweet.full_text, screenshot_data))


conn.commit()
conn.close()
