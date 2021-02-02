# Import native dependencies
import random

# Import installed dependencies
import asyncio

# Import our own files
from constants import PRINTS, SOUNDS


SOUND_SUBDIR = "farts"


def pickFart():
    return random.choice(SOUNDS[SOUND_SUBDIR])


def handleErrorEncounter(e):
    if e is not None:
        print(PRINTS["FART_ERROR"].format(error=e))


def addCommands(bot):
    @bot.command(
        name="fart",
        help="Forces the bot to do what it does best",
        pass_context=True
    )
    async def forceFart(context):
        # Get the user's voice channel
        voiceChannel = (context.message.author.voice and
                        context.message.author.voice.channel)

        # Only join and wreak havoc if the user is in a voice channel
        if voiceChannel is not None:
            # Grab voice channel name
            channel = voiceChannel.name
            # Join voice channel
            await voiceChannel.connect()

            # Create StreamPlayer
            fart = pickFart()
            context.voice_client.play(fart, after=handleErrorEncounter)

            # Wait until the sound is finished playing
            while (context.voice_client is not None and
                    context.voice_client.is_playing()):
                await asyncio.sleep(1)

            # Stop the player just in case
            context.voice_client.stop()
            # Announce in the script window that we're done doing our job
            print(PRINTS["FART_PLAYED"].format(channel=channel))

            # Disconnect after we're done ruining everyone's day
            print(PRINTS["DISCONNECTING"])
            await context.voice_client.disconnect()
            print(PRINTS["DISCONNECTED"].format(channel=channel))
        else:
            print(PRINTS["FART_FAILED"])
