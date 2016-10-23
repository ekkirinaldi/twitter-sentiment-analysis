# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 23:36:11 2016

@author: Einherjar
"""

import tweepy
from textblob import TextBlob

consumer_key ='1tpCNxzMtA43I06VdmSuZDikv'
consumer_secret ='4j4GeunLOE9zNTTSMsesdO42al2DhegAr2ZJSrOBxQstEpuLbl'

access_token = '222002940-BO8XVPtATVECyujqeOrkCHTbzIYlYN78wFMjd54b'
access_secret ='MZf8V4O9tThtFoJY8MxQTXow0F6OCCpWTizjm1fUzynyz'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Hilary')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)