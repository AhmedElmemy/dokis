import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Headpat(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def headpat(self,ctx):
        headpat_list = ["Ahaha!~ I-I'm not sure what to say!", "Be careful; you may knock my bow down!", "E-Easy now!", "This doesn't really seem like the type of thing one does to their President, but I suppose I'll let it slide!"]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(headpat_list))


def setup(bot):
    bot.add_cog(Headpat(bot))
