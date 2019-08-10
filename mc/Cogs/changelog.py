import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self.f = open("../changelog.txt", "r")

    @client.command()
    async def changelog(self,ctx):
        e = discord.Embed(title=f"A bug-fixing update! This has been changed on August 2, 2019. Version: {conf.version}",
                          description=f"```{self.f.read()}```", color=conf.norm)
        e.set_author(name=f"The Changelog for {conf.name}.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
