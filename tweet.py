import tweepy
from mykeys import *

def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))

client = tweepy.Client(consumer_key=APIkey,
                       consumer_secret=APIkeysecret,
                       access_token=accesstoken,
                       access_token_secret=accesstokensecret)

print('\n\t--- Twitter ---')
response = client.create_tweet(text=input("Post: "))

if not response[2]: prCyan("'%s' tweeted.\n" % response[0]['text'])
else: print("Error: ", response[2])

# More functionnalities:
# https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9
## 10 (timeline), 11 (mentions)