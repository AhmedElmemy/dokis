﻿import discord, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class InteractionsActOne(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if not (conf.mc_id or conf.monika_id or conf.natsuki_id or conf.sayori_id):
            return
        if ctx.guild is None:
            return
        if ctx.guild.id in conf.act2:
            return

        if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
            async with message.content.typing():
                await asyncio.sleep(conf.type_speed)
            if message.author.id == conf.mc_id:
                await message.channel.send("Augh!")
            if message.author.id == conf.monika_id:
                await message.channel.send("O-Oh! Well, uh, thank you, Monika.")
            elif message.author.id == conf.natsuki_id:
                await message.channel.send("Oh! Well, that was certainly unexpected!")
            elif message.author.id == conf.sayori_id:
                await message.channel.send("H-Hey! Don't hug so hard, Sayori!")

        # Interactions with MC
        if message.author.id == conf.mc_id:
            if "i-i love you, yuri." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("*tackle hugs MC*")

        # Interactions with Monika
        if message.author.id == conf.monika_id:
            if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Uuu... :flushed:")

        # Interactions with Natsuki
        if message.author.id == conf.natsuki_id:
            if "geez, yuri! don't make it all awkward!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I'm sorry...")
            elif "w-well it's not like i love her back or anything!!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh... I see...")
                
        # Interactions with Sayori
        if message.author.id == conf.sayori_id:
            if "aww thank you, yuri!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Y-You're welcome, Sayori.")

            elif "well, of course she does! yuri loves everybody!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("S-Sayori! You didn't have to say it like that...")



def setup(bot):
    bot.add_cog(InteractionsActOne(bot))