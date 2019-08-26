import discord, random, asyncio, re
import discord.ext.commands as client


class Tagging(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hi_list = ["Hi!", "Hello!", "Hiiiiii!~", "Hello, human person!"]
        self.love_list = ["Aww! I love you too!", "Thank you so much!~", "I love you too! :smile:", ":blush:", "I don't really deserve your love, but I'm flattered, anyway!"]
        self.night_list = ["Goodnight! Sleep tight! Don't let the bedbugs bite!~", "Nighty night!~", "Sleep well!", "Goodnight!"]
        self.morning_list = ["Good morning! I hope you slept well!~", "Morning, everyone!", "Goooooooood morning!~", "Morning, Sunshine!~"]
        self.afternoon_list = ["Good afternoon!", "Afternoon?? Shoot! I'm late for school again!", "Good afternoon, indeed!", "Afternoon!"]
        self.compliment_list = ["Awww! Thank you so much! :blush:", "I know you are, but what am I? :stuck_out_tongue_closed_eyes:", "Y-You really think so? Aww!~", "How sweet! Thank you so much!"]
        self.apology_list = ["It's okay; I forgive you!", "Well, alright. As long as you promise to behave yourself!", "Thank you for apologizing!", "Okay. Just try not to do it again!"]
        self.sickness_list = ["Don't worry! I'm sure you'll feel better soon!", "Aww... get plenty of rest, and eat a lot of healthy foods!"]
        self.russian_list = ["I don't speak Russian, but I'm assuming that's a compliment, to which I say thank you!", "Sorry, I only know English, despite being Japanese.", "Hehehe. That sounds funny."]
        self.otherbestgirl = "Well, I respect your opinion!"
        self.bestgirl = "S-Stop it! That's not true!"
        self.natsukilove = "Awww, she does??"
        self.yurilove = "Well, of course she does! Yuri loves everybody!"
        self.monikalove = "Yay! I'm glad she does!"
        self.mclove = "Yay! My best friend loves me!!! :heart:"
        self.respempty = ["Did someone mention me?", "You rang?", "Are you guys talking about me?"]
        self.resbad = ["Huh? I don't understand.", "I don't get it.", "???", "Maybe try something I actually understand?"]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if re.search(f"^<@!?{self.bot.user.id}>", message.content):
            async with message.channel.typing():
                await asyncio.sleep(self.bot.config['type_speed'])

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

            elif re.search("(yuri.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.yuri_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.yurilove)

            elif re.search("(mc.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.mc_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.mclove)

            elif re.search("cyka.*blyat", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.russian_list))

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                love_tag_reactions = [f"Aww! Well, you can tell {regex} that I love them, too!", f"{regex} does? Well, that's so sweet to hear!", f"And I love {regex}, too! :heart:", f"Yay! I'm loved by {regex}!"]

                await message.channel.send(random.choice(love_tag_reactions))

            elif "test" in message.content.lower():
                await message.channel.send("I'm working just fine.")

            elif re.search("(monika.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.monika_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE): 
                await message.channel.send("Monika isn't a meanie! And no, I don't feel obligated to say that for fear of her deleting me again...")

            elif re.search("(natsuki.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.natsuki_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE): 
                await message.channel.send("Hey, she may be spunky, but she's not a meanie!")

            elif re.search("(yuri.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.yuri_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE): 
                await message.channel.send("What?? Yuri is the last person who would ever be a meanie!")

            elif re.search("(sayori.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.sayori_id}>.*(are|is being|is).*a.*meanie)", message.content, re.IGNORECASE):
                await message.channel.send("Eh?? No, I'm not!!")

            elif re.search(r".+\s.*(are|is).*meanie", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s(are|is).*meanie", content).group(1)
                meanie_list = [f"Hey! Stop being a meanie, {regex}!", f"We don't like meanies on this server, {regex}!", f"Are you being a meanie, {regex}? If so, please stop."]

                await message.channel.send(random.choice(meanie_list))

            elif "test" in message.content.lower():
                await message.channel.send("Testing, testing! 1-2-1-2 testing!")
            else:
                await message.channel.send(random.choice(self.resbad))


def setup(bot):
    bot.add_cog(Tagging(bot))