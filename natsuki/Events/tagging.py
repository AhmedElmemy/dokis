import discord, random, asyncio, re
import discord.ext.commands as client


class Tagging(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hi_list = ["Hi, I guess...", "What, do I have to greet you back or something?", "Hey there, dummy!"]
        self.love_list = ["...I love you, too, okay??", "W-what?? Don't expect me to say that I love you back or anything, you d-dummy!", "*urk!* :flushed:", "Shut up! You don't mean that!"]
        self.night_list = ["Goodnight, Dummy!", "Goodnight, then.", "You better get good rest or I'll punch you!", "Sleep well, baka!"]
        self.morning_list = ["Well, it's *A* morning, I guess...", "Good morning to everyone except my dad.", "Did you get a good night's sleep? Er, not that I really care!!"]
        self.afternoon_list = ["Good afternoon, I guess.", "Afternoon.", "Yeah, so it's the afternoon. What's your point?"]
        self.compliment_list = ["***I'M NOT CUTE!!!***", "Hey! I'm not cute!", "Sh-shut up! I'm not cute!!", "Have you ever considered that maybe I want to be something other than cute?!"]
        self.apology_list = ["Hmph. I'll forgive you, but it's not like you deserve it!", "Fine. I guess I'll let it go...", "You better be sorry, you baka!"]
        self.sickness_list = ["Ok... well you'd better get better soon... not that I care or anything..", "Ok dummy! Get rest!"]
        self.otherbestgirl = "Pfft! As if!"
        self.bestgirl = "Ha! Of course I am!"
        self.monikalove = "Act 2 says otherwise."
        self.yurilove = "W-Well it's not like I love her back or anything!!"
        self.sayorilove = "S-shut up! No she doesn't!"
        self.mclove = "Ha! I'm sure he does! I-I'll believe it when he tells me that himself!"
        self.respempty = "Yes?"
        self.resbad = "Uh... What?"

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if re.search(f"^<@!?{self.bot.user.id}>", message.content):
            async with message.channel.typing():
                await asyncio.sleep(int(self.bot.config['type_speed']))

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

            elif re.search("(yuri|sayori|monika).*best.*(girl|doki)", message.content, re.IGNORECASE):
                await message.channel.send(self.otherbestgirl)

            elif re.search("(you('re|.*are)|^is|yuri).*best.*(girl|doki)", message.content, re.IGNORECASE):
                await message.channel.send(self.bestgirl)

            elif re.search("(sayori.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.sayorilove)

            elif re.search("(monika.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.monikalove)

            elif re.search("(yuri.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.yurilove)

            elif re.search("(mc.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send(self.mclove)

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                mentioned_love_reactions = [f"W-well, it's not like I love {regex} back or anything!", f"Shut up! {regex} doesn't love me!", f"{regex} loves me? Yeah, I'll believe that when they tell me that, themselves!"]

                await message.channel.send(random.choice(mentioned_love_reactions))

            elif "test" in message.content.lower():
                await message.channel.send("I'm working just fine.")

            else:
                await message.channel.send(self.resbad)

def setup(bot):
    bot.add_cog(Tagging(bot))
