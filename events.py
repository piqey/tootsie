# Import native dependencies
import random

# Import installed dependencies
import discord

# Import our own files
from constants import PRINTS, MESSAGES


def appendEvents(bot):
    @bot.event
    async def on_ready():
        # Announce one's presence
        print(PRINTS["READY"].format(user=bot.user))

        # Loop through all the guilds (servers) the bot is a part of
        for guild in bot.guilds:
            # Print the current guild
            print(PRINTS["FOUND_GUILD"].format(user=bot.user, guild=guild.name,
                  id=guild.id))

    @bot.event
    async def on_message(message):
        # Confirm that the message was received in the bot's DMs
        if (isinstance(message.channel, discord.channel.DMChannel) and
                message.author != bot.user):
            # Start sending the message
            print(PRINTS["DM_RECEIVED"].format(author=message.author))
            await message.channel.send(random.choice(MESSAGES["DM_RESPONSES"]))
            # Done sending the message
            print(PRINTS["DM_REPLIED"].format(author=message.author))
