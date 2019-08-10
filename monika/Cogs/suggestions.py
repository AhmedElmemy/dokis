import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Suggestions(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def suggest(self,ctx):
        e = discord.Embed(title="Wow! You wanna suggest something? Alrighty!",description="[Click here](https://forms.gle/beiyyP3F1BEsbuVF8) to go to the suggestions form!", color=conf.norm)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Suggestions(bot))
