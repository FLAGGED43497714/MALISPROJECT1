from numpy.core.numeric import full
import tweepy
import json

#teams = [homeTeam, awaTeam]
#language = 'it' / 'en' / 'fr' etc

def requestTweets(team1, team2, language, daymonth, nb_tweets) : 

    teams = [team1, team2]

    consumer_key = 'cB0v9dTf1igUQHAztCAc2cmiv'
    consumer_key_secret = 'jr0HRnBjVDnP9stEB4mCc8VxSaFwadjgRDdDJq7v9J5BtL9rjt'

    access_token = '1447529937385185289-Vh6vY1S8tOxU31xEEnc1LJgffY5F3R'
    access_token_secret = 'XtR0BOMhbCgn6BUxbWmRQB7lPuymmeQQzvH7XYohfXCnu'


    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_key_secret)

    api = tweepy.API(auth)


    # choice = input("enter the hashtag : ")
    for team_index in range(2) :

        tweets = tweepy.Cursor(api.search_tweets,q= teams[team_index] + ' AND -filter:retweets AND -filter:replies' , lang = language, tweet_mode = "extended").items(nb_tweets) #,result_type='popular'

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

        for tweet in tweets :
            if isGoodTweet(conc_txt=conc_txt, tweet_full_text=tweet.full_text) == False :
                print("bad tweet")
                conc_parallel += tweet.full_text + "\n\n\n\n"

            else :
                conc_txt += "created at : "+str(tweet.created_at) + "\n"
                conc_txt += "followers count : "+str(tweet.user.followers_count) + "\n"
                conc_txt += "fav count : "+str(tweet.favorite_count) + "\n"
                conc_txt += tweet.full_text + "\n\n\n\n"

        print(conc_txt)

        path_write = str(teams[0])+"_"+str(teams[1])+"_"+str(teams[team_index])+str(daymonth)+".txt"

        text_file = open(path_write, "w", encoding="utf-8")
        # text_file_para = open("output_parallel.txt", "w", encoding="utf-8")


        text_file.write(conc_txt)
        # text_file_para.write(conc_parallel)

        text_file.close()
        # text_file_para.close()