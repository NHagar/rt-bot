import os
import tweepy

auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_TOKEN'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_SECRET'))

api = tweepy.API(auth)

tl = api.list_timeline('dmninterns', 'dmnterns-2k17', include_entities=True)

for i in tl:
    try:
        if 'RT' not in i.text and 'dallasnews.com' in i.entities['urls'][0]['expanded_url']:
            api.retweet(i.id)
    except:
        pass
