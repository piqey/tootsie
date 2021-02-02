# Import native dependencies
import random

# Import our own files
from constants import BASICS, PRINTS, MESSAGES
from sound import soundManager


SOUND_SUBDIR = "farts"


def pickFart():
    sounds = soundManager.getDict(SOUND_SUBDIR)
    return random.choice(list(sounds.keys()))


def pickReply():
    return random.choice(MESSAGES["FART_AFFIRMATION"])


def eHandler(e):
    if e is not None:
        print(PRINTS["FART_ERROR"].format(error=e))


def addCommands(bot):
    # TODO: Disable if bot is already in a voice channel
    @bot.command(
        name="fart",
        help="Forces the bot to do what it does best",
        pass_context=True
    )
    async def forceFart(context, reps=1):
        # Get the user's voice channel
        voiceChannel = (context.message.author.voice and
                        context.message.author.voice.channel)

        # Only join and wreak havoc if the user is in a voice channel
        if reps > BASICS["FART_MAX"]:
            await context.channel.send(MESSAGES["FART_TERRIBLE_PERSON"])
        elif voiceChannel is not None:
            # Communicate with the command's user
            reply = pickReply().format(user=context.author.name)
            await context.channel.send(reply)

            # Grab voice channel name
            channel = voiceChannel.name

            # Join voice channel
            await voiceChannel.connect()

            # Store VoiceClient instance for ease of access
            vc = context.voice_client

            # Stream the sound (a number of times equal to rep)
            for _ in range(reps):
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
            reply = MESSAGES["FART_FAILED"].format(user=context.author.name)
            await context.channel.send(reply)
