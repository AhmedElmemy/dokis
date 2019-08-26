import discord, random, asyncio, re
import discord.ext.commands as client


class Triggers(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.name_list = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]
        self.goodmorning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]
        self.goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]
        self.goodnight_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]
        self.hang_list = [":unamused:", "Hey! Stop acting like a meanie!", ":rolling_eyes:", "I thought we were better than this...", "Ha, ha. Funny. Can you sense my sarcasm?"]
        self.suicide_list = ["H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!", "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!", "Listen, I've been where you are. You'll get through it, I promise.", "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"]
        self.meanie_list = ["Do we have a meanie in the server? If so, please stop.", "Cease your bulli, you meanie!", "Boo! You meanie..."]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.guild.id in self.bot.w_tog_off or message.content.startswith(f"<@{self.bot.user.id}>"):
            return

        mct = message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if ("cinnamon bun" or "best girl") in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send(random.choice(self.name_list))
                return

            elif ("breakfast" or "b2") in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("I want breakfast.")
                return

            elif re.search("(goodmorning|good.*morning)", message.content, re.IGNORECASE):
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send(random.choice(self.goodmorning_list))
                return

            elif re.search("(goodafternoon|good.*afternoon)", message.content, re.IGNORECASE):
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send(random.choice(self.goodafternoon_list))
                return

            elif re.search("(goodnight|gn|good.*night)", message.content, re.IGNORECASE):
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send(random.choice(self.goodnight_list))
                return

            elif re.search("((h(a|u)ng).*ed)", message.content, re.IGNORECASE):
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                if "myself" in message.content.lower():
                    await message.channel.send(random.choice(self.suicide_list))
                else:
                    await message.channel.send(random.choice(self.hang_list))
                return

            elif "meanie" in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send(random.choice(self.meanie_list))
                return

            elif "kill" in word.lower():
                async with message.channel.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                if "myself" in message.content.lower():
                    await message.channel.send(random.choice(self.suicide_list))
                else:
                    await message.channel.send("Can we change the topic to something more wholesome please?")
                return


def setup(bot):
    bot.add_cog(Triggers(bot))