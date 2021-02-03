# Import native dependencies
import os

# Import installed dependencies
import discord
import asyncio


# Make a class for all the sound-managing stuff we need
class SoundManager:
    def __init__(self, root):
        self.sounds = {}
        self.root = root

        self._loadSounds()

    def addSound(self, path, group="root"):
        if group not in self.sounds:
            self.sounds[group] = {}

        source = discord.FFmpegPCMAudio(path)

        fileName = os.path.basename(path)
        self.sounds[group][fileName] = source

    # TODO: Possibly make file grouping better (subdicts)
    def _loadSounds(self):
        for subpath, dirs, fileNames in os.walk(self.root):
            subdirPath = subpath[(len(self.root) - len(subpath)):]
            dirName = (subpath != self.root and subdirPath)

            for fileName in fileNames:
                filePath = os.path.join(subpath, fileName)
                self.addSound(filePath, dirName)

    def getSound(self, name, group="root"):
        return self.sounds[group][name]

    def getDict(self, group="root"):
        return self.sounds[group]

    def getList(self, group="root"):
        return list(self.sounds[group])

    def _replaceSound(self, name, group=None):
        if group is not None:
            path = os.path.join(self.root, group, name)
        else:
            path = os.path.join(self.root, name)

        self.sounds[group][name] = discord.FFmpegPCMAudio(path)

    async def playSound(self, vc, name, group=None, after=lambda e: print(e)):
        # Start streaming the sound
        vc.play(self.getSound(name, group), after=after)

        # Wait until the sound is finished playing
        while vc is not None and vc.is_playing():
            await asyncio.sleep(1)

        # Stop the player just in case
        vc.stop()

        # Reload the sound for later use
        self._replaceSound(name, group)
