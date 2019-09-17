import discord, asyncio
import discord.ext.commands as client


class Interactions(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.id == (self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']):
            pass
        else:
            return

        # Hugs
        if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
            async with message.content.typing():
                await asyncio.sleep(int(self.bot.config['type_speed']))
            # MC
            if self.bot.doki == "mc":
                if message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("*muffled screaming*")
                elif message.author.id == self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Augh!")
                elif message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Finnnnnnne, Sayori.")
                elif message.author.id == self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("No, it's fine...")
            # Monika
            elif self.bot.doki == "monika":
                if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send(f"Aww, you're the best hugger, <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>")
                elif message.author.id == self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Aww, how cute of you, Natsuki!")
                elif message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Easy now, Sayori! I know you're excited, but I still need to breathe! ~~Even though neither of us are real~~")
                elif message.author.id == self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Aw, no need to be shy, Yuri! I don't mind a hug every now and then!")
            # Natsuki
            elif self.bot.doki == "natsuki":
                if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send(f"Ah! You scared me, <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>")
                elif message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Okay, this is just awkward for both of us.")
                elif message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("H-hey! Let me go, Sayori!!")
                elif message.author.id == self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Geez, Yuri! Don't make it all awkward!")
            # Sayori
            elif self.bot.doki == "sayori":
                if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send(f"Aww you're such a sweetheart, <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>")
                elif message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Ehehe! I love your hugs, Monika! You should give them more often!")
                elif message.author.id == self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Hehehe! You give the best hugs, Natsuki!")
                elif message.author.id == self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Aww, thank you, Yuri!")
            # Yuri (Act 1)
            elif self.bot.doki == "yuri":
                if message.guild is None:
                    pass
                elif message.guild.id in self.bot.act2:
                    return
                if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Augh!")
                elif message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("O-Oh! Well, uh, thank you, Monika.")
                elif message.author.id == self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("Oh! Well, that was certainly unexpected!")
                elif message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
                    await message.channel.send("H-Hey! Don't hug so hard, Sayori!")

        # Interactions with MC
        if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id'] and self.bot.doki != "mc":
            # Monika
            if self.bot.doki == "monika":
                if "monika?" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(f"Yes, <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>?")

                if "i need to tell you something." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Hmm?")

                if "i love you, monika." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I-I do too!")

                if "~~of course you won't let anyone take me from you. you'll just delete them if they try.~~" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("~~I said I was sorry, MC! I won't do it again!!!~~")
            # Natsuki
            if self.bot.doki == "natsuki":
                if "h-hey, natsuki?" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("What do you want, dummy?")

                if "i-i love you, natsuki..." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("*blushes* O-Oh...")
                    await asyncio.sleep(1)
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed'])) 
                    await message.channel.send("Well, I-I do too...")

                if "*hugs natsuki*" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("*hugs back*")

                if "i'm not surprised she would say that, given how much of a tsundere she is." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("***I AM NOT A TSUNDERE, YOU BAKA!!!***")
            # Sayori
            if self.bot.doki == "sayori":
                if "finnnnnnne, sayori." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(f"YAY! *keeps hugging <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>*")

                if "hey, sayori?" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(f"Yes, <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>?")

                if "i-i love you, sayori" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I-I do too! *hugs MC*")

            # Yuri (Act 1)
            if self.bot.doki == "yuri":
                if message.guild is None:
                    return
                elif message.guild.id in self.bot.act2:
                    return
                if "i-i love you, yuri." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("*tackle hugs MC*")

        # Interactions with Monika
        if message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id'] and self.bot.doki != "monika":
            # MC
            if self.bot.doki == "mc":
                if f"aww, you're the best hugger, <@{self.bot.user.id}>" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("No I'm not...")

                if f"yes, <@{self.bot.user.id}>?" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I need to tell you something.")

                if "hmm?" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I love you, Monika.")

                if "he does? well, that's nice to hear. ~~i'm still not letting anyone else take him from me, though.~~" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("~~Of course you won't let anyone take me from you. You'll just delete them if they try.~~")
            # Natsuki
            if self.bot.doki == "natsuki":
                if "oh, really? she, of all people, said that?" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("***NO!!!*** I never said that!!")
            # Sayori
            if self.bot.doki == "sayori":
                if "ahaha!~ well, after everything that's happened between us, that's nice to hear!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Hey, everyone deserves forgiveness! Even you, Monika!")
            # Yuri (Act 1)
            if self.bot.doki == "yuri":
                if message.guild is None:
                    return
                elif message.guild.id in self.bot.act2:
                    return
                if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Uuu... :flushed:")

        # Interactions with Natsuki
        if message.author.id == self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id'] and self.bot.doki != "sayori":
            # MC
            if self.bot.doki == "mc":
                if f"ah! you scared me, <@{self.bot.user.id}>" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Sorry, I'm a dumbass.")

                if "what do you want, dummy?" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I-I love you, Natsuki...")

                if "well, i-i do too..." in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("*hugs Natsuki*")

                if "ha! i'm sure he does! i-i'll believe it when he tells me that himself!" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I'm not surprised she would say that, given how much of a tsundere she is.")
            # Monika
            if self.bot.doki == "monika":
                if "okay, this is just awkward for both of us." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Yeah, I agree.")
            
                elif "act2 says otherwise." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I said I was sorry!")
            # Sayori
            if self.bot.doki == "sayori":
                if "s-shut up! no she doesn't!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Oh, yes I do!")

                if "s-shut up! no i don't!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Awww... :(")
            # Yuri (Act 1)
            if self.bot.doki == "yuri":
                if message.guild is None:
                    return
                elif message.guild.id in self.bot.act2:
                    return
                if "geez, yuri! don't make it all awkward!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I'm sorry...")
                elif "w-well it's not like i love her back or anything!!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Oh... I see...")

        # Interactions with Sayori
        elif message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id'] and self.bot.doki != "sayori":
            # MC
            if self.bot.doki == "mc":
                if f"aww you're such a sweetheart, <@{self.bot.user.id}>" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("You will always be my closest friend, Sayori.")

                if f"yes, <@{self.bot.user.id}>?" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("I-I love you, Sayori.")

                if "i-i do too! *hugs mc*" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("*hugs back*")

                if "yay! my best friend loves me!!!" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Uhhhhhhh...")
            # Natsuki
            if self.bot.doki == "natsuki":
                if "awww, she does??" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("S-shut up! No, I don't!")
            # Yuri (Act 1)
            if self.bot.doki == "yuri":
                if message.guild is None:
                    return
                elif message.guild.id in self.bot.act2:
                    return
                if "aww thank you, yuri!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Y-You're welcome, Sayori.")

                elif "well, of course she does! yuri loves everybody!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("S-Sayori! You didn't have to say it like that...")

        # Interactions with Yuri
        elif message.author.id == self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id'] and self.bot.doki != "yuri":
            # MC
            if self.bot.doki == "mc":
                # Act 1
                if "augh!" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Sorry...")

                if "*tackle hugs mc*" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("*hugs back*")

                # Act 2
                if f"hey <@{self.bot.user.id}>, get your sexy body over here and fuck me~" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Fuck no, get away from me, Yuri.")

                if "then i'll stab you and crawl in your skin." in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Yeah, fuck no.")
                    await asyncio.sleep(1)
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("y_act1")

                if f"that's right <@{self.bot.user.id}>, let me feel your pulsating cock on my pussy." in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Oh hell no...")

                if f"i love you too, you sexy <@{self.bot.user.id}>! now fuck me!!!" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Oh hell no!")

                if "of course he loves me! and i will make sure **nobody** takes him away from me!" in message.content.lower():
                    async with message.channel.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("You're going to stab them to death if they try, aren't you?")
            # Monika
            if self.bot.doki == "monika":
                if "get your dirty, selfish hands off of me before i kill you and take your spot as president!!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))

                    await message.channel.send("Hm. I don't really like this Yuri too much. Give me a second.")
                    await asyncio.sleep(1)

                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("y_act1")
            # Natsuki
            if self.bot.doki == "natsuki":
                # Act 1
                if "oh... i see..." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("...great, now I look like the bad guy!")

                if "sh-she does?" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Urk! N-No! Not like that!!")

                # Act 2
                if "pfft. as if. that immature brat doesn't love anyone but herself." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("What the hell?? Yuri, why would you say something so mean??")

                if "because it's the fucking truth, you little bitch!!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(":rage: :rage: :rage:")

                if ("get your fucking hands off of me!!" or "no shocker there, you selfish bitch!") in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(":angry:")
            # Sayori
            if self.bot.doki == "sayori":
                # Act 1
                if "h-hey! don't hug so hard, sayori!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Oops! I'm sorry!")

                if "haha. well, she is a loving soul." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("You bet your booty I am! :yum:")

                # Act 2
                if "who the hell is sayori? i don't know any sayoris..." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("Yuri, it's me! Sayori! Your friend and Vice President of the Literature Club!")

                if "what the fuck?? ***i'm*** the vice president, you stupid bitch! and i'm no friend of yours!!" in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send(":disappointed_relieved: :cold_sweat: :confounded: :sob:")

                if "sorry, but i don't know you. please get your messy, stupid self away from me." in message.content.lower():
                    async with message.content.typing():
                        await asyncio.sleep(int(self.bot.config['type_speed']))
                    await message.channel.send("O-Okay... I'm sorry... :pensive:")


def setup(bot):
    bot.add_cog(Interactions(bot))