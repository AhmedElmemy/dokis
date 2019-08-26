import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Swears(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def swear(self,ctx):
        swear_list = ["HECK!", "DARN IT!", "POOP!", "CRUD!", "FRICK!", "SON OF A BISCUIT!", "MOTHERTRUCKER!"]
        async with ctx.message.channel.typing():
            await asyncio.sleep(self.b.config['type_speed'])
        await ctx.send(random.choice(swear_list))


def setup(bot):
    bot.add_cog(Swears(bot))
