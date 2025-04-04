import discord
import os
import asyncio
import configparser
import json

from discord import app_commands
from discord.ext.commands import Bot

global token
global config

#Defining the bot
intents = discord.Intents.all()
bot = Bot(intents=intents, command_prefix='!')

#Initializing the main config file
config = configparser.ConfigParser()
config.read('./configs/main.cfg')

with open('token.txt', 'r') as file:
    token = file.read()

def checkPermissions(user:discord.Member, permissions:list):
    roles = user.roles
    for role in roles:
        if role.permissions.value & permissions:
            return True
    return False

def getLanguages():
    availableLanguages = []
    for dir in os.listdir('./translations'):
        availableLanguages.append(dir)
    return availableLanguages

def openLanguageFile(language:str):
    filename = os.path.basename(__file__)
    with open(f'./translations/{language}/{filename}.json', 'r') as file:
        return file.read().json()

class MainCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='setlanguage', description='Sets the language of the bot for the server.')
    async def setLanguage(self, interaction:discord.Interaction, language: str):
        prompt = openLanguageFile(language)
        if not checkPermissions(interaction.user, 1024):
            await interaction.response(text=prompt['setlang']['noperms'])
        else:
            config['language'] = language
            with open("./configs/main.cfg", "w") as configfile:
                config.write(configfile)
            await interaction.response(text=prompt['langchanged']['success'])

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user} (ID: {bot.user.id})')

async def main():
    #Load all of the extensions in /modules/
    for file in os.listdir("./modules"):
        if file.endswith(".py"):
            await bot.load_extension(f"modules.{file[:-3]}")
    await bot.start(token)

#---------------------------------------------------------------------------------
# Don't forget to enter your bot token in token.txt from Discord Developer Portal!
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())
