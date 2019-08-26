import discord, asyncio
import discord.ext.commands as client


class Suggestions(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def suggest(self,ctx):
        e = discord.Embed(title="Wow! You wanna suggest something? Alrighty!",description="[Click here](https://forms.gle/beiyyP3F1BEsbuVF8) to go to the suggestions form!", color=int(self.b.config["monika"]["embed_color"], base=16))
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Suggestions(bot))
