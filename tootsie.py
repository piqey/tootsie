import os
import random

import discord
from dotenv import load_dotenv

MESSAGE_DM_REPLIES = (
    "I don't know how to respond to this situation.",
    "My creator did not think this far ahead. Or did he?",
    "I'm a bot that makes fart noises, why are you messaging me?",
    "Are you looking for an easter egg or something?",
    "I hope you don't keep sending me these messages."
)

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


@client.event
async def on_message(message):
    if (isinstance(message.channel, discord.channel.DMChannel) and
            message.author != client.user):
        print(f"Received a DM from {message.author}, sending response...")
        await message.channel.send(random.choice(MESSAGE_DM_REPLIES))
        print(f"Sent a response to {message.author}'s DM.")


client.run(TOKEN)
