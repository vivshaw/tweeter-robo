# Tweeter Robo

A simple, Heroku-ready tweetbot written with Tweepy &amp; Markovify

## What it does

Tweeter Robo is just a simple Markov chain bot that posts to Twitter. To see it in action, check out my bot, [@MechaBronte](https://twitter.com/MechaBronte).

## Usage

First, you'll need to register an account for your bot, [register an app](https://apps.twitter.com/), and grab your Twitter API keys. Then, things will differ depending on whether you want local or cloud deployment:

#### Local deployment

```
git clone https://github.com/vivshaw/tweeter-robo.git
cd tweeter-robo
pip install -r requirements.txt
vim tweeter_robo/twitter_credentials
#Fill in your Twitter API keys here
python tweeter_robo_go.py corpus.txt
```
#### Heroku deployment

```
git clone https://github.com/vivshaw/tweeter-robo.git
cd tweeter-robo
heroku create
git push heroku master
heroku ps:scale worker=0
```

Or, if you want to use the scheduler, replace that last step with:

```
heroku addons:create scheduler:standard
heroku addons:open scheduler
```

## Todo

* Implement [dotenv](https://github.com/theskumar/python-dotenv) for cleaner load of Twitter creds
* Automate some of the deployment tasks with [fabric](http://www.fabfile.org/), probably
