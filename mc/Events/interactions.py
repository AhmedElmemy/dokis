import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Interactions(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if not (conf.monika_id or conf.natsuki_id or conf.sayori_id or conf.yuri_id):
            return

        # Interactions with Monika
        if message.author.id == conf.monika_id:
            if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("*muffled screaming*")

            if f"aww, you're the best hugger, <@{self.bot.user.id}>" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("No I'm not...")

            if f"yes, <@{self.bot.user.id}>?" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I need to tell you something.")

            if "hmm?" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I love you, Monika.")

            if "he does? well, that's nice to hear. ~~i'm still not letting anyone else take him from me, though.~~" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("~~Of course you won't let anyone take me from you. You'll just delete them if they try.~~")

        # Interactions with Natsuki
        if message.author.id == conf.natsuki_id:
            if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Augh!")

            if f"ah! you scared me, <@{self.bot.user.id}>" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Sorry, I'm a dumbass.")

            if "what do you want, dummy?" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I-I love you, Natsuki...")

            if "well, i-i do too..." in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("*hugs Natsuki*")

            if "ha! i'm sure he does! i-i'll believe it when he tells me that himself!" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I'm not surprised she would say that, given how much of a tsundere she is.")

        # Interactions with Sayori
        elif message.author.id == conf.sayori_id:
            if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Finnnnnnne, Sayori.")

            if f"aww you're such a sweetheart, <@{self.bot.user.id}>" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("You will always be my closest friend, Sayori.")

            if f"yes, <@{self.bot.user.id}>?" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I-I love you, Sayori.")

            if "i-i do too! *hugs mc*" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("*hugs back*")

            if "yay! my best friend loves me!!!" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Uhhhhhhh...")

        # Interactions with Yuri
        elif message.author.id == conf.yuri_id:

            # Act 1
            if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("No, it's fine...")

            if "augh!" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Sorry...")

            if "*tackle hugs mc*" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("*hugs back*")

            # Act 2
            if f"hey <@{self.bot.user.id}>, get your sexy body over here and fuck me~" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Fuck no, get away from me, Yuri.")

            if "then i'll stab you and crawl in your skin." in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Yeah, fuck no.")
                await asyncio.sleep(1)
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("y_act1")

            if f"that's right <@{self.bot.user.id}>, let me feel your pulsating cock on my pussy." in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh hell no...")

            if f"i love you too, you sexy <@{self.bot.user.id}>! now fuck me!!!" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh hell no!")

            if "of course he loves me! and i will make sure **nobody** takes him away from me!" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("You're going to stab them to death if they try, aren't you?")


def setup(bot):
    bot.add_cog(Interactions(bot))