# Import native dependencies
import os
from random import sample

# Import installed dependencies
from discord.ext import commands

# Import our own files
from constants import PRINTS
from sound import soundManager, SOUND_DIR

def pickSounds(group, reps=1):
    sounds = soundManager.getDict(group)
    return sample(list(sounds.keys()), reps)


def eHandler(e):
    if e is not None:
        print(PRINTS["FART_ERROR"].format(error=e))


# Make FartBot subclass to add useful functions/methods
class FartBot(commands.Bot):
    # Method to check if bot is connected to a voice channel in a guild
    def isConnected(self, guild):
        vc = next((inst for inst in self.voice_clients if inst.guild == guild), False)
        return vc and vc.is_connected()

    # Method used to make the bot join a voice channel, fart & leave
    async def play(self, voiceChannel, group, reps=1, delay=None):
        # Get channel name
        channel = voiceChannel.name

        # Join voice channel
        vc = await voiceChannel.connect()

        # Get sample of farts list
        sounds = pickSounds(group, reps)

        # Stream the sound
        for _ in range(reps):
            if vc.is_connected():
                await soundManager.playSound(
                    vc,
                    sounds.pop(),
                    group=group,
					delay=delay,
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
