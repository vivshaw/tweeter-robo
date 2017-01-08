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
        
        #initialize corpus (after processing) and delay
        self.corpus = TweetBot.load_corpus(corpus)
        self.delay = delay
    
    @staticmethod
    def load_corpus(corpus):
        with open(corpus, 'r') as corpus_file:
            corpus_lines = corpus_file.readlines()
        return corpus_lines
        
    def tweet(self, message):
        self.api.update_status(message)

    def automate(self):
        pass
    
def main(args):
    args = args[1:]
    bot = TweetBot(args[0], args[1])
    

if __name__ == "__main__":
    main(sys.argv)