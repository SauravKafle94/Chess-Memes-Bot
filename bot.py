import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

# Load the secret token from the .env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='chessmeme')
async def chessmeme(ctx):
    url = "https://meme-api.com/gimme/AnarchyChess"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(title=data['title'], color=0x7289da)
                embed.set_image(url=data['url'])
                await ctx.send(embed=embed)
            else:
                await ctx.send("Google en passant. (Failed to fetch meme)")

keep_alive()
# Tell the bot to use the hidden token
bot.run(os.getenv('DISCORD_TOKEN'))
