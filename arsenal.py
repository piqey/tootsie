# Import native dependencies
import random

# Import our own files
from constants import PRINTS
from sound import soundManager


SOUND_SUBDIR = "farts"


def pickFart():
    sounds = soundManager.getDict(SOUND_SUBDIR)
    return random.choice(list(sounds.keys()))


def eHandler(e):
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

            # Store VoiceClient instance for ease of access
            vc = context.voice_client

            # Stream the sound
            await soundManager.playSound(
                vc,
                pickFart(),
                group=SOUND_SUBDIR,
                after=eHandler
            )

            # Announce in the script window that we're done doing our job
            print(PRINTS["FART_PLAYED"].format(channel=channel))

            # Disconnect after we're done ruining the moment
            print(PRINTS["DISCONNECTING"])
            await vc.disconnect()
            print(PRINTS["DISCONNECTED"].format(channel=channel))
        else:
            print(PRINTS["FART_FAILED"])
