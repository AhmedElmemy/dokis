import discord, asyncio, json, discord.utils
from discord.ext import commands
from Cogs.config import conf


def dev(): # Any command with this check can only be run with those whose ID is in the "admins" array in the config.py file.
    def predicate(ctx):
        if ctx.author.id in conf.admins:
            return True
        else:
            pass
    return commands.check(predicate)

