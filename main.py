import discord
import os
import asyncio
import configparser
import json
from core.perms import checkPermissions
from core.language import getLanguages, openLanguageFile
from discord import app_commands
from discord.ext import commands
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

class MainCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setLanguage(self, interaction:discord.Interaction, language: str):
        prompt = openLanguageFile(language)
        if not checkPermissions(interaction.user, 1024):
            await interaction.response(text=prompt['setlang']['noperms'])
        else:
            config['CORE']['language'] = language
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
