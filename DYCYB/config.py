# DYCYB/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv("gB1yGFeNqyNrblquB1xeZUp7y")
    consumer_secret = os.getenv("HofPhxLWrj2kgy3QC3NOuT0Vmu2etAvwXHEeLfXFs9z2Xbq4Ax")
    access_token = os.getenv("1237368414-klVmgs8qq6NdWfsxteWh3qZJRZBJswZ0DyM0nPu")
    access_token_secret = os.getenv("YAcif1krphxVnNbjZXptjvMjsDcUYt3C3TY5ec2pCmNoC")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
