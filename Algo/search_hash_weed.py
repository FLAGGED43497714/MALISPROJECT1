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

tweets = tweepy.Cursor(api.search_tweets,q='FC Barcelona AND -filter:retweets AND -filter:replies' , lang = 'en', tweet_mode = "extended").items(2000) #,result_type='popular'

# result_type='popular'

# for tweet in tweets :
#     # if (not tweet.retweeted) and ('RT @' not in tweet.text):
#     print(tweet.text)

def isGoodTweet(conc_txt, tweet_full_text) :
    good_tweet = True
    ban_word_list = ['weed', 'beuh', 'nba', 'NBA', 'sanitaire', 'telegram', 'snap', 'snapchat', 'live stream']
    if conc_txt.count(tweet_full_text) >=  1 :
        good_tweet = False
    for ban_word in ban_word_list :
        if tweet_full_text.count(ban_word) >=  1 :
            good_tweet = False
    return good_tweet


conc_txt = ""
conc_parallel = ""

# def tweet_to_json(tweet):
#     tweet_dict = {
#         "text": tweet.full_text,
#         "author_name": tweet.user.screen_name
#     }
#     with open('tweet.json', 'w+') as f:
#         json.dump(tweet_dict, f)

for tweet in tweets :
    if isGoodTweet(conc_txt=conc_txt, tweet_full_text=tweet.full_text) == False :
        print("bad tweet")
        conc_parallel += tweet.full_text + "\n\n\n\n"

    else :
        # tweet_to_json(tweet=tweet)
        conc_txt += "created at : "+str(tweet.created_at) + "\n"
        conc_txt += "followers count : "+str(tweet.user.followers_count) + "\n"
        conc_txt += "fav count : "+str(tweet.favorite_count) + "\n"
        conc_txt += tweet.full_text + "\n\n\n\n"
        # print(tweet)

print(conc_txt)

text_file = open("Barca1.txt", "w", encoding="utf-8")
text_file_para = open("output_parallel.txt", "w", encoding="utf-8")


text_file.write(conc_txt)
text_file_para.write(conc_parallel)

text_file.close()
text_file_para.close()