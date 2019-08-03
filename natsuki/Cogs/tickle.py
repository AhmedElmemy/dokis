import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf
#Imports


class Tickle(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def tickle(self,ctx): 
        laughs = ["H-hey! Cut that out!! Ahahahaha!!", "Hehehehe!!", "Ehehehe!", "STOP IT! STOP! EHEHEHEHE!!!", "I'm gonna break your ribs for this! Hehehe!"]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(laughs))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Tickle(bot))
