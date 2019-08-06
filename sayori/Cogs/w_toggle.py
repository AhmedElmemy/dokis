import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf


class toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.has_permissions(manage_messages=True)
    async def toggle(self,ctx):
        if ctx.guild.id in conf.w_tog_on: # Disable chat triggers.
            conf.w_tog_on.remove(ctx.guild.id)
            await ctx.send("Okay, I won't react to the triggers in chat!")
        elif ctx.guild.id not in conf.w_tog_on: # Enables chat triggers.
            conf.w_tog_on.insert(0, ctx.guild.id)
            await ctx.send("Okay, I'll react to the triggers in chat!")
        else: # Do not run in private messages.
            await ctx.send("Hey so an error happened, i'll just leave a code for you to report! ERROR: 17: Returned ELSE, is this in a PM?")
    

def setup(bot):
    bot.add_cog(toggle(bot))
