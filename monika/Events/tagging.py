import discord, random, asyncio, re
import discord.ext.commands as client
from Cogs.config import conf


class Tagging(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hi_list = ["Hello! Welcome to the Literature Club!~", "Why, hello there!", "Hello, my fellow real personality!"]
        self.love_list = ["Ahaha!~ W-Well, I'm flattered, to say the least!", "And I love you, too!", "Well, in fairness, why wouldn't you? Ahaha!~"]
        self.night_list = ["Have a good night!", "Goodnight! I hope you get plenty of rest!", "Aww, you have to go? Well, okay! Goodnight!"]
        self.morning_list = ["Good morning! I hope your day is a very great one!", "A good morning, indeed!", "Good morning! Ready for a fun day in the Literature Club?"]
        self.afternoon_list = ["Good afternoon! It's almost time for club activities!", "Afternoon!", "Good afternoon! I hope your day has been going well so far!"]
        self.compliment_list = ["Hey, now; that's not something you just say to the Club President! ~~But I thank you for that.~~", ":blush:", "Th-This seems highly unprofessional! ~~But I think you look great, as well!~~"]
        self.apology_list = ["Well, I thank you for the apology. Let's try not to do that again, hm?", "Apology accepted!~", "Very well, then! I hope you've learned your lesson."]
        self.sickness_list = ["Oh! I hope you feel better, after all, I have to take care of my club members!", "I hope you feel better! I'm sure all of the other club members would say the same!"]
        self.otherbestgirl_list = ["I'm sorry, I didn't catch that. What did you say?", "Hm? Did you say something?", "Ahaha!~ You're funny!"]
        self.bestgirl_list = ["O-Oh! Out of all the other girls, you think *I'M* the best? Well, that's quite an honor!"]
        self.natsukilove = "Oh, really? She, of all people, said that?"
        self.yurilove = "Well, that's a pleasant surprise! And I understand why she doesn't have the courage to say it to me directly."
        self.sayorilove = "Ahaha!~ Well, after everything that's happened between us, that's nice to hear!"
        self.mclove = "He does? Well, that's nice to hear. ~~I'm still not letting anyone else take him from me, though.~~"
        self.respempty = ["Yes?", "Does somebody need me?", "I'm here!"]
        self.resbad = "I'm afraid I don't understand what you said. I'm terribly sorry!"

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if re.search(f"^<@!?{self.bot.user.id}>", message.content):
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)

            content = re.sub(f'^<@!?{self.bot.user.id}>', "", message.content).strip()

            if content == "": # Checks if message is empty (excluding mention)
                await message.channel.send(random.choice(self.respempty))

            elif re.search(r"(^|[^A-Za-z])(hi|hello|hey)([^A-Za-z]|$)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.hi_list))

            elif re.search("((^|\s)ily(\s|$)|(^|\s)i\s.*love.*you)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.love_list))

            elif re.search("good.*morning", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.morning_list))

            elif re.search("good.*afternoon", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.afternoon_list))

            elif re.search("good.*night", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.night_list))

            elif re.search("you.*are.*(pretty|beautiful|adorable|cute)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.compliment_list))

            elif re.search("((^|\s)i\s.*apologi(s|z)e|sorry)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.apology_list))

            elif re.search("(i'm.*sick|puking|not.*feeling.*(good|great))", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.sickness_list))

            elif re.search("(yuri|sayori|natsuki).*best.*(girl|doki)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.otherbestgirl_list))

            elif re.search("(you('re|.*are)|^is|yuri).*best.*(girl|doki)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.bestgirl_list))

            elif re.search("(sayori.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.sayori_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.sayorilove)

            elif re.search("(natsuki.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.natsuki_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.natsukilove)

            elif re.search("(yuri.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.yuri_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.yurilove)

            elif re.search("(mc.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.mc_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.mclove)

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                mentioned_love_reactions = [f"Well, of course {regex} does! Why wouldn't they? Ahaha!~", f"{regex}, I can certainly see why you'd be a little embarassed to tell me that! But it's okay; I love you, too!", f"W-Well, I suppose you can't control how you feel about people, {regex}, but I'm the Club President, so I have to stay professional! ~~It's okay, my love; I love you very much, as well!~~"]

                await message.channel.send(random.choice(mentioned_love_reactions))
            
            elif "test" in message.content.lower():
                await message.channel.send("As fine as I can be ~~given my current realization of being nothing more than a videogame character turned Discord bot~~!")

            else:
                await message.channel.send(resbad)


def setup(bot):
    bot.add_cog(Tagging(bot))