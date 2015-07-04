import tweepy

# define class for using tweepy Twitter api
class TwitterAPI:
    # constructor
    def __init__(self, ck, cs, at, ats):
        consumer_key = ck
        consumer_secret = cs
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = at
        access_token_secret = ats
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    # send tweet
    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == '__main__':

    # open file with access keys and tokens
    f = open("/home/kimbsy/Documents/ORTHRUS.access")

    # assign keys and tokens
    ck = f.readline()
    cs = f.readline()
    at = f.readline()
    ats = f.readline()

    # instantiate twitter class
    twitter = TwitterAPI(ck, cs, at, ats)

    # send tweet
    # twitter.tweet("Hello World!")