from idlelib.outwin import file_line_pats

import discord
import os
import asyncio
import traceback
import datetime

from core.configHandler import Config
from core.perms import checkPermissions
from core.language import getLanguages, TranslationFile
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot

global token
global filename

#Defining the bot
time = datetime.datetime.now()
intents = discord.Intents.all()
bot = Bot(intents=intents, command_prefix='!')

filename = os.path.basename(__file__)[:-3]

config = Config("configs/main.cfg")

with open('token.txt', 'r') as file:
    token = file.read()

def loadModules():
    modules = []
    with open("enabled_modules.txt", "r") as file:
        for line in file:
            if line.endswith("\n"):
                line = line[:-1]
            modules.append(line)
    print(modules)
    return modules

class MainCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="ping")
    async def ping(self, ctx):
        """Test the bot's latency, usually used for bot tests"""
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

#Error handler
@bot.event
async def on_command_error(ctx, error):
    traceback.print_exception(type(error), error, error.__traceback__)
    await ctx.send(f'An error occurred: {error}')

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'[{time}] Logged on as {bot.user} (ID: {bot.user.id})')

async def main():
    enabled_modules = loadModules()
    #Load all of the extensions in enabled_modules.txt
    for file in enabled_modules:
        try:
            await bot.load_extension(f"modules.{file}")
            print(f"[{time}] Loaded {file}.py")
        except Exception:
            print(f"[{time}] ERROR! Could not load {file}.py")
    await bot.add_cog(MainCommands(bot))
    await bot.start(token)

#---------------------------------------------------------------------------------
# Don't forget to enter your bot token in token.txt from Discord Developer Portal!
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())
