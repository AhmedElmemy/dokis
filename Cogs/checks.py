import discord, discord.utils, json
from discord.ext import commands


config = json.loads(open("config.json", "r").read())
def dev(): # Any command with this check can only be run with those whose ID is in the "admins" array in the config.py file.
    def predicate(ctx):
        if str(ctx.author.id) in config['admins']:
            return True
        else:
            pass
    return commands.check(predicate)
