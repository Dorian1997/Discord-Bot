import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

bot.remove_command("help")


@bot.event

async def on_ready():

    await bot.add_cog(help_cog(bot))

    await bot.add_cog(music_cog(bot))

#start the bot with token
bot.run("TOKEN")