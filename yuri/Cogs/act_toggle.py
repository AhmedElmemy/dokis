import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class act_toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    @client.has_permissions(manage_messages=True)
    @client.guild_only()
    async def act1(self,ctx): 
        if ctx.guild.id in conf.act2: # Switch to Act 1 if in Act 2
            conf.act2.remove(ctx.guild.id)
            await ctx.send("O-Oh... Wh-What just happened? I feel funny...")
        else:
            await ctx.send("I'm already in my 'Act 1' mode. And I'd prefer if it stayed that way...")

    @client.command()
    @client.has_permissions(manage_messages=True)
    @client.guild_only()
    async def act2(self,ctx): 
        if ctx.guild.id not in conf.act2: # Switch to Act 2 if in Act 1
            conf.act2.insert(0, ctx.guild.id)
            await ctx.send("Ha. Haha. HAHAHAHAHHAHAHA!!!!")
        else:
            await ctx.send("Oh, you little cutie! I'm already in Act 2 mode! Ahaha!!")


def setup(bot):
    bot.add_cog(act_toggle(bot))
