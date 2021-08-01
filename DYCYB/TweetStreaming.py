import json, tweepy, logging, time
from tweepy.streaming import Stream
from config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def tweetfinder(api):
    logger.info("Retrieving tweets")
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=["can't find"], languages=["en"])


def main():
    api = create_api()
    while True:
        tweetfinder(api)
        logger.info("waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
