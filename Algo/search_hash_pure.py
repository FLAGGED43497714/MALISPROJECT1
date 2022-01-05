from numpy.core.numeric import full
import tweepy
import json

from difflib import SequenceMatcher



consumer_key = 'cB0v9dTf1igUQHAztCAc2cmiv'
consumer_key_secret = 'jr0HRnBjVDnP9stEB4mCc8VxSaFwadjgRDdDJq7v9J5BtL9rjt'

access_token = '1447529937385185289-Vh6vY1S8tOxU31xEEnc1LJgffY5F3R'
access_token_secret = 'XtR0BOMhbCgn6BUxbWmRQB7lPuymmeQQzvH7XYohfXCnu'


auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_key_secret)

api = tweepy.API(auth)


# choice = input("enter the hashtag : ")

tweets = tweepy.Cursor(api.search_tweets,q='#psg AND -filter:retweets AND -filter:replies' , lang = 'fr', tweet_mode = "extended").items(200) #,result_type='popular'

# result_type='popular'

# for tweet in tweets :
#     # if (not tweet.retweeted) and ('RT @' not in tweet.text):
#     print(tweet.text)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


conc_txt = ""

conc_parallel = ""

tweets_string_list = []


for tweet in tweets :
    # print(tweet.full_text)
    already_in = False
    for other_tweet_text in tweets_string_list :
        if similar(tweet.full_text,other_tweet_text) >=  0.6 :
            print("already in")
            already_in = True
        else :
            continue
    if already_in == False :
        # print(tweet.full_text)
        conc_txt += tweet.full_text + "\n\n\n\n"
        tweets_string_list += [tweet.full_text]

    if already_in == True :
        # print(tweet.full_text)
        conc_parallel += tweet.full_text + "\n\n\n\n"


# print(conc_txt)
# print(conc_txt)

text_file = open("output.txt", "w", encoding="utf-8")
text_file_para = open("output_parallel.txt", "w", encoding="utf-8")


text_file.write(conc_txt)
text_file_para.write(conc_parallel)

text_file.close()
text_file_para.close()