# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:27:34 2017

@author: vivshaw
"""

import tweepy
from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret);
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#tweet = 'Hello, world! Just testing Python twitter automation with tweepy'
#api.update_status(status=tweet)