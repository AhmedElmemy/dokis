import discord, asyncio
import discord.ext.commands as client


class Interactions(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.id == (self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']):
            pass
        else:
            return

        # Hugs
        if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
            async with message.content.typing():
                await asyncio.sleep(int(self.bot.config['type_speed']))
            if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send(f"Ah! You scared me, <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>")
            elif message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send("Okay, this is just awkward for both of us.")
            elif message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send("H-hey! Let me go, Sayori!!")
            elif message.author.id == self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send("Geez, Yuri! Don't make it all awkward!")

        # Interactions with MC
        if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
            if "h-hey, natsuki?" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("What do you want, dummy?")

            if "i-i love you, natsuki..." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("*blushes* O-Oh...")
                await asyncio.sleep(1)
                async with message.channel.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed'])) 
                await message.channel.send("Well, I-I do too...")

            if "*hugs natsuki*" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("*hugs back*")

            if "i'm not surprised she would say that, given how much of a tsundere she is." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("***I AM NOT A TSUNDERE, YOU BAKA!!!***")

        # Interactions with Monika
        if message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
            if "oh, really? she, of all people, said that?" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("***NO!!!*** I never said that!!")

        # Interactions with Sayori
        if message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
            if "awww, she does??" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("S-shut up! No, I don't!")

        # Interactions with Yuri
        if message.author.id == self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']:

            # Act 1
            if "oh... i see..." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("...great, now I look like the bad guy!")

            if "sh-she does?" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("Urk! N-No! Not like that!!")

            # Act 2
            if "pfft. as if. that immature brat doesn't love anyone but herself." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send("What the hell?? Yuri, why would you say something so mean??")

            if "because it's the fucking truth, you little bitch!!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send(":rage: :rage: :rage:")

            if ("get your fucking hands off of me!!" or "no shocker there, you selfish bitch!") in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(int(self.bot.config['type_speed']))
                await message.channel.send(":angry:")


def setup(bot):
    bot.add_cog(Interactions(bot))
