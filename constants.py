# Import native dependencies
import os

# Import installed dependencies
import discord

# Basic constants
BASICS = {
    "CMD_PREFIX": "]"
}

# Prints
PRINTS = {
    # Define some stuff that only appear in the program window
    "READY": "yoooo {user} is in the house",
    "FOUND_GUILD": "{user} is connected to {guild} ({id})",

    # DM-related prints
    "DM_RECEIVED": "Received a DM from {author}, sending response...",
    "DM_REPLIED": "Sent a response to {author}'s DM.",

    # Fart-related prints
    "FART_FAILED": "Unable to rip ass; user is not in a voice channel.",
    "FART_PLAYED": "Finished deploying weapons in {channel}.",
    "FART_ERROR": "Unable to rip ass; error encountered: {error}",

    # General use prints
    "DISCONNECTING": "Disconnecting...",
    "DISCONNECTED": "Disconnected from {channel}."
}

# Messages
MESSAGES = {
    # Define some different messages that won't ever change
    "DM_RESPONSES": (
        "I don't know how to respond to this situation.",
        "My creator did not think this far ahead. Or did he?",
        "I'm a bot that makes fart noises, why are you messaging me?",
        "Are you looking for an easter egg or something?",
        "I hope you don't keep sending me these messages."
    )
}


# Sound stuff, doing it this way to make sure the files load initially
def getAbsoluteFromRelative(path):
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    return os.path.join(fileDir, path)


def fastPCM(relative):
    return discord.FFmpegPCMAudio(getAbsoluteFromRelative(relative))


SOUND_DIR_REL = "sound\\"
SOUND_DIR = getAbsoluteFromRelative(SOUND_DIR_REL)

# Recursively get a list of sounds
SOUNDS = {}

for path, directories, filenames in os.walk(SOUND_DIR):
    sources = {}

    for filePath in filenames:
        sources[filePath] = fastPCM(os.path.join(path, filePath))

    if path == SOUND_DIR:
        # Would rather have files right inside SOUND_DIR be listed under
        # their own directory or else picking random choices from the files
        # directly inside would be difficult (getting a list when you are
        # expecting a sound
        SOUNDS["root"] = sources
    else:
        SOUNDS[path[(len(SOUND_DIR) - len(path)):]] = sources
