# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:27:34 2017

@author: vivshaw
"""

import os
import argparse
import tweepy
import markovify
from time import sleep

if os.getenv("HEROKU"):
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
else:
    from tweeter_robo.twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret


class TweetBot:
    def __init__(self, corpus):
        self.load_corpus(corpus)

        # initialize Twitter authorization with Tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def load_corpus(self, corpus):
        with open(corpus) as corpus_file:
            corpus_lines = corpus_file.read()
        self.model = markovify.Text(corpus_lines)

    def tweet(self):
        message = self.model.make_short_sentence(140)
        try:
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)
        
    def automate(self, delay):
        while True:
            self.tweet()
            sleep(delay)
            
    def automate_with_limit(self, delay, limit):
        for i in range (limit):
            self.tweet()
            sleep(delay)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("corpus", help="filename of the text corpus used as input for the Markov chain")
    parser.add_argument("-d", "--delay", type=int, default=7200, help="delay in seconds between tweets (default: 7200)")
    parser.add_argument("-l", "--limit", type=int, default=0, help="number of tweets to send before exit (default: no limit)")
    args = parser.parse_args()
    
    bot = TweetBot(args.corpus)
    if args.limit:
        bot.automate_with_limit(args.delay, args.limit)
    else:
        bot.automate(args.delay)