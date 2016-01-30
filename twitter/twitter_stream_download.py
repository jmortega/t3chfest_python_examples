# python twitter_stream_download.py -q python -d data
# 
# It will produce the list of tweets for the query "python" 
# in the file data/stream_python.json

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json

consumer_key = 'cRz70QuhNCGvFMlFHy3ARekMY'
consumer_secret = 'WBdhkig3nZ5DTFZS0UKN0k2HnmwgbQ39xQRN6kWzeE2DfvYztg'
access_token = '201832916-lLrZ1Qw4D5zQZii0k3RgOxuY0ymnyJfPkQSXu1sc'
access_secret = 'YLKNQfqIfgN9PK8IwYBd3TsSI3fkl1pfXgUkM3aP9Xgl8'

outfile = open('timeline.json','wb')

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    return parser


def process_or_store(tweet):
    print(json.dumps(tweet))
    line = json.dumps(tweet) + "\n"
    outfile.write(line)


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, query):
        query_fname = format_filename(query)
        self.outfile = "stream_%s.json" % (query_fname)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    
    for tweet in tweepy.Cursor(api.user_timeline).items():
        process_or_store(tweet._json)
    
    #twitter_stream = Stream(auth, MyListener(args.query))
    #twitter_stream.filter(track=[args.query])
