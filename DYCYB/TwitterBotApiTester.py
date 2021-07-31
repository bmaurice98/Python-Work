from logging import Handler
import tweepy

# Authenticate to Twitter

auth = tweepy.OAuthHandler(
    "gB1yGFeNqyNrblquB1xeZUp7y", "HofPhxLWrj2kgy3QC3NOuT0Vmu2etAvwXHEeLfXFs9z2Xbq4Ax"
)

auth.set_access_token(
    "1237368414-klVmgs8qq6NdWfsxteWh3qZJRZBJswZ0DyM0nPu",
    "YAcif1krphxVnNbjZXptjvMjsDcUYt3C3TY5ec2pCmNoC",
)

# Access twitter API and verify auth credentials
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK\n")

except:
    print("Authentication Error\n")

# print recent tweeters and their tweet
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
