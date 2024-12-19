from wakepy import keep
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from langdetect import DetectorFactory
import time

#sentiment analysis using vader library
def vader_sentiment(text):
        #starting vader module for text analysis
        analyzer = SentimentIntensityAnalyzer()
        #geting sentiment scores on a scale from -1 to 1 as a dictionary (compound)
        scores = analyzer.polarity_scores(text)
        # calcualting the sentiment of each text based on the compund score
        #positive
        if scores['compound'] >= 0.05:
            sentiment = 1
        #negative
        elif scores['compound'] <= -0.05:
            sentiment = -1
        #neutral
        else:
            sentiment = 0

        return sentiment

def is_english(text):
    try:
        if pd.isna(text) or text.strip() == '':
            return False

        return detect(text) == 'en'
    except:
         return False

with keep.running():
    start_day = "2012-01-01"
    end_day = "2019-11-23"

    tweet = pd.read_csv('data/tweets.csv', delimiter=';', lineterminator='\n')
    tweet.rename(columns={'timestamp': 'date', 'text\r': 'text'}, inplace=True)
    tweet['date'] = pd.to_datetime(tweet['date']).dt.tz_localize(None)
    tweet = tweet[(tweet['date'] >= start_day) & (tweet['date'] <= end_day)]
    tweet['date'] = tweet['date'].dt.date
    tweet = tweet.drop(columns=['id', 'user', 'fullname', 'url'])

    start_time = time.time() 
    tweet['is_english'] = tweet['text'].apply(is_english)
    tweet = tweet[tweet['is_english'] == True]

    tweet = tweet.drop(columns=['is_english'])

    tweet = tweet.dropna(subset=['text'])
    tweet = tweet[tweet['text'].apply(type) == str]
    tweet['sentiment'] = tweet['text'].apply(vader_sentiment)
    tweet.to_csv('data/tweets_sentiment.csv', index=False)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")