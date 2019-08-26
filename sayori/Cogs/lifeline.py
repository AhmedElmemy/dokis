import discord, asyncio
import discord.ext.commands as client


class Lifeline(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def lifeline(self,ctx): 
        async with ctx.message.channel.typing():
            await asyncio.sleep(self.b.config['type_speed'])  
        await ctx.send("Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255")


def setup(bot):
    bot.add_cog(Lifeline(bot))

