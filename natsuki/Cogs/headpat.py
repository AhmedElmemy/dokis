import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf

class Headpat(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def headpat(self,ctx): 
        headpat_list = ["Hey! Don't pat me so hard!", "Geez, you're gonna mess up my hair!", "...okay, I guess that kinda felt nice...", "What do I look like, a puppy??", "T-thanks, I guess..."]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(headpat_list))



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Headpat(bot))
