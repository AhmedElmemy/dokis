import discord, random, asyncio
from discord.ext import commands as client


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self.f = open("changelog.txt", "r")

    @client.command()
    async def changelog(self,ctx):
        e = discord.Embed(title=f"A bug-fixing update! This has been changed on August 2, 2019. Version: {self.b.config['version']}",
                          description=f"```{self.f.read()}```", color=int(self.b.config[self.b.doki]["embed_color"], base=16))
        e.set_author(name=f"The Changelog for {self.b.doki}.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
