# Import native dependencies
import os

# Import our own files
from soundmanager import SoundManager


def getAbsoluteFromRelative(path):
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    return os.path.join(fileDir, path)


SOUND_DIR_REL = "sound\\"
SOUND_DIR = getAbsoluteFromRelative(SOUND_DIR_REL)

# Create a SoundManager instance for our purposes
soundManager = SoundManager(SOUND_DIR)
