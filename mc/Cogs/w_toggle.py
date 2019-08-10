import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    @client.has_permissions(manage_messages=True)
    async def toggle(self,ctx):
        try:
            if ctx.guild.id not in conf.w_tog_off: # Disable chat triggers.
                conf.w_tog_off.insert(0, ctx.guild.id)
                await ctx.send("I won't react to triggers in chat anymore.")
            else: # Enables chat triggers.
                conf.w_tog_off.remove(ctx.guild.id)
                await ctx.send("Fine, I'll start reacting to triggers again.")
        except: # Do not run in private messages.
            await ctx.send("This command doesn't work in PMs.")


def setup(bot):
    bot.add_cog(toggle(bot))
