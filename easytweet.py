# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:27:34 2017

@author: vivshaw
"""

import sys
import tweepy
from time import sleep
from secrets import *

class TweetBot:
    def __init__(self, corpus, delay):
        #initialize Twitter authorization with Tweepy
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(self.auth)
        
        #initialize other fields
        self.corpus = TweetBot.loadCorpus(corpus)
        self.delay = delay
    
    @staticmethod
    def loadCorpus(corpus):
        return corpus
        
    def tweet(self, message):
        self.api.update_status(message)

    def automate(self):
        pass
    
def main(args):
    args = args[1:]
    bot = TweetBot(args[0], args[1])
    print(bot.corpus, bot.delay)
    bot.tweet("Hello World!")

if __name__ == "__main__":
    main(sys.argv)