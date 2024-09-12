import check
import concurrent.futures
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import epic
import json
from os import getenv
import re
import last_wordle

load_dotenv()
discord_token = getenv("DISCORD_TOKEN")
guild_id = getenv("GUILD_ID")
announcement_channel = getenv("ANNOUNCEMENT_CHANNEL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client)

check

def wordle_check():
    score = last_wordle.check_time()
    return score

@tree.command(
    name="wordle",
    description="Check Today's Penis Gambit",
    guild=discord.Object(id=guild_id)
)
async def wordle(interaction):
    await interaction.response.send_message(wordle_check())

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await tree.sync(guild=discord.Object(id=guild_id))

    announcement.start()
    print("starting announcement")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.search(r"d+i+c+k+", message.content, re.IGNORECASE):
        await message.channel.send("butt")
    if re.search(r"h+o+w+", message.content, re.IGNORECASE):
        await message.channel.send("idk lol")

@tasks.loop(minutes=1)
async def announcement():
    guild = client.get_guild(int(guild_id))
    channel_id = guild.get_channel(int(announcement_channel))
    print("in announcement")
    bool_val, epoch = epic.has_expired()
    if bool_val:
        print("bool was True")
        await channel_id.send(content=f"CLAIM BEFORE: <t:{epoch}:f>",file=discord.File("./pics/test.png"))

client.run(discord_token)
