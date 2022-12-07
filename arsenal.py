# Import native dependencies
from random import choice

# Import our own files
from constants import BASICS, PRINTS, MESSAGES
from typing import Optional


def pickReply():
    return choice(MESSAGES["FART_AFFIRMATION"])


def addCommands(bot):
    # TODO: Disable if bot is already in a voice channel
    @bot.slash_command(
        name = "fart",
        description = "Let me know when you're in the mood ;)",
        pass_context = True
    )
    async def forceFart(ctx, reps: Optional[int]):
        if reps is None:
            reps = 1

        if not bot.isConnected(ctx.guild):
            # Get the user's voice channel
            voiceChannel = (ctx.author.voice and
                            ctx.author.voice.channel)

            # Only join and wreak havoc if the user is in a voice channel
            if reps > BASICS["FART_MAX"]:
                await ctx.respond(MESSAGES["FART_TERRIBLE_PERSON"])
            elif voiceChannel is not None:
                # Communicate with the command's user
                await ctx.respond(pickReply().format(user=ctx.author.name))

                # You know what this does
                await bot.fart(voiceChannel, reps)
            else:
                print(PRINTS["FART_FAILED"])
                await ctx.respond(MESSAGES["FART_FAILED"].format(user=ctx.author.name))
        else:
            await ctx.channel.send(MESSAGES["FART_FAILED_BUSY"])
