# Import native dependencies
import random

# Import installed dependencies
import discord

# Import our own files
import constants.messages as MESSAGES


def appendEvents(client):
    @client.event
    async def on_ready():
        # Announce one's presence
        print(f"yoooo {client.user} is in the house")

        # Loop through all the guilds (servers) the bot is a part of
        for guild in client.guilds:
            # Print the current guild
            print(f"{client.user} is connected to {guild.name} ({guild.id})")

    @client.event
    async def on_message(message):
        # Confirm that the message was received in the bot's DMs
        if (isinstance(message.channel, discord.channel.DMChannel) and
                message.author != client.user):
            # Start sending the message
            print(f"Received a DM from {message.author}, sending response...")
            await message.channel.send(random.choice(MESSAGES.DM_RESPONSES))
            # Done sending the message
            print(f"Sent a response to {message.author}'s DM.")
