import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Act_check(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.guild_only()
    async def act(self,ctx):
            if ctx.guild.id not in conf.act2:
                await ctx.send("I'm on Act 1.")
            else:
                await ctx.send("I'm on Act 2.")


def setup(bot):
    bot.add_cog(Act_check(bot))
