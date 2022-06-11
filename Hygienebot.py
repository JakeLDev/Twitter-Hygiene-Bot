import tweepy
import os

def parse_APIs(filename):
    # if os.path.isfile(filename): # If rakefileName exists
    with open(filename, "r") as file:
        lines = file.readlines() # Read the file into an array
        ConsumerKey = lines[0].split()[-1]
        ConsumerSecret = lines[1].split()[-1]
        AccessToken = lines[2].split()[-1]
        AccessTokenSecret = lines[3].split()[-1]
    # print(ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret)
    return ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret


def main():
    ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret = parse_APIs("API_Keys.txt")

    client = tweepy.Client(consumer_key = ConsumerKey,
                        consumer_secret = ConsumerSecret,
                        access_token = AccessToken,
                        access_token_secret = AccessTokenSecret)

    # Replace the text with whatever you want to Tweet about
    response = client.create_tweet(text='hello world')

    print(response)

main()