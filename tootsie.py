import os

import discord
from dotenv import load_dotenv

# Mount dotenv
load_dotenv()
# Grab the token from the environment file
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f"yoooo {client.user} is in the house")

client.run(TOKEN)
