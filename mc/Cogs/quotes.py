import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Quotes(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self.quote_list = ["I want breakfast.", "AAAAAaaaaAAAAAAAAHH!!!!", "get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head", "I made eggs and toast!", "It's bad to skip breakfast! I get all cranky...", "I was playing with the crayons and smacked my forehead into the shelf!", "Yuri's boobs are just as they've always been! Big and beautiful!", "I did something bad, and now I have to accept the revolution!", "This isn't the napping club!", "I'm fine with--looking like a unicorn--", "So, if I keep it unbuttoned then I won't get a boyfriend, right?"]

    @client.command()
    async def quote(self,ctx):
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)
        await ctx.send(random.choice(self.quote_list))


def setup(bot):
    bot.add_cog(Quotes(bot))
