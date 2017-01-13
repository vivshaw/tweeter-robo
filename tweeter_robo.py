# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:27:34 2017

@author: vivshaw
"""

import sys
import os
import tweepy
import markovify
from time import sleep

if os.getenv("HEROKU"):
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_key = os.getenv("ACCESS_TOKEN")
    access_secret = os.getenv("ACCESS_TOKEN_SECRET")
else:
    from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret

class TweetBot:
    def __init__(self, corpus, delay):
        corpus = TweetBot.load_corpus(corpus)
        self.model = markovify.Text(corpus)
        self.delay = delay

        #initialize Twitter authorization with Tweepy
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
    
    @staticmethod
    def load_corpus(corpus):
        with open(corpus) as corpus_file:
            corpus_lines = corpus_file.read()
        return corpus_lines
        
    def tweet(self):
        message = self.model.make_short_sentence(140)
        try:
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)
        
    def automate(self):
        while True:
            self.tweet()
            sleep(self.delay)
            
    def automate_with_limit(self, limit):
        for i in range (limit):
            self.tweet()
            sleep(self.delay)
    
    def reply(self, reply_within):
        pass
            
def main(args):
    args = args[1:]
    bot = TweetBot(args[0], int(args[1]))
    bot.automate();

if __name__ == "__main__":
    main(sys.argv)
