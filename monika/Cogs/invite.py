import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Invite(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def invite(self,ctx): 
        e = discord.Embed(title="My invite link!", description="Oh, you would like to add me to a new server? You can get my link below!", colour=conf.norm)
        e.add_field(name="Here it is!", value="[Click here to invite me!](https://discordbots.org/bot/436351740787294208)", inline=True)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Invite(bot))
