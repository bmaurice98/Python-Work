import json, tweepy, logging, time
from tweepy.streaming import Stream
from config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}: {tweet.text}\n")
        return False

    def on_error(self, status):
        print("Error detected")
        exit()


def tweetfinder(api):
    logger.info("Retrieving tweets")
    for i in range(3):
        tweets_listener = MyStreamListener(api)
        stream = tweepy.Stream(api.auth, tweets_listener)
        stream.filter(track=["can't find"], languages=["en"])


def main():
    api = create_api()
    while True:
        tweetfinder(api)
        logger.info("waiting...")
        time.sleep(30)


if __name__ == "__main__":
    main()
