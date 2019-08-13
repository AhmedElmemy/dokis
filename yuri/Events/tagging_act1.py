import discord, random, asyncio, re
import discord.ext.commands as client
from Cogs.config import conf


class TaggingActOne(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hi_list = ["H-Hello there.", "...h-hi...", "O-Oh, are you talking to me? S-Sorry, I'm not used to that..."]
        self.love_list = ["O-Oh! W-W-Well, uhh... :flushed:", "I-I love you, too... :relaxed:", "R-Really? Why? I-I don't have anything worth loving...", "Uuu, why is my heart beating so fast right now??"]
        self.night_list = ["G-Goodnight, then.", "Until next time.", "I hope you have wonderful dreams!"]
        self.morning_list = ["It is a good morning, indeed.", "I hope you slept wonderfully!", "Good morning!"]
        self.afternoon_list = ["Good afternoon.", "A truly beautiful afternoon, it is.", "Ah, it's times like this where I just want to sit outsite and read a good book."]
        self.compliment_list = ["Y-You really think so...?", "Uuu... :flushed:", "T-Thank you. I needed to hear that...", ":blush:"]
        self.apology_list = ["I don't think I fully understand why you're apologizing, but I accept it, anyway.", "It's alright; I forgive you.", "N-No, I'm the one who should be sorry; I mess up everything...", "Consider your apology accepted, then!"]
        self.sickness_list = ["O-Oh... I hope y-you feel better soon.", "Oh... please do feel better."]
        self.otherbestgirl = "W-Well, I suppose that's true; she's much better than I am..."
        self.bestgirl = "Oh! Uh... Well, I'm glad you think that!"
        self.natsukilove = "Sh-She does?"
        self.monikalove = "Ahaha... I-I'm glad that I have a friend like Monika who loves me... :blush:"
        self.sayorilove = "Haha. Well, she is a loving soul."
        self.mclove = "Uuuuuuuuuu..."
        self.resempty = ["Y-Yes...?", "Did you want to talk to me...?", "Hm?"]
        self.resbad= "I-I'm sorry, but I don't understand what you mean..."

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        try:
            if message.guild.id in conf.act2:
                return
        except:
            pass

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

            elif re.search("you('re|.*are).*are.*cute", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.compliment_list))

            elif re.search("((^|\s)i\s.*apologi(s|z)e|sorry)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.apology_list))

            elif re.search("(i'm.*sick|puking|not.*feeling.*(good|great))", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.sickness_list))

            elif re.search("(yuri|natsuki|monika).*best.*(girl|doki)", message.content, re.IGNORECASE):
                await message.channel.send(self.otherbestgirl)

            elif re.search("(you('re|.*are)|^is|yuri).*best.*(girl|doki)", message.content, re.IGNORECASE):
                await message.channel.send(self.bestgirl)

            elif re.search("(natsuki.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.natsuki_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.natsukilove)

            elif re.search("(monika.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.monika_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.monikalove)

            elif re.search("(sayori.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.sayori_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.sayorilove)

            elif re.search("(mc.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.mc_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.mclove)

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                mentioned_love_reactions = [f"Ohoho, well I think it's safe to say that {regex} doesn't love me as much as you do.", f"{regex} does, do they? Well, I beg to differ.", "I'm sorry, {regex}, but I already have a lover, and they belong to me and me alone.", "Well, I suppose I could touch myself to {regex}, as well..."]

                await message.channel.send(random.choice(act1_mentioned_love_reactions))

            elif "test" in message.content.lower():
                await message.channel.send("I-I believe I'm working properly... Oh, I hope I am...")
            
            else:
                await message.channel.send(resbad)  


def setup(bot):
    bot.add_cog(TaggingActOne(bot))