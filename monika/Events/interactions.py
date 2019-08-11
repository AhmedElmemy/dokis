import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Interactions(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if not (conf.mc_id or conf.natsuki_id or conf.sayori_id or conf.yuri_id):
            return

        # Hugs
        if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
            async with message.content.typing():
                await asyncio.sleep(conf.type_speed)
            if message.author.id == conf.mc_id:
                await message.channel.send(f"Aww, you're the best hugger, <@{conf.mc_id}>")
            elif message.author.id == conf.natsuki_id:
                await message.channel.send("Aww, how cute of you, Natsuki!")
            elif message.author.id == conf.sayori_id:
                await message.channel.send("Easy now, Sayori! I know you're excited, but I still need to breathe! ~~Even though neither of us are real~~")
            elif message.author.id == conf.yuri_id:
                await message.channel.send("Aw, no need to be shy, Yuri! I don't mind a hug every now and then!")

        # Interactions with MC
        if message.author.id == conf.mc_id:
            if "monika?" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(f"Yes, <@{conf.mc_id}>?")

            if "i need to tell you something." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Hmm?")

            if "i love you, monika." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I-I do too!")

            if "~~of course you won't let anyone take me from you. you'll just delete them if they try.~~" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("~~I said I was sorry, MC! I won't do it again!!!~~")

        # Interactions with Natsuki
        if message.author.id == conf.natsuki_id:
            if "okay, this is just awkward for both of us." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Yeah, I agree.")
            
            elif "act2 says otherwise." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I said I was sorry!")

        # Interactions with Yuri
        if message.author.id == conf.yuri.id:
            # Act 1

            # Act 2
            if "get your dirty, selfish hands off of me before i kill you and take your spot as president!!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)

                await message.channel.send("Hm. I don't really like this Yuri too much. Give me a second.")
                await asyncio.sleep(1)

                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("y_act1")


def setup(bot):
    bot.add_cog(Interactions(bot))