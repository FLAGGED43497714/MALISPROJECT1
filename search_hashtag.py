from numpy.core.numeric import full
import tweepy
import json


consumer_key = 'RCHKQdGU4MhlECGYkWIpdoazF'
consumer_key_secret = 'sIVmd37ElrRx36CWfXCuytQJBq3kzaF0cf6mg9cCyiQ40Fz2rL'

access_token = '1447529937385185289-wg6XgED6AHYLkLyilcjYhvfGUX0IV5'
access_token_secret = 'KWOrbaPkjJ5GgL2GrviUEe9UBFC3Dt8KG5Trcwvhz3M8x'


auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_key_secret)

api = tweepy.API(auth)


# choice = input("enter the hashtag : ")

tweets = tweepy.Cursor(api.search_tweets,q='#PSG AND -filter:retweets AND -filter:replies' , lang = 'fr', tweet_mode = "extended").items(1000) #,result_type='recent'

# result_type='popular'

# for tweet in tweets :
#     # if (not tweet.retweeted) and ('RT @' not in tweet.text):
#     print(tweet.text)


conc_txt = ""
for tweet in tweets :
    if conc_txt.count(tweet.full_text) >=  1 :
        print("already in")
    else :
        conc_txt += tweet.full_text + "\n\n\n\n"

print(conc_txt)
print(conc_txt)

text_file = open("output.txt", "w", encoding="utf-8")


text_file.write(conc_txt)

text_file.close()