import discord
import config
from cogs import general_cog
from cogs import music_cog


from discord.ext import commands


TOKEN = config.token

intents=discord.Intents.all()


bot = commands.Bot(command_prefix=commands.when_mentioned_or("."),
                    description="Private Discord Bot for kekw Server",
                    intents=intents)

bot.remove_command('help')


bot.add_cog(music_cog.Music(bot))
bot.add_cog(general_cog.General(bot))

bot.run(TOKEN)
