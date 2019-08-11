import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.has_permissions(manage_messages=True)
    @client.guild_only()
    async def toggle(self,ctx):
        if ctx.guild.id not in conf.w_tog_off: # Disable chat triggers.
            conf.w_tog_off.insert(0, ctx.guild.id)
            await ctx.send("Ok, I guess you don't want to hear from me.")
        else: # Enables chat triggers.
            conf.w_tog_off.remove(ctx.guild.id)
            await ctx.send("Ok, I guess you do want to hear from me.")


def setup(bot):
    bot.add_cog(toggle(bot))
