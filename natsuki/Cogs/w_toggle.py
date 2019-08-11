import discord, asyncio
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
            await ctx.send("Fine, I won't react to chat triggers.")
        else: # Enables chat triggers.
            conf.w_tog_off.remove(ctx.guild.id)
            await ctx.send("Fine, I'll react to chat triggers.")
    

def setup(bot):
    bot.add_cog(toggle(bot))
