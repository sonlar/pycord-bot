import discord
from dotenv import load_dotenv
from os import getenv
import re
import last_wordle

load_dotenv()
discord_token = getenv("DISCORD_TOKEN")
guild_id = getenv("GUILD_ID")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client)

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.search(r"d+i+c+k+", message.content, re.IGNORECASE):
        await message.channel.send("butt")
    if re.search(r"h+o+w+", message.content, re.IGNORECASE):
        await message.channel.send("idk lol")

client.run(discord_token)
