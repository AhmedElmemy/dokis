import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Tickle(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self.laughs = ["Oh! Hehehe!", "P-Please! Stop it! Ehehe!", "Hey, that tickles! Hahaha!", "HAHAHAHAHAHA! *snort*", "H-Hey! That's my ticklish spot!! :laughing:"]

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def tickle(self,ctx):
        if ctx.guild is None: # PM's. Always do Act 1.
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(self.laughs))

        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            if ctx.guild.id not in conf.act2: # Act 1
                await ctx.send(random.choice(self.laughs))
            else: # Act 2
                laughs2 = ["Ahahaha! Yes, just like that!", "HEHEHEHEHEHEHE!!!", "Hahahahahaha!!!", "AHAHAHAHAHAHAHAHAHA!!!"]
                await ctx.send(random.choice(laughs2))


def setup(bot):
    bot.add_cog(Tickle(bot))
