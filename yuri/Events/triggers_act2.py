import discord, random, asyncio, re
import discord.ext.commands as client


class TriggersActTwo(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cut_words = ["cut", "cutting", "cuts", "stab", "stabbing", "stabs"]
        self.cut_list = ["Oooo, yes. Say that again, please.", "Hahaha! I love your twisted sense of humor! It makes me so wet...", "Oh, I love it when you say that word... it makes me want to cut you and lick all the blood off."]
        self.knife_list = ["Ahahaha! Did someone mention knives...?!", "Oh, I love knives! The way the sharp blade slides along skin is just beautiful!", "Oh, just hearing that word makes me feel so... Ahaha..."]
        self.pen_list = ["I still have the pen I stole from MC... I even still use it from time to time...", "Hahaha. Are you expecting me to do something naughty with a pen? Because I just might if you ask nicely...", "Oh... Oh...! OH!!! YES, YES, YESYESYES!!!"]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.guild is None:
            return
        elif message.guild.id not in self.bot.act2 or message.guild.id in self.bot.w_tog_off:
            return

        mct = message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if word.lower() in self.cut_words:
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send(random.choice(self.cut_list))
                return

            elif re.search("(kni(fe|ves))", message.content, re.IGNORECASE):
                async with message.channel.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send(random.choice(self.knife_list))
                return

            elif "pen" or "pens" in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send(random.choice(self.pen_list))
                return


def setup(bot):
    bot.add_cog(TriggersActTwo(bot))