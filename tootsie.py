# Import native dependencies
import os

# Import installed dependencies
from discord.ext import commands
from dotenv import load_dotenv

# Import our own files
import constants.config as CONFIG
import events

# Mount dotenv
load_dotenv()
# Grab the token from the environment file
TOKEN = os.getenv("DISCORD_TOKEN")

# Store an instance the Discord bot class
bot = commands.Bot(command_prefix=CONFIG.CMD_PREFIX)

# Append bot events with our own
events.appendEvents(bot)

# Run the bot
bot.run(TOKEN)
