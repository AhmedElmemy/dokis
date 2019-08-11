import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Invite(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def invite(self,ctx):
        e = discord.Embed(title="My invite link!", description="F-fine! I guess I can join someone else's server, too... but I probably won't like it!", colour=conf.norm)
        e.add_field(name="Here goes...", value="[Click here to invite me!](https://discordbots.org/bot/433834936450023424)", inline=True)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Invite(bot))
