import tweepy 
import pandas as pd
import time

api_key = 'RCHKQdGU4MhlECGYkWIpdoazF'
api_key_secret = 'sIVmd37ElrRx36CWfXCuytQJBq3kzaF0cf6mg9cCyiQ40Fz2rL'

access_token = '1447529937385185289-wg6XgED6AHYLkLyilcjYhvfGUX0IV5'
access_token_secret = 'KWOrbaPkjJ5GgL2GrviUEe9UBFC3Dt8KG5Trcwvhz3M8x'

# consumer_key = "X8IkTIwvxCEWSPpMNSIE53opE"
# consumer_secret = "s4bXVKUBYLVU8bXK6E6FzTArhzLAzjjZP4K2wwBMXb2eMib4SG"
# access_token = "1447529937385185289-Sf4XEFDpuZ1axo4s4V16jTaNpJTk2u"
# access_token_secret = "KUwbbJrKbhg8okx4IsVCQno5bZNP7oMuB9CxsDCFjUw1f"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# t0 = time

for status in api.user_timeline(screen_name = "emmanuelmacron", count = 1 ) :
    print(status.text)
