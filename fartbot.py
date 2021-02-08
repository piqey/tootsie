# Import native dependencies
from random import choice

# Import installed dependencies
from discord.ext import commands

# Import our own files
from constants import PRINTS
from sound import soundManager

SOUND_SUBDIR = "farts"


def pickFart():
    sounds = soundManager.getDict(SOUND_SUBDIR)
    return choice(list(sounds.keys()))


def eHandler(e):
    if e is not None:
        print(PRINTS["FART_ERROR"].format(error=e))


# Make FartBot subclass to add useful functions/methods
class FartBot(commands.Bot):
    # Method to check if bot is connected to a voice channel in a guild
    def isConnected(self, guild):
        vc = next((inst for inst in self.voice_clients if inst.guild == guild), None)
        return vc and vc.is_connected() or False

    # Method used to make the bot join a voice channel, fart & leave
    async def fart(self, voiceChannel, reps=1):
        # Get channel name
        channel = voiceChannel.name

        # Join voice channel
        vc = await voiceChannel.connect()

        # Stream the sound
        for _ in range(reps):
            if vc.is_connected():
                await soundManager.playSound(
                    vc,
                    pickFart(),
                    group=SOUND_SUBDIR,
                    after=eHandler
                )
            else:
                print(PRINTS["FART_DISCONNECTED"])
                break

        # Announce in the script window that we're done doing our job
        print(PRINTS["FART_PLAYED"].format(channel=channel))

        # Disconnect after we're done ruining the moment
        print(PRINTS["DISCONNECTING"])
        await vc.disconnect()
        print(PRINTS["DISCONNECTED"].format(channel=channel))
