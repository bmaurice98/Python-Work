import json, tweepy, logging, time
from tweepy.streaming import Stream
from src.config import create_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.id}: {tweet.user.name}: {tweet.text}\n")
        reply(self.api, tweet.id)
        return False

    def on_error(self, status):
        print("Error detected")
        exit()


def tweetfinder(api):
    logger.info("Retrieving tweets")
    for i in range(1):
        tweets_listener = MyStreamListener(api)
        stream = tweepy.Stream(api.auth, tweets_listener)
        stream.filter(
            track=["I can't find", "I lost my", "I don't know where"], languages=["en"]
        )


def reply(api, tweetid):
    Twt = tweetid
    print(Twt)
    api.update_status(
        "Have you checked your butthole? https://youtu.be/--9kqhzQ-8Q",
        in_reply_to_status_id=Twt,
        auto_populate_reply_metadata=True,
    )


def main():
    api = create_api()
    while True:
        tweetfinder(api)
        logger.info("waiting...")
        time.sleep(600)


if __name__ == "__main__":
    main()
