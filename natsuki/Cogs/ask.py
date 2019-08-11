import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Ask(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def ask(self,ctx, arg1=None):
        if arg1 is None:
            await ctx.send("Hey! You wanted to ask me something so what is it?!")
        else:
            answer_list = ["Eh. Probably not.","I guess so.","How should I know, dummy?", "I don't know. Ask Monika if you want the answer that badly.", "No.","Pfft. In your dreams!", "Is manga literature?", "Yuri might know."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await ctx.send(random.choice(answer_list))


def setup(bot):
    bot.add_cog(Ask(bot))
