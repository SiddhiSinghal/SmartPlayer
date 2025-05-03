import pandas as pd
from textblob import TextBlob

def analyze_sentiment(df):
    def get_sentiment(text):
        return TextBlob(text).sentiment.polarity
    
    df['sentiment'] = df['chat'].apply(get_sentiment)
    return df
