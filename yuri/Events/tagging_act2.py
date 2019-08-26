import discord, random, asyncio, re
import discord.ext.commands as client


class TaggingActTwo(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hi_list = ["Hello there.", "Hello, my beloved! Nice to see you!"]
        self.love_list = ["I love you, too! I love you so much that I touch myself to you every night!", "I'm glad, because if you didn't, I'd be very, *very* upset...", ":smirk:", "...Ahahaha. Ahahahahahaha! Ahahahahahahahaha! AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"]
        self.night_list = ["Haha. No. You're not allowed to go.", "Goodnight! I'll be sure to watch over you very closely while you're resting...", "I hope you don't mind if I look at your chest move up and down while the beautiful, soft breathing noises come from your mouth. Ahaha..."]
        self.morning_list = ["Good morning, my love!", "Oh, good! You're finally awake!", "Did you know you snore very loudly? Ahaha...", "Good morning! I can't wait to spend the day together! Just you and me, nobody else..."]
        self.afternoon_list = ["Good afternoon! But who cares what time it is; we'll be together forever, right??", "A perfect afternoon for just staring at each other, telling what kind of dirty things we could do together..."]
        self.compliment_list = ["Ohoho, stop it, you! I'm nothing compared to you!", "But you're 10 times as amazing!", "no u", "Oh? Am I attractive enough for you to pleasure youself to the thought of me? Because I do it to the thought of you all the time!", "Oh, I love it when you tell me that!"]
        self.apology_list = ["Ahaha. There's no need to be sorry. I honestly found it kinda hot...", "Well, if it'll make you feel better, I accept your apology.", "Uhuhu. You look so cute when you apologize like that!"]
        self.sickness = "Feel better soon my love so we can love each other forever!"
        self.otherbestgirl = "No, she's fucking not."
        self.bestgirl = "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
        self.natsukilove = "Pfft. As if. That immature brat doesn't love anyone but herself."
        self.monikalove = "I'll believe that when that bitch says it to my face!"
        self.sayorilove = "Who the hell is Sayori? I don't know any Sayoris..."
        self.mclove =  "Of course he loves me! And I will make sure **NOBODY** takes him away from me!"
        self.resempty = ["Yes, my love?", "Oh, did someone call for me?"]
        self.resbad= "I love you, but I have no clue what you just said."

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.guild is None:
            return
        if message.guild.id not in self.bot.act2:
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
                await message.channel.send(self.sickness)

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

                await message.channel.send(random.choice(mentioned_love_reactions))

            elif "test" in message.content.lower():
                await message.channel.send("I-I believe I'm working properly... Oh, I hope I am...")
            
            else:
                await message.channel.send(self.resbad)  


def setup(bot):
    bot.add_cog(TaggingActTwo(bot))