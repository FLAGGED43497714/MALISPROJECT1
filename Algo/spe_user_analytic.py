import tweepy

consumer_key = 'RCHKQdGU4MhlECGYkWIpdoazF'
consumer_key_secret = 'sIVmd37ElrRx36CWfXCuytQJBq3kzaF0cf6mg9cCyiQ40Fz2rL'

access_token = '1447529937385185289-wg6XgED6AHYLkLyilcjYhvfGUX0IV5'
access_token_secret = 'KWOrbaPkjJ5GgL2GrviUEe9UBFC3Dt8KG5Trcwvhz3M8x'


auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_key_secret)

api = tweepy.API(auth)

id_lequipe = 50465434

conc_txt = ""

for Tweet in api.user_timeline(user_id=id_lequipe).items(10):
    text = str(Tweet.full_text.encode("utf-8"))
    if "#PSG" in text:
        conc_txt += Tweet.full_text + "\n\n\n"


print(conc_txt)
    
