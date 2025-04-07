import discord
from discord.ext import commands
import json
from main import bot

def guildcheck(guildid):
    with open("data/levels.json", 'r',encoding='utf=8') as file:
        levels = json.load(file)
        gid = str(guildid)
    if gid not in levels:
        levels[gid]= {}
        with open("data/levels.json", 'w',encoding='utf=8') as f1:
            json.dump(levels, f1)

def usercheck(guildid, userid):
    with open("data/levels.json", 'r',encoding='utf=8') as file:
        levels = json.load(file)
        gid = str(guildid)
        uid = str(userid)
    if uid not in levels[gid]:
        levels [gid] [uid] = [0,0]
        with open("data/levels.json", 'w',encoding='utf=8') as f1:
            json.dump(levels, f1)

class LevelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @commands.hybrid_command(name="level")
    async def level(self,ctx):
        userid = ctx.author.id
        guildid = ctx.guild.id
        guildcheck(guildid)
        usercheck(guildid,userid)
        with open("data/levels.json", 'r', encoding='utf-8') as file:
            levels = json.load(file)
        gid = str(guildid)
        uid = str(userid)
        xp = levels[gid] [uid] [0]
        lvl = levels[gid] [uid] [1]
        await ctx.send(f'Your xp and level is{xp, lvl}')

    @bot.event
    async def on_message(message):
        if message.author.bot:
            return
    
async def setup(bot):
    await bot.add_cog(LevelCommands(bot))

#dump or dumps?
#Where is my mind?