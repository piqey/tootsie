# Import native dependencies
import random

# Import our own files
from constants import BASICS, PRINTS, MESSAGES


def pickReply():
    return random.choice(MESSAGES["FART_AFFIRMATION"])


def addCommands(bot):
    # TODO: Disable if bot is already in a voice channel
    @bot.command(
        name="fart",
        help="Forces the bot to do what it does best",
        pass_context=True
    )
    async def forceFart(context, reps=1):
        if not bot.isConnected(context.guild):
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

                # You know what this does
                await bot.fart(voiceChannel, reps)
            else:
                print(PRINTS["FART_FAILED"])
                reply = MESSAGES["FART_FAILED"].format(user=context.author.name)
                await context.channel.send(reply)
        else:
            await context.channel.send(MESSAGES["FART_FAILED_BUSY"])
