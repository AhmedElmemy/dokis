import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf


class Delete(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def delete(self,ctx, *, arg1=None):
        if arg1 is None:
            await ctx.send("What do you need me to delete?")
        elif arg1 == "Sayori" or arg1 == "Natsuki" or arg1 == "Yuri" or arg1 == "sayori" or arg1 == "natsuki" or arg1 == "yuri" or arg1 == f"<@{conf.sayori_id}" or arg1 == f"<@{conf.natsuki_id}" or arg1 == f"<@{conf.yuri_id}":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send("Ahahahaha! You know, I tried that once. Didn't really work out well in the long run.")

        elif arg1 == "me" or arg1 == "Me" or arg1 == "mE" or arg1 == "ME":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send("Why would i want to do that?")

        elif arg1 == "<@270057011251642368>":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send("Why would you want to delete the man who gave you the ability to use me? Shame on you!")

        elif arg1 == f"<@{conf.monika_id}>" or arg1 == "Monika":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send("Ahahahaha! No.")
        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await ctx.send(f'os.remove("./characters/{arg1}.chr")')


def setup(bot):
    bot.add_cog(Delete(bot))
