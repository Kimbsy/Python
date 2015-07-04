import tweepy

class TwitterAPI:
    def __init__(self, ck, cs, at, ats):
      consumer_key = ck
      consumer_secret = cs
      auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
      access_token = at
      access_token_secret = ats
      auth.set_access_token(access_token, access_token_secret)
      self.api = tweepy.API(auth)

    def tweet(self, message):
      self.api.update_status(status=message)

if __name__ == '__main__':

  f = open("/home/kimbsy/Programs/Python/ORTHRUS/access")

  tvitter = TwitterAPI()
  twitter.tweet("Hello World!")
