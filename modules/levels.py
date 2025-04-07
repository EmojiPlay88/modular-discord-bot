import discord
import json
import os
from discord.ext import commands

#Create the data file if doesn't exist
def fileCheck():
    if not os.path.exists("data/levels.json"):
        with open("data/levels.json", 'w',encoding='utf=8') as file:
            json.dump({}, file)

#"Simpler" way to load the data file
def loadJson():
    try:
        with open("data/levels.json", 'r',encoding='utf=8') as file:
            levels = json.load(file)
            return levels
    except FileNotFoundError:
        fileCheck()
        return loadJson()

#Check if guild id is in the data file
def guildcheck(guildid):
    levels = loadJson()
    if guildid not in levels:
        levels[guildid]= {}
        with open("data/levels.json", 'w',encoding='utf=8') as file:
            json.dump(levels, file)

#Check if user id is in the data file
def usercheck(guildid, userid):
    levels = loadJson()
    if userid not in levels[guildid]:
        levels[guildid][userid] = [0,0]
        with open("data/levels.json", 'w',encoding='utf=8') as file:
            json.dump(levels, file)

class LevelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        fileCheck() #On initialization check if data file exists or not

    #/level
    #TODO: Translation file implementation
    @commands.hybrid_command(name="level")
    async def level(self,ctx):
        userid = str(ctx.author.id)
        guildid = str(ctx.guild.id)
        guildcheck(guildid)
        usercheck(guildid,userid)
        with open("data/levels.json", 'r', encoding='utf-8') as file:
            levels = json.load(file)
        await ctx.send(f'Your xp and level is{levels[guildid][userid][0], levels[guildid][userid][1]}')

    #changed ur @bot.event to @commands.Cog.listener() bc you dont use @bot.event in cogs or whatever it says in docs
    @commands.Cog.listener()
    async def on_message(message): ##this not finished (Emoji dont touch it!) Edit: gotcha
        if message.author.bot:
            return
    
async def setup(bot):
    await bot.add_cog(LevelCommands(bot))

#dump or dumps?
#Where is my mind?

#copyright gurkinsoft 2025