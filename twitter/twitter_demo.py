import tweepy
from tweepy import *

# Consumer keys and access tokens, used for OAuth 
consumer_key = 'cRz70QuhNCGvFMlFHy3ARekMY'
consumer_secret = 'WBdhkig3nZ5DTFZS0UKN0k2HnmwgbQ39xQRN6kWzeE2DfvYztg'
access_token = '201832916-lLrZ1Qw4D5zQZii0k3RgOxuY0ymnyJfPkQSXu1sc'
access_token_secret = 'YLKNQfqIfgN9PK8IwYBd3TsSI3fkl1pfXgUkM3aP9Xgl8'

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
 
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
if __name__ == '__main__':
    
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
     
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
     
    # Sample method, used to update a status
    #api.update_status('Hello Python Central!')
    
    
    # Creates the user object. The me() method returns the user whose authentication keys were used.
    user = api.me()
     
    print('Name: ' + user.name)
    print('Location: ' + user.location)
    print('Friends: ' + str(user.friends_count))

    listener = StdOutListener()

    stream = Stream(auth, listener)
    stream.filter(track=['#pythoncentral'])