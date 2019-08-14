import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Triggers(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.dad_list = ["Hey! Can you not say that word around me, you jerk??","W-what?? Is Papa here??"]
        self.cupcake_list = ["Did someone mention me?", "What did you call me??", "Yes?"]
        self.manga_list = ["You like manga, too?? I-I mean, it's not like I like manga or anything...!", "...!", "***MANGA IS LITERATURE!***"]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        try:
            if message.guild.id in conf.w_tog_off:
                return
        except:
            pass

        mct = message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if ("daddy" or "papa" or "dad" or "father") in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.dad_list))
                return

            elif ("cupcake" or "cupcakes") in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.cupcake_list))
                return

            elif "manga" in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.manga_list))
                return


def setup(bot):
    bot.add_cog(Triggers(bot))