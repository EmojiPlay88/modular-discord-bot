import discord
from discord.ext import commands
import json

class LevelCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="level")
    async def level(self,ctx):
        levels = {}
        userid = ctx.author.id
        guildid = ctx.guild.id
        with open("data/levels.json", 'r+', encoding='utf-8') as file:
            levels = json.load(file)

            if guildid not in levels:
                levels [guildid] = {}
                json.dumps(levels)

            if userid not in levels[guildid]:
                levels [guildid] [userid] = [0,0]
                json.dumps(levels)

            json.dump(levels,file)

            lvl = levels[guildid] [userid] [1]
            xp = levels[guildid] [userid] [0]
            await ctx.send(f'Your level and xp is{lvl, xp}')

async def setup(bot):
    await bot.add_cog(LevelCommands(bot))


#holy fuck help me, i rlly want slep