import os
import logging
import random
from dotenv import load_dotenv
import tweepy

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(
    filename='tweet_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Fetch Twitter credentials
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# List of tweets to choose from
TWEETS = [
    "🚀 New day, new chance to shine!",
    "💡 Code. Debug. Repeat.",
    "🌱 Growth starts with small steps.",
    "🔥 Python bots make life easier!",
    "📌 Stay focused. Keep learning.",
    "👨‍💻 Just posted this using a Python script!",
]

def post_random_tweet():
    try:
        tweet = random.choice(TWEETS)
        client.create_tweet(text=tweet)
        logging.info(f"Tweet posted: {tweet}")
        print(f"✅ Tweet posted successfully: {tweet}")
    except Exception as e:
        logging.error(f"Error posting tweet: {e}")
        print(f"❌ Error posting tweet: {e}")

def main():
    print("🚀 Twitter Bot Running...")
    post_random_tweet()

if __name__ == "__main__":
    main()

