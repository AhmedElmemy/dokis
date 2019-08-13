import discord, random, asyncio, re
import discord.ext.commands as client
from Cogs.config import conf


class TriggersActOne(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cut_words = ["cut", "cutting", "cuts", "stab", "stabbing", "stabs"]
        self.cut_list = ["Uuu...!", "D-Did you have to say that word...?", "I-I'm sorry, I-I really don't like that word...", ":confounded:"]
        self.knife_list = ["Y-You know, I'm a fan of knives...", "Do you like knives, as well?"]
        self.pen_list = ["I-I get the feeling you're insulting me by mentioning pens...", "Uuu...! Why did Monika have to make me do...things...? Now I can't think of pens the same way again...!! :cold_sweat:", "I-I only use pens for writing, I swear!!"]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.guild.id in conf.w_tog_off:
            return

        mct = message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if word.lower() in self.cut_words:
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.cut_list))

            elif re.search("(kni(fe|ves))", message.content, re.IGNORECASE):
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.knife_list))

            elif "pen" or "pens" in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.pen_list))


def setup(bot):
    bot.add_cog(TriggersActOne(bot))