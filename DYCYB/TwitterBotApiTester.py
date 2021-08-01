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
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

# Creating a tweet

# api.update_status("Welp, I guess it starts...")

# Return user details

user = api.get_user("itz_mizu")

# print(user.name)
# print(user.description)
# print(user.location)

# for follower in user.followers():
#     print(follower.name)

# set follow status 'create_friendship' or 'destroy_friendship'
# api.destroy_friendship("realpython")

# return list of accounts account has blocked
# for block in api.blocks():
#     print(block.name)

# returns recent tweets with given keyword
# for tweet in api.search(q="can't find", lang="en", rpp=10):
#     print(f"{tweet.user.name}: {tweet.text}\n")

# return worldwide trends
trends_worldwide = api.trends_place(1)

for trend in trends_worldwide[0]["trends"]:
    print(trend["country", "name"])
