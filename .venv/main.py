import discord
from discord.ext.commands import Bot
from modules.ping import Ping

intents = discord.Intents.all()
bot = Bot(intents=intents, command_prefix='!')
global token

with open('token.txt', 'r') as file:
    token = file.read()

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user} (ID: {bot.user.id})')

async def main():
    await bot.load_extension('modules.ping')
    #---------------------------------------------------------------------------------
    # Don't forget to enter your bot token in token.txt from Discord Developer Portal!
    #---------------------------------------------------------------------------------
    await bot.start(token)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
