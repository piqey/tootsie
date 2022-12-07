# Import our own files
from constants import PRINTS


def appendEvents(bot):
    @bot.event
    async def on_ready():
        # Announce one's presence
        print(PRINTS["READY"].format(user=bot.user))

        # Loop through all the guilds (servers) the bot is a part of
        for guild in bot.guilds:
            # Print the current guild
            print(PRINTS["FOUND_GUILD"].format(user=bot.user, guild=guild.name, id=guild.id))
