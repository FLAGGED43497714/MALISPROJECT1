from numpy.core.numeric import full
import tweepy
import json


consumer_key = 'cB0v9dTf1igUQHAztCAc2cmiv'
consumer_key_secret = 'jr0HRnBjVDnP9stEB4mCc8VxSaFwadjgRDdDJq7v9J5BtL9rjt'

access_token = '1447529937385185289-Vh6vY1S8tOxU31xEEnc1LJgffY5F3R'
access_token_secret = 'XtR0BOMhbCgn6BUxbWmRQB7lPuymmeQQzvH7XYohfXCnu'


auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_key_secret)

api = tweepy.API(auth)


# choice = input("enter the hashtag : ")

# tweets = tweepy.Cursor(api.search_full_archive,label='matchTweetArchive',query='#psg OR paris saint germain' ,maxResults = 10, fromDate = 202110261200, toDate = 202110271200, lang = 'fr').items(10) #,result_type='popular'  ///, tweet_mode = "extended"
tweets = tweepy.Cursor(api.search_tweets,q='#psg  AND -filter:retweets AND -filter:replies' , lang = 'fr', tweet_mode = "extended").items(10) #,result_type='popular'


# result_type='popular'

# for tweet in tweets :
#     # if (not tweet.retweeted) and ('RT @' not in tweet.text):
#     print(tweet.text)

# print("tweets")
# print(tweets)
# print("\n\n")

conc_txt = ""
for tweet in tweets :

    if conc_txt.count(tweet.full_text) >=  1 :
        print("already in")

    if tweet.full_text.count("RT @") == 1 :
        conc_txt += tweet.full_text
    else :
        conc_txt += tweet.full_text + "\n\n\n\n"

# print(conc_txt)
# print(conc_txt)

text_file = open("output.txt", "w", encoding="utf-8")


text_file.write(conc_txt)

text_file.close()