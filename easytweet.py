# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:27:34 2017

@author: vivshaw
"""

import sys
import io
import tweepy
from time import sleep
from random import randint
from secrets import *

class TweetBot:
    def __init__(self, corpus, delay):
        self.corpus = TweetBot.load_corpus(corpus)
        self.delay = delay

        #initialize Twitter authorization with Tweepy
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(self.auth)
    
    @staticmethod
    def load_corpus(corpus):
        with io.open(corpus, encoding='utf8') as corpus_file:
            corpus_lines = corpus_file.readlines()
        stripped_corpus = [line.strip() for line in corpus_lines if line.strip()]
        return stripped_corpus
        
    def tweet(self):
        line = self.corpus[randint(0, len(self.corpus) - 1)]
        try:
            self.api.update_status(line)
        except tweepy.TweepError as error:
            print(error.reason)
        
    def automate(self):
        while True:
            self.tweet()
            sleep(self.delay)
            
def main(args):
    args = args[1:]
    bot = TweetBot(args[0], int(args[1]))
    bot.automate();

if __name__ == "__main__":
    main(sys.argv)