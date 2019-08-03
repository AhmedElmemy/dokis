import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf
#Imports


class Swears(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def swear(self,ctx): 
        swear_list = ["HECK!", "DARN IT!", "POOP!", "CRUD!", "FRICK!", "SON OF A BISCUIT!", "MOTHERTRUCKER!"]        
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(swear_list))


def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Swears(bot))
