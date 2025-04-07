# Modular Discord Bot

## PLEASE NOTICE!

This project is far from being even runnable, so if you want to accelerate the development process, you can make a pull request <3

## Why
* This repository is made for people that want to make a custom Discord bot, with proper functional, that is easy to setup and does not require (almost) any coding experience
* Or if you're lazy and just want an already made bot
* Or if you want to expend the functionality of this bot much further

## Installing
1. Make sure you have Python 3.11 or later installed.
2. Clone this repo to any folder you like
   ```
   git clone https://github.com/EmojiPlay88/modular-discord-bot.git
   ```
3. Install all dependencies:
   ```
   pip instal -r ./requirements.txt
   ```
   
## Main configuration
1. Make an application in [Discord Developer Portal](https://discord.com/developers/applications) (if you want to make ONLY a bot then preferably name your application as your future bot's name, and set the application icon as a profile picture you want to use for your bot)
     * In **"Bot"** tab customize your bot how you want it to be
     * Preferably enable all intents and set permissions for your bot
2. Click **"Reset Token"** button and copy the new token that was displayed for you (Reminder: Don't tell it to anyone!)
3. Paste the token you copied to ```token.txt``` file in the directory where you cloned the repository
4. Under **"OAuth2"** tab on **Discord Developer Portal** in **"Generate URL"** section click **"bot"** and then copy the generated URL
5. Open the URL you just copied and add your bot to the server you want it to be
6. Run ```main.py``` as Python code and you're pretty much ready to go

## Module configuration
* Main module files are found in ```/modules``` folder (that can be found in root folder)
* To enable/disable any modules just insert/delete their name in ```enabled_modules.txt``` file found in root folder

## Module development
* This bot uses ```discord.py``` library
* To make your own module just make a ```.py``` file in ```/modules``` folder
* You can use already written modules as a reference
