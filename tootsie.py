import os

import discord
from dotenv import load_dotenv

# Mount dotenv
load_dotenv()
# Grab the token from the environment file
TOKEN = os.getenv("DISCORD_TOKEN")

# Store an instance the Discord Client class
client = discord.Client()

# Attach to the client's events
@client.event
async def on_ready():
    # Announce oneself
    print(f"yoooo {client.user} is in the house")

    # Loop through all the guilds (servers) the bot is a part of
    for guild in client.guilds:
        # Print the current guild
        print(f"{client.user} is connected to {guild.name} (ID: {guild.id})")

client.run(TOKEN)
