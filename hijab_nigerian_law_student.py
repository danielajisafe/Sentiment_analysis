# standard packages
import tweepy
import csv
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key ='**************************'
consumer_secret = '******************************'

acess_token='*********************************'
acess_token_secret='*****************************'

auth= OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acess_token,acess_token_secret)

api = tweepy.API(auth)

# Retrieve Tweets
public_tweets = api.search ('JusticeforFirdaus')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob (tweet.text)
	print(analysis.sentiment)

    

# Saving each Tweet to a CSV file
#and label each one as either 'positive', or 'negative' based on the sentiment 

csvfile = open('twitter_sentiment.csv', 'w') #open file for operation
writer = csv.writer(csvfile)   


for tweet in public_tweets:
    foo = tweet.text.encode('utf-8').strip()  #this encoding formatting was required to make file writing of tweets  troublefree, as some   characters in the tweets faced format problems

    analysis = TextBlob(tweet.text).sentiment
    emotion = analysis.polarity
    if emotion > 0:
       writer.writerow([foo,"positive",analysis]) 
  
    else : 
       writer.writerow([foo,"negative",analysis])   
    
csvfile.close()
print("ENtire process completed successfully ! Our new CSV file contains the results.")