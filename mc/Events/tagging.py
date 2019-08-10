import discord, random, asyncio, re
import discord.ext.commands as client
from Cogs.config import conf


class Tagging(client.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.hello_list = ["Hi, I guess.", "Hello..."]
        self.afternoon_list = ["Is it a good afternoon?", "What? It's the afternoon?", "Ehhhhhh..."]

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if re.search(f"^<@!?{self.bot.user.id}>", message.content):
            content = re.sub(f'^<@!?{self.bot.user.id}>', "", message.content).strip()
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)

            if content == "":
                await message.channel.send("Hm? What is it?")

            elif re.search(r"(^|[^A-Za-z])(hi|hello|hey)([^A-Za-z]|$)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.hello_list))

            elif re.search("((^|\s)ily(\s|$)|(^|\s)i\s.*love.*you)", message.content, re.IGNORECASE):
                await message.channel.send("...")

            elif re.search("good.*morning", message.content, re.IGNORECASE):
                await message.channel.send(":zzz: Huh- morning already?")

            elif re.search("good.*afternoon", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(self.afternoon_list))

            elif re.search("good.*night", message.content, re.IGNORECASE):
                await message.channel.send("Um... Good night, I guess.")

            elif re.search("you('re|.*are).*(pretty|beautiful|adorable|cute)", message.content, re.IGNORECASE):
                await message.channel.send("No I’m not.")

            elif re.search("((^|\s)i\s.*apologi(s|z)e|sorry)", message.content, re.IGNORECASE):
                await message.channel.send("I-It’s ok.")

            elif re.search("(i'm.*sick|puking|not.*feeling.*(good|great))", message.content, re.IGNORECASE):
                await message.channel.send("I’m not one for that stuff, maybe ask Monika.")

            elif re.search("(yuri|sayori|natsuki|monika).*best.*(girl|doki)", message.content, re.IGNORECASE):
                await message.channel.send("I’ll have to agree with you there.")

            elif re.search("(you('re|.*are)|^is|mc).*best.*doki", message.content, re.IGNORECASE):
                await message.channel.send("Who? Me? How?")

            elif re.search("(sayori.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.sayori_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send("Of course she does. She loves everyone.")

            elif re.search("(natsuki.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.natsuki_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send("She does? That's a surprise.")

            elif re.search("(yuri.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.yuri_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send("Does she? It's hard to tell when she's so quiet.")

            elif re.search("(monika.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.monika_id}>.*loves.*you)", message.content, re.IGNORECASE):
                await message.channel.send("She doesn't just love me. She's a bit of a yandere.")

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                await message.channel.send("Um… what?")

            elif "test" in message.content.lower():
                await message.channel.send("Yes, I'm fine.")

            else:
                await message.channel.send("Eh?")


def setup(bot):
    bot.add_cog(Tagging(bot))