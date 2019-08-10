import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Invite(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def invite(self,ctx): 
            e = discord.Embed(title="My invite link...", description="Here's the link you can use to invite me to your server. Why you would, I don't know.", color=conf.norm)
            e.add_field(name="Enjoy!", value="[Click here to invite me!](https://discordbots.org/bot/596407346176065552)", inline=True)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Invite(bot))
