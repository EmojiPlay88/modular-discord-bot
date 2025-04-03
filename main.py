import discord
import os
from discord.ext.commands import Bot

global token

intents = discord.Intents.all()
bot = Bot(intents=intents, command_prefix='!')

with open('token.txt', 'r') as file:
    token = file.read()

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
    import asyncio
    asyncio.run(main())
