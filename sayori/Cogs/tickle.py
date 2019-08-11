import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Tickle(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def tickle(self,ctx):
        laughs = ["Hehehehehe!~", "Ahahahaha!!", "*giggles*", "**PFFFT AHAHAHAHAHAHHAHAHAHHAHA!!!!!**", "Ehehe!~", "WAHAHAHAHAHA!!!~"]        
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(laughs))


def setup(bot):
    bot.add_cog(Tickle(bot))
