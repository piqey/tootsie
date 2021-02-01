# Import native dependencies
import os

# Import installed dependencies
import discord
from dotenv import load_dotenv

# Import our own files
import events

# Mount dotenv
load_dotenv()
# Grab the token from the environment file
TOKEN = os.getenv("DISCORD_TOKEN")

# Store an instance the Discord Client class
client = discord.Client()

# Append client events with our own
events.appendEvents(client)

# Run the client
client.run(TOKEN)
