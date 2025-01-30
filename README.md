# Spotipy

A Telegram bot that notifies daily the new releases of your favorite artists!

## Motivation

I am usually the damn fucking person in social events that doesn't know what's going on when a new released song is being played. Also, my phone is a shit and for whatever reason spotify notifications never get through. The reasons mentioned above jointly with my interest (though amateur skills yet) in programming probably useless stuff for other human beings made me realize this is the project I wanted to waste (some business would say invest, idfc, I'm a mathematician) two (very cold, all need to be said) evenings. Enjoy!

## Working principle

This app uses the spotify API and the python library spotipy to make requests to the spotify database. It does the following:
1) Identifies and lists your followed artists.
2) Get the lasts albums
3) Compare those albums with the albums of the day before (stored on a json database) and updates the database.
4) Sends a telegram message with the new releases

This process is repeated daily

## Installation

Clone the repository

    $ git clone https://github.com/abeldonate/spotibot.git

Setup the environment

    $ make setup

Make a Telegram bot via @BotFather (just type /newbot and follow the instructions) and get your chat id via @userinfobot typing /start. From now on the bot token provided by @BotFather will be `BOT_TOKEN` and the ID will be `ME_ID`.

Go to the spotify API webpage (https://developer.spotify.com/dashboard) and sing in. Create a new app and follow the instructions. You will get here the tokens `CLIENT_ID` and `CLIENT_SECRET`

Create the file `src/.env` and fill it with your data

    CLIENT_ID=""
    CLIENT_SECRET=""
    BOT_TOKEN=""
    ME_ID=""

Run the program with

    $ make

## Requirements

Must have installed python, pip, virtualenv and make