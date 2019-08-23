import discord, asyncio
import discord.ext.commands as client


class Ping(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def ping(self, ctx):
        e = discord.Embed(colour=self.b.config['success_embed_color'])
        e.add_field(name='Pong! :ping_pong:', value=f'`{round(self.b.latency * 1000)}ms`', inline=False)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Ping(bot))