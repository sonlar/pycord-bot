import discord
from dotenv import load_dotenv
from os import getenv
import re

load_dotenv()
discord_token = getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.search(r'd+i+c+k+', message.content, re.IGNORECASE):
        await message.channel.send('butt')
    if re.search(r'h+o+w+', message.content, re.IGNORECASE):
        await message.channel.send('idk lol')

client.run(discord_token)
