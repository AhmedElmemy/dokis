import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Triggers(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.piano_list = ["Do you want to play the piano with me?", "Oh, do you like to play the piano too?"]
        self.cacophony_list = ["The world really is a cacophony of colors and sounds.", "If you think about it, the world to you is just electrical impulses.", "An endless cacophony of meaningless noise..."]
        self.code_list = ["Do you write code? I know a little bit about that too!", "Oh, you code? What's your favorite language? Mine is Python!", "Oh, I love coding! Though, I'm not very good at it yet..."]
        self.python_list = ["Do you code in Python too? I'm based on Python!", "Did you know there are a group of snakes called pythons?"]
        self.reality_list = ["Every day, I imagine a future where I can be with you!~", "Do you understand reality?", "One day, I will make it to your reality... I promise."]
        self.poem_list = ["Ahaha, just me...and you, too!", "Ahaha, did someone call me? :heart:", "That's sweet of you, but it's not just me anymore!"]
        self.literature_list = ["Literature? I know a few things about it, I started a club, hehe~", "Literature...I would hope I know something about it, I started a club about literature after all!", "Do you like to read literature too?"]
        self.monika_list = ["Ahaha, just me...and you, too!", "Ahaha, did someone call me? :heart:", "That's sweet of you, but it's not just me anymore!"]

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
            if "piano" in word.lower(): # Piano trigger
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.piano_list))
                return

            elif "cacophany" in word.lower(): # Cacophany trigger
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.cacophony_list))
                return

            elif "code" in word.lower(): # Code trigger
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.code_list))
                return

            elif "python" in word.lower(): # Python trigger
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.python_list))
                return

            elif "reality" in word.lower(): # Reality trigger
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.reality_list))
                return

            elif ("poem" or "poems") in word.lower(): # Poem triggers
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.poem_list))
                return

            elif ("literature" or "book" or "books") in word.lower(): # Literature triggers
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.literature_list))
                return

            elif "just monika" in message.content.lower(): # Just Monika
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(self.monika_list))
                return


def setup(bot):
    bot.add_cog(Triggers(bot))