import discord
import os
import asyncio
import traceback

from core.configHandler import Config
from core.perms import checkPermissions
from core.language import getLanguages, openLanguageFile
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Bot

global token
global filename

#Defining the bot
intents = discord.Intents.all()
bot = Bot(intents=intents, command_prefix='!')

filename = os.path.basename(__file__)[:-3]

config = Config("configs/main.cfg")

with open('token.txt', 'r') as file:
    token = file.read()

class MainCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="setlanguage", description="Set language for the server")
    async def setLanguage(self, ctx, language: str):
        print(config.returnConfig())
        config.updateConfig('CORE', 'language', language)
        config.writeConfig()
        print(config.returnConfig())
        await ctx.reply(f'Sucessfully changed language to {language}')

#Error handler
@bot.event
async def on_command_error(ctx, error):
    traceback.print_exception(type(error), error, error.__traceback__)
    await ctx.send(f'An error occurred: {error}')

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged on as {bot.user} (ID: {bot.user.id})')

async def main():
    #Load all of the extensions in /modules/
    for file in os.listdir("./modules"):
        if file.endswith(".py"):
            await bot.load_extension(f"modules.{file[:-3]}")
            print(f"Loaded {file}")
    await bot.add_cog(MainCommands(bot))
    await bot.start(token)

#---------------------------------------------------------------------------------
# Don't forget to enter your bot token in token.txt from Discord Developer Portal!
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())
