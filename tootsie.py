# Import native dependencies
import os

# Import installed dependencies
from dotenv import load_dotenv
from discord import Intents

# Import our own files
from constants import BASICS
from fartbot import FartBot
import events
import arsenal

# Mount dotenv
load_dotenv()
# Grab the token from the environment file
TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

# Store an instance the Discord bot class
bot = FartBot(
	command_prefix = BASICS["CMD_PREFIX"],
	intents = intents
)

# Append bot events with our own
events.appendEvents(bot)
# Add commands to the bot instance
arsenal.addCommands(bot)

# Run the bot
bot.run(TOKEN)
