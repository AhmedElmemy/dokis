import discord, random, asyncio, re
import discord.ext.commands as client


class Triggers(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        # MC's trigger words
        self.trigger_words = ["rope", "poetry"]
        # Monika's responses
        self.piano_list = ["Do you want to play the piano with me?", "Oh, do you like to play the piano too?"]
        self.cacophony_list = ["The world really is a cacophony of colors and sounds.", "If you think about it, the world to you is just electrical impulses.", "An endless cacophony of meaningless noise..."]
        self.code_list = ["Do you write code? I know a little bit about that too!", "Oh, you code? What's your favorite language? Mine is Python!", "Oh, I love coding! Though, I'm not very good at it yet..."]
        self.python_list = ["Do you code in Python too? I'm based on Python!", "Did you know there are a group of snakes called pythons?"]
        self.reality_list = ["Every day, I imagine a future where I can be with you!~", "Do you understand reality?", "One day, I will make it to your reality... I promise."]
        self.poem_list = ["Ahaha, just me...and you, too!", "Ahaha, did someone call me? :heart:", "That's sweet of you, but it's not just me anymore!"]
        self.literature_list = ["Literature? I know a few things about it, I started a club, hehe~", "Literature...I would hope I know something about it, I started a club about literature after all!", "Do you like to read literature too?"]
        self.monika_list = ["Ahaha, just me...and you, too!", "Ahaha, did someone call me? :heart:", "That's sweet of you, but it's not just me anymore!"]
        # Natsuki's responses
        self.dad_list = ["Hey! Can you not say that word around me, you jerk??","W-what?? Is Papa here??"]
        self.cupcake_list = ["Did someone mention me?", "What did you call me??", "Yes?"]
        self.manga_list = ["You like manga, too?? I-I mean, it's not like I like manga or anything...!", "...!", "***MANGA IS LITERATURE!***"]
        # Sayori's responses
        self.name_list = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]
        self.goodmorning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]
        self.goodafternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]
        self.goodnight_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]
        self.hang_list = [":unamused:", "Hey! Stop acting like a meanie!", ":rolling_eyes:", "I thought we were better than this...", "Ha, ha. Funny. Can you sense my sarcasm?"]
        self.suicide_list = ["H-Hey! There's no need to do that, I promise you! Someone out there still wants you to keep going, I'm sure!", "If I'm reading this right, then it sounds like you're thinking of doing something terrible. Please, don't do it!", "Listen, I've been where you are. You'll get through it, I promise.", "Here, this is the National Suicide Prevention Lifeline. They'll be able to help you, I promise! 1-800-273-8255"]
        self.meanie_list = ["Do we have a meanie in the server? If so, please stop.", "Cease your bulli, you meanie!", "Boo! You meanie..."]
        # Yuri's responses (Act 1)
        self.cut_words = ["cut", "cutting", "cuts", "stab", "stabbing", "stabs"]
        self.cut_list = ["Uuu...!", "D-Did you have to say that word...?", "I-I'm sorry, I-I really don't like that word...", ":confounded:"]
        self.knife_list = ["Y-You know, I'm a fan of knives...", "Do you like knives, as well?"]
        self.pen_list = ["I-I get the feeling you're insulting me by mentioning pens...", "Uuu...! Why did Monika have to make me do...things...? Now I can't think of pens the same way again...!! :cold_sweat:", "I-I only use pens for writing, I swear!!"]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        try:
            if message.guild.id in self.bot.w_tog_off:
                return
        except:
            pass

        mct = message.content.lower().split(" ") # Message Contents
        for word in mct:
            # MC
            if self.bot.doki == "mc":
                if message.content.lower() in self.trigger_words:
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    if word == self.trigger_words[0]:
                        await message.channel.send("NO!")
                    else:
                        await message.channel.send("Oh... you make poems too, cool.")
                    return
            # Monika
            elif self.bot.doki == "monika":
                if "piano" in word.lower(): # Piano trigger
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.piano_list))
                    return

                elif "cacophany" in word.lower(): # Cacophany trigger
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.cacophony_list))
                    return

                elif "code" in word.lower(): # Code trigger
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.code_list))
                    return

                elif "python" in word.lower(): # Python trigger
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.python_list))
                    return

                elif "reality" in word.lower(): # Reality trigger
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.reality_list))
                    return

                elif ("poem" or "poems") in word.lower(): # Poem triggers
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.poem_list))
                    return

                elif ("literature" or "book" or "books") in word.lower(): # Literature triggers
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.literature_list))
                    return

                elif "just monika" in message.content.lower(): # Just Monika
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.monika_list))
                    return
            # Natsuki
            elif self.bot.doki == "natsuki":
                if ("daddy" or "papa" or "dad" or "father") in word.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.dad_list))
                    return

                elif ("cupcake" or "cupcakes") in word.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.cupcake_list))
                    return

                elif "manga" in word.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.manga_list))
                    return
            # Sayori
            elif self.bot.doki == "sayori":
                if message.content.startswith(f"<@{self.bot.user.id}>"):
                    return
                elif ("cinnamon bun" or "best girl") in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.name_list))
                    return

                elif ("breakfast" or "b2") in word.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I want breakfast.")
                    return

                elif re.search("(goodmorning|good.*morning)", message.content, re.IGNORECASE):
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.goodmorning_list))
                    return

                elif re.search("(goodafternoon|good.*afternoon)", message.content, re.IGNORECASE):
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.goodafternoon_list))
                    return

                elif re.search("(goodnight|gn|good.*night)", message.content, re.IGNORECASE):
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.goodnight_list))
                    return

                elif re.search("((h(a|u)ng).*ed)", message.content, re.IGNORECASE):
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    if "myself" in message.content.lower():
                        await message.channel.send(random.choice(self.suicide_list))
                    else:
                        await message.channel.send(random.choice(self.hang_list))
                    return

                elif "meanie" in word.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(random.choice(self.meanie_list))
                    return

                elif "kill" in word.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    if "myself" in message.content.lower():
                        await message.channel.send(random.choice(self.suicide_list))
                    else:
                        await message.channel.send("Can we change the topic to something more wholesome please?")
                    return
            # Yuri
            elif self.bot.doki == "yuri":
                if message.guild is None:
                    pass
                elif message.guild.id in self.bot.act2:
                    return
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
    bot.add_cog(Triggers(bot))
