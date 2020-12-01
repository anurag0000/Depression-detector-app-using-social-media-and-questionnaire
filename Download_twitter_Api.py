from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'kA64n1G9ZazthjEPLsbJWFglO'
consumer_secret = 'cYy3ton9Wegx8DjBCBXFYyhYopEaynKlGPwL0R2HDiPKCYMw93'
access_token = '1332615497716678658-HD6B4LVgpUzwgr4OdtkCBcgyOpVm1V'
access_secret = '39DX9uhnJ8Y6zK20676ppsIiOyFlphCaqGQ6h4McKas7F'



class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('data/tweetdata.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad'])