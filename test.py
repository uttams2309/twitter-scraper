import tweepy
import csv

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '1096367845359927296-dmyZTKw4vQrTA378JRyVLJzhx9ckUN'
ACCESS_SECRET = 'Utgs76d9CFhAK5KpQZFUdjO5hYnElpsiByi6YCHLeSk8g'
CONSUMER_KEY = 'IyVHhVzR5FrxjARpUZq6UOaAM'
CONSUMER_SECRET = 'f7csUfZ7aSNYvK11jyD224jzlICxiJVXSXG64CSJ3XaFYSc1rr'


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api


# Create API object
api = connect_to_twitter_OAuth()

f = open("t5.csv","w",encoding="utf_8_sig")
writer = csv.writer(f,lineterminator='\n')
writer.writerow(["username","followers","created_at","tweet_text"])
flag = True
last_id = None
count = 0
while(flag):
    for tweet in tweepy.Cursor(api.search,q='#coronavirus'+' -filter:retweets',lang="en").items():
        username = tweet.user.screen_name
        followers = tweet.user.followers_count
        text = tweet.text
        ca = tweet.created_at
        count = count + 1
        writer.writerow([username,followers,ca,text])
        flag = True
        last_id = tweet.id
        if count%100==0:
            print(str(count)+'tweets extracted \n')
f.close()
print('extracted'+str(count)+'tweets')

