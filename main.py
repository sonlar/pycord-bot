import discord
from dotenv import load_dotenv
from os import getenv
import re
import wordle

load_dotenv()
discord_token = getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client)
daily_stats = wordle.play_wordle()
print(daily_stats)

@tree.command(
    name="wordle",
    description="Check Today's Penis Gambit",
    guild=discord.Object(id=547041619656966185)
)
async def wordle(interaction):
    await interaction.response.send_message(daily_stats)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await tree.sync(guild=discord.Object(id=547041619656966185))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if re.search(r"d+i+c+k+", message.content, re.IGNORECASE):
        await message.channel.send("butt")
    if re.search(r"h+o+w+", message.content, re.IGNORECASE):
        await message.channel.send("idk lol")

client.run(discord_token)
