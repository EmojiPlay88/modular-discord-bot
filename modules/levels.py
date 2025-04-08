import discord
import json
import os
from discord.ext import commands

#------------------------------------------
#ids in data file are stored as str NOT int
#------------------------------------------

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
        levels[guildid][userid] = [0,1]
        with open("data/levels.json", 'w',encoding='utf=8') as file:
            json.dump(levels, file)

def lvlup(guildid, userid):
    levels = loadJson()
    lvl = levels[guildid][userid][1]
    if levels[guildid][userid][0] >= 10*lvl:
        levels[guildid][userid][1] += 1
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

    @commands.Cog.listener()
    async def on_message(self,message):
        if not message.author.bot:
            guildid = str(message.guild.id)
            userid = str(message.author.id)
            guildcheck(guildid)
            usercheck(guildid, userid)
            levels = loadJson()
            levels[guildid][userid][0] += 5
            with open("data/levels.json", 'w',encoding='utf=8') as file:
                json.dump(levels, file)
            lvlup(guildid, userid)
        else:
            return

async def setup(bot):
    await bot.add_cog(LevelCommands(bot))

#dump or dumps?
#Where is my mind?

#Emoji dont touch it! Edit: gotcha

#copyright gurkinsoft 2025 Edit: whyyyyyyy?
