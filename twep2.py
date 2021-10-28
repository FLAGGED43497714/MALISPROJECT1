
from tweepy import OAuthHandler
from tweepy import Stream
 
 
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler("a8allB4YpiQC7bxZXbqahbI2E", "DqguAhTm6gwvQlxcapPqfHn0F9jl6ztzXmOjoaTXFscnZwJZ29")
        auth.set_access_token("1447529937385185289-IGPtUvWquPZyBvT0wOlG5A7C7Dy4C4", "oLiWjVDYVy8GLXHoa4J1LWlwb0N7XQaXN53UvduuYSdLG")
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(Stream):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["donal trump", "hillary clinton", "barack obama", "bernie sanders"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)