# Import native dependencies
from random import choice

# Import our own files
from constants import BASICS, PRINTS, MESSAGES
import discord
from discord.commands import Option
from sound import soundManager

def pickReply():
    return choice(MESSAGES["FART_AFFIRMATION"])


def addCommands(bot):
    # TODO: Disable if bot is already in a voice channel
    @bot.slash_command(
        name = "play",
        description = "Let me know when you're in the mood ;)",
        pass_context = True
    )
    async def playSound(
        ctx: discord.ApplicationContext,
        group: Option(
            str,
            "The sound group to sample from",
            required = True,
            choices = [*set(soundManager.sounds.keys())],
            default = "farts"
        ),
        reps: Option(
            int,
            "How many times to play a sound (be reasonable)",
            required = True,
            default = 1
        ),
        delay: Option(
            float,
            "Overrides the sound queue, instead playing sounds after a specified delay",
            required = False
        )
    ):
        if not bot.isConnected(ctx.guild):
            # Get the user's voice channel
            voiceChannel = (ctx.author.voice and ctx.author.voice.channel)

            # Only join and wreak havoc if the user is in a voice channel
            if voiceChannel is not None:
                # Communicate with the command's user
                await ctx.respond(pickReply().format(user=ctx.author.name))

                # You know what this does
                await bot.play(voiceChannel, group, min(len(soundManager.sounds[group]), reps), delay)
            else:
                print(PRINTS["FART_FAILED"])
                await ctx.respond(MESSAGES["FART_FAILED"].format(user=ctx.author.name))
        else:
            await ctx.channel.send(MESSAGES["FART_FAILED_BUSY"])
