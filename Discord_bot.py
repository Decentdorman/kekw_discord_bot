import discord
import os

from cogs import general_cog
from cogs import music_cog

from dotenv import load_dotenv
from discord.ext import commands


'load_dotenv()'
'TOKEN = os.getenv("DISCORD_TOKEN")'
TOKEN = "MTA0MzY3NDkwNDMyODk0MTU3OQ.GXcbgk.c2-0eakgQPCl6TSdMhrYDxxmSvxyfwbEjpNgPs"

intents=discord.Intents.all()


bot = commands.Bot(command_prefix=commands.when_mentioned_or("."),
                    description="Private Discord Bot for kekw Server",
                    intents=intents)

bot.remove_command('help')


bot.add_cog(music_cog.Music(bot))
bot.add_cog(general_cog.General(bot))

bot.run(TOKEN)
