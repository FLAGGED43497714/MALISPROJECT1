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

tweets = tweepy.Cursor(api.search_tweets,q='#psg  AND -filter:retweets AND -filter:replies' , lang = 'fr', tweet_mode = "extended").items(200) #,result_type='popular'

# result_type='popular'

# for tweet in tweets :
#     # if (not tweet.retweeted) and ('RT @' not in tweet.text):
#     print(tweet.text)

def isGoodTweet(conc_txt, tweet_full_text) :
    good_tweet = True
    ban_word_list = ['weed', 'beuh', 'nba', 'NBA', ' pass ', 'sanitaire', 'telegram', 'snap', 'snapchat']
    if conc_txt.count(tweet_full_text) >=  1 :
        good_tweet = False
    for ban_word in ban_word_list :
        if tweet_full_text.count(ban_word) >=  1 :
            good_tweet = False
    return good_tweet


conc_txt = ""
conc_parallel = ""

for tweet in tweets :
    if isGoodTweet(conc_txt=conc_txt, tweet_full_text=tweet.full_text) == False :
        print("bad tweet")
        conc_parallel += tweet.full_text + "\n\n\n\n"

    else :
        conc_txt += tweet.full_text + "\n\n\n\n"

print(conc_txt)
print(conc_txt)

text_file = open("output.txt", "w", encoding="utf-8")
text_file_para = open("output_parallel.txt", "w", encoding="utf-8")


text_file.write(conc_txt)
text_file_para.write(conc_parallel)

text_file.close()
text_file_para.close()