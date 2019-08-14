import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Triggers(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.trigger_words = ["rope", "poetry"]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        try:
            if message.guild.id in conf.w_tog_off:
                return
        except:
            pass

        mct = message.content.lower().split(" ") # Message Contents
        for word in mct:
            if message.content.lower() in self.trigger_words:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                if word == self.trigger_words[0]:
                    await message.channel.send("NO!")
                else:
                    await message.channel.send("Oh... you make poems too, cool.")
                return


def setup(bot):
    bot.add_cog(Triggers(bot))
