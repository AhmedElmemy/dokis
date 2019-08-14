﻿import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Interactions(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if not (conf.mc_id or conf.monika_id or conf.natsuki_id or conf.yuri_id):
            return

        # Hugs
        if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
            async with message.content.typing():
                await asyncio.sleep(conf.type_speed)
            if message.author.id == conf.mc_id:
                await message.channel.send(f"Aww you're such a sweetheart, <@{conf.mc_id}>")
            elif message.author.id == conf.monika_id:
                await message.channel.send("Ehehe! I love your hugs, Monika! You should give them more often!")
            elif message.author.id == conf.natsuki_id:
                await message.channel.send("Hehehe! You give the best hugs, Natsuki!")
            elif message.author.id == conf.yuri_id:
                await message.channel.send("Aww, thank you, Yuri!")

        # Interactions with MC
        if message.author.id == conf.mc_id:
            if "finnnnnnne, sayori." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(f"YAY! *keeps hugging <@{conf.mc_id}>*")

            if "hey, sayori?" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(f"Yes, <@{conf.mc_id}>?")

            if "i-i love you, sayori" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I-I do too! *hugs MC*")

        # Interactions with Monika
        if message.author.id == conf.monika_id:
            if "ahaha!~ well, after everything that's happened between us, that's nice to hear!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Hey, everyone deserves forgiveness! Even you, Monika!")

        # Interactions with Natsuki
        if message.author.id == conf.natsuki_id:
            if "s-shut up! no she doesn't!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh, yes I do!")

            if "s-shut up! no i don't!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Awww... :(")

        # Interactions with Yuri
        if message.author.id == conf.yuri_id:

            # Act 1
            if "h-hey! don't hug so hard, sayori!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oops! I'm sorry!")

            if "haha. well, she is a loving soul." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("You bet your booty I am! :yum:")

            # Act 2
            if "who the hell is sayori? i don't know any sayoris..." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Yuri, it's me! Sayori! Your friend and Vice President of the Literature Club!")

            if "what the fuck?? ***i'm*** the vice president, you stupid bitch! and i'm no friend of yours!!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(":disappointed_relieved: :cold_sweat: :confounded: :sob:")

            if "sorry, but i don't know you. please get your messy, stupid self away from me." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("O-Okay... I'm sorry... :pensive:")


def setup(bot):
    bot.add_cog(Interactions(bot))