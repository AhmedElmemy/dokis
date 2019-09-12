import discord, random, asyncio, re
import discord.ext.commands as client


class Tagging(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        # MC's responses
        if self.bot.doki == "mc":
            hi_list = ["Hi, I guess.", "Hello..."]
            afternoon_list = ["Is it a good afternoon?", "What? It's the afternoon?", "Ehhhhhh..."]
            otherbestgirl = "I’ll have to agree with you there."
            otherbestgirl_regex = "(yuri|sayori|natsuki|monika)"
            bestgirl = "Who? Me? How?"
            natsukilove = "She does? That's a surprise."
            yurilove = "Does she? It's hard to tell when she's so quiet."
            sayorilove = "Of course she does. She loves everyone."
            monikalove = "She doesn't just love me. She's a bit of a yandere."
            resbad = "Eh?"
            resempty = "Hm? What is it?"
            testmessage = "Yes, I'm fine."

        # Monika's responses
        elif self.bot.doki == "monika":
            hi_list = ["Hello! Welcome to the Literature Club!~", "Why, hello there!", "Hello, my fellow real personality!"]
            love_list = ["Ahaha!~ W-Well, I'm flattered, to say the least!", "And I love you, too!", "Well, in fairness, why wouldn't you? Ahaha!~"]
            night_list = ["Have a good night!", "Goodnight! I hope you get plenty of rest!", "Aww, you have to go? Well, okay! Goodnight!"]
            morning_list = ["Good morning! I hope your day is a very great one!", "A good morning, indeed!", "Good morning! Ready for a fun day in the Literature Club?"]
            afternoon_list = ["Good afternoon! It's almost time for club activities!", "Afternoon!", "Good afternoon! I hope your day has been going well so far!"]
            compliment_list = ["Hey, now; that's not something you just say to the Club President! ~~But I thank you for that.~~", ":blush:", "Th-This seems highly unprofessional! ~~But I think you look great, as well!~~"]
            apology_list = ["Well, I thank you for the apology. Let's try not to do that again, hm?", "Apology accepted!~", "Very well, then! I hope you've learned your lesson."]
            sickness_list = ["Oh! I hope you feel better, after all, I have to take care of my club members!", "I hope you feel better! I'm sure all of the other club members would say the same!"]
            otherbestgirl_list = ["I'm sorry, I didn't catch that. What did you say?", "Hm? Did you say something?", "Ahaha!~ You're funny!"]
            otherbestgirl_regex = "(yuri|sayori|natsuki)"
            bestgirl = "O-Oh! Out of all the other girls, you think *I'M* the best? Well, that's quite an honor!"
            natsukilove = "Oh, really? She, of all people, said that?"
            yurilove = "Well, that's a pleasant surprise! And I understand why she doesn't have the courage to say it to me directly."
            sayorilove = "Ahaha!~ Well, after everything that's happened between us, that's nice to hear!"
            mclove = "He does? Well, that's nice to hear. ~~I'm still not letting anyone else take him from me, though.~~"
            mentioned_love_reactions = ["Well, of course %s does! Why wouldn't they? Ahaha!~", "%s, I can certainly see why you'd be a little embarrassed to tell me that! But it's okay; I love you, too!", "W-Well, I suppose you can't control how you feel about people, %s, but I'm the Club President, so I have to stay professional! ~~It's okay, my love; I love you very much, as well!~~"]
            respempty = ["Yes?", "Does somebody need me?", "I'm here!"]
            resbad = "I'm afraid I don't understand what you said. I'm terribly sorry!"
            testmessage = "As fine as I can be ~~given my current realization of being nothing more than a videogame character turned Discord bot~~!"

        # Natsuki's responses
        elif self.bot.doki == "natsuki":
            hi_list = ["Hi, I guess...", "What, do I have to greet you back or something?", "Hey there, dummy!"]
            love_list = ["...I love you, too, okay??", "W-what?? Don't expect me to say that I love you back or anything, you d-dummy!", "*urk!* :flushed:", "Shut up! You don't mean that!"]
            night_list = ["Goodnight, Dummy!", "Goodnight, then.", "You better get good rest or I'll punch you!", "Sleep well, baka!"]
            morning_list = ["Well, it's *A* morning, I guess...", "Good morning to everyone except my dad.", "Did you get a good night's sleep? Er, not that I really care!!"]
            afternoon_list = ["Good afternoon, I guess.", "Afternoon.", "Yeah, so it's the afternoon. What's your point?"]
            compliment_list = ["***I'M NOT CUTE!!!***", "Hey! I'm not cute!", "Sh-shut up! I'm not cute!!", "Have you ever considered that maybe I want to be something other than cute?!"]
            apology_list = ["Hmph. I'll forgive you, but it's not like you deserve it!", "Fine. I guess I'll let it go...", "You better be sorry, you baka!"]
            sickness_list = ["Ok... well you'd better get better soon... not that I care or anything..", "Ok dummy! Get rest!"]
            otherbestgirl = "Pfft! As if!"
            otherbestgirl_regex = "(yuri|sayori|monika)"
            bestgirl = "Ha! Of course I am!"
            monikalove = "Act 2 says otherwise."
            yurilove = "W-Well it's not like I love her back or anything!!"
            sayorilove = "S-shut up! No she doesn't!"
            mclove = "Ha! I'm sure he does! I-I'll believe it when he tells me that himself!"
            mentioned_love_reactions = ["W-well, it's not like I love %s back or anything!", "Shut up! %s doesn't love me!", "%s loves me? Yeah, I'll believe that when they tell me that, themselves!"]
            respempty = "Yes?"
            resbad = "Uh... What?"
            testmessage = "I'm working just fine."

        # Sayori's responses
        elif self.bot.doki == "sayori":
            hi_list = ["Hi!", "Hello!", "Hiiiiii!~", "Hello, human person!"]
            love_list = ["Aww! I love you too!", "Thank you so much!~", "I love you too! :smile:", ":blush:", "I don't really deserve your love, but I'm flattered, anyway!"]
            night_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]
            morning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]
            afternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]
            compliment_list = ["Awww! Thank you so much! :blush:", "I know you are, but what am I? :stuck_out_tongue_closed_eyes:", "Y-You really think so? Aww!~", "How sweet! Thank you so much!"]
            apology_list = ["It's okay; I forgive you!", "Well, alright. As long as you promise to behave yourself!", "Thank you for apologizing!", "Okay. Just try not to do it again!"]
            sickness_list = ["Don't worry! I'm sure you'll feel better soon!", "Aww... get plenty of rest, and eat a lot of healthy foods!"]
            russian_list = ["I don't speak Russian, but I'm assuming that's a compliment, to which I say thank you!", "Sorry, I only know English, despite being Japanese.", "Hehehe. That sounds funny."]
            otherbestgirl = "Well, I respect your opinion!"
            otherbestgirl_regex = "(yuri|natsuki|monika)"
            bestgirl = "S-Stop it! That's not true!"
            natsukilove = "Awww, she does??"
            yurilove = "Well, of course she does! Yuri loves everybody!"
            monikalove = "Yay! I'm glad she does!"
            mclove = "Yay! My best friend loves me!!! :heart:"
            mentioned_love_reactions = ["Aww! Well, you can tell %s that I love them, too!", "%s does? Well, that's so sweet to hear!", "And I love %s, too! :heart:", "Yay! I'm loved by %s!"]
            respempty = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]
            resbad = ["Huh? I don't understand.", "I don't get it.", "???", "Maybe try something I actually understand?"]
            testmessage = "Testing, testing! 1-2-1-2 testing!"

        # Yuri's responses
        elif self.bot.doki == "yuri":
            if message.guild is None:
                pass
            elif message.guild.id in self.bot.act2:
                return
            hi_list = ["H-Hello there.", "...h-hi...", "O-Oh, are you talking to me? S-Sorry, I'm not used to that..."]
            love_list = ["O-Oh! W-W-Well, uhh... :flushed:", "I-I love you, too... :relaxed:", "R-Really? Why? I-I don't have anything worth loving...", "Uuu, why is my heart beating so fast right now??"]
            night_list = ["G-Goodnight, then.", "Until next time.", "I hope you have wonderful dreams!"]
            morning_list = ["It is a good morning, indeed.", "I hope you slept wonderfully!", "Good morning!"]
            afternoon_list = ["Good afternoon.", "A truly beautiful afternoon, it is.", "Ah, it's times like this where I just want to sit outsite and read a good book."]
            compliment_list = ["Y-You really think so...?", "Uuu... :flushed:", "T-Thank you. I needed to hear that...", ":blush:"]
            apology_list = ["I don't think I fully understand why you're apologizing, but I accept it, anyway.", "It's alright; I forgive you.", "N-No, I'm the one who should be sorry; I mess up everything...", "Consider your apology accepted, then!"]
            sickness_list = ["O-Oh... I hope y-you feel better soon.", "Oh... please do feel better."]
            otherbestgirl = "W-Well, I suppose that's true; she's much better than I am..."
            otherbestgirl_regex = "(sayori|natsuki|monika)"
            bestgirl = "Oh! Uh... Well, I'm glad you think that!"
            natsukilove = "Sh-She does?"
            monikalove = "Ahaha... I-I'm glad that I have a friend like Monika who loves me... :blush:"
            sayorilove = "Haha. Well, she is a loving soul."
            mclove = "Uuuuuuuuuu..."
            mentioned_love_reactions = ["O-Oh, %s does...? W-Well, that's nice to hear.", "Uuu... I-I'm flattered, %s...", "R-Really? %s loves me...?", "W-Well... I-I think I love %s, too...!"]
            resempty = ["Y-Yes...?", "Did you want to talk to me...?", "Hm?"]
            resbad = "I-I'm sorry, but I don't understand what you mean..."
            testmessage = "I-I believe I'm working properly... Oh, I hope I am..."

        if re.search(f"^<@!?{self.bot.user.id}>", message.content):
            content = re.sub(f'^<@!?{self.bot.user.id}>', "", message.content).strip()
            async with message.channel.typing():
                await asyncio.sleep(int(self.bot.config['type_speed']))

            if content == "":
                await message.channel.send(resempty if self.bot.doki == ("mc" or "natsuki") else random.choice(resempty))

            elif re.search(r"(^|[^A-Za-z])(hi|hello|hey)([^A-Za-z]|$)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(hi_list))

            elif re.search("((^|\s)ily(\s|$)|(^|\s)i\s.*love.*you)", message.content, re.IGNORECASE):
                await message.channel.send("..." if self.bot.doki == "mc" else random.choice(love_list))

            elif re.search("good.*morning", message.content, re.IGNORECASE):
                await message.channel.send(":zzz: Huh- morning already?" if self.bot.doki == "mc" else random.choice(morning_list))

            elif re.search("good.*afternoon", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(afternoon_list))

            elif re.search("good.*night", message.content, re.IGNORECASE):
                await message.channel.send("Um... Good night, I guess." if self.bot.doki == "mc" else random.choice(night_list))

            elif re.search("you('re|.*are).*(pretty|beautiful|adorable|cute)", message.content, re.IGNORECASE):
                await message.channel.send("No I’m not." if self.bot.doki == "mc" else random.choice(compliment_list))

            elif re.search("((^|\s)i\s.*apologi(s|z)e|sorry)", message.content, re.IGNORECASE):
                await message.channel.send("I-It’s ok." if self.bot.doki == "mc" else random.choice(apology_list))

            elif re.search("(i'm.*sick|puking|not.*feeling.*(good|great))", message.content, re.IGNORECASE):
                await message.channel.send("I’m not one for that stuff, maybe ask Monika." if self.bot.doki == "mc" else random.choice(sickness_list))

            elif re.search(f"{otherbestgirl_regex}.*best.*(girl|doki)", message.content, re.IGNORECASE):
                if self.bot.doki != "monika":
                    await message.channel.send(otherbestgirl)
                else:
                    await message.delete()
                    await message.channel.send(random.choice(otherbestgirl_list))

            elif re.search(f"(you('re|.*are)|^is|{self.bot.doki}).*best.*doki", message.content, re.IGNORECASE):
                await message.channel.send(bestgirl)

            elif (re.search("(sayori.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE)) and self.bot.doki != "sayori":
                await message.channel.send(sayorilove)

            elif (re.search("(natsuki.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE)) and self.bot.doki != "natsuki":
                await message.channel.send(natsukilove)

            elif (re.search("(yuri.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE)) and self.bot.doki != "yuri":
                await message.channel.send(yurilove)

            elif (re.search("(monika.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE)) and self.bot.doki != "monika":
                await message.channel.send(monikalove)

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                await message.channel.send("Um… what?" if self.bot.doki == "mc" else (random.choice(mentioned_love_reactions) % (regex)))

            elif "test" in message.content.lower():
                await message.channel.send(testmessage)

            else:
                await message.channel.send(resbad if self.bot.doki != "sayori" else random.choice(resbad))


def setup(bot):
    bot.add_cog(Tagging(bot))