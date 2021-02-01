# Import native dependencies
import random

# Import installed dependencies
import discord


# Define some constants
MESSAGE_DM_REPLIES = (
    "I don't know how to respond to this situation.",
    "My creator did not think this far ahead. Or did he?",
    "I'm a bot that makes fart noises, why are you messaging me?",
    "Are you looking for an easter egg or something?",
    "I hope you don't keep sending me these messages."
)


def appendEvents(client):
    @client.event
    async def on_ready():
        # Announce oneself
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
            await message.channel.send(random.choice(MESSAGE_DM_REPLIES))
            # Done sending the message
            print(f"Sent a response to {message.author}'s DM.")
