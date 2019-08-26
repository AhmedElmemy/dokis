import discord, asyncio
import discord.ext.commands as client


class InteractionsActTwo(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_message(self, message):
        if message.author.id == (self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']):
            pass
        if message.guild is None:
            return
        if message.guild.id not in self.bot.act2:
            return

        if (f"hugs <@{self.bot.user.id}>" or f"hugs @!<{self.bot.user.id}>") in message.content.lower():
            async with message.content.typing():
                await asyncio.sleep(self.bot.config['type_speed'])
            if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send(f"That's right <@{self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']}>, let me feel your pulsating cock on my pussy.")
            elif message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send("Get your dirty, selfish hands off of me before I kill you and take your spot as President!!")
            elif message.author.id == self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send("Get your fucking hands off of me!!")
            elif message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
                await message.channel.send("I'm sorry, who are you? And why are you hugging me?")

        # y_act1
        if "y_act1" in message.content.lower() and (message.author.id == (self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id'] or self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id'])): # Act 2
            if message.guild.id in self.bot.act2:
                self.bot.act2.remove(message.guild.id)
                await message.channel.send("O-Oh... Wh-What just happened? I feel funny...")
            else:
                await message.channel.send("Oh snap! You encountered a bug! Please report this to the developers if you're seeing this message!")
                pass

        # Interactions with MC
        if message.author.id == self.bot.config['mc']['test_id' if self.bot.test_mode else 'public_id']:
            if "i-i love you, yuri." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send(f"I love you too, you sexy <@{conf.mc_id}>! Now fuck me!!! :smirk:")
            elif "fuck no, get away from me, yuri." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("Then I'll stab you and crawl in your skin.")
            elif "you're going to stab them to death if they try, aren't you?" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")

        # Interactions with Monika
        if message.author.id == self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']:
            if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("Except that I don't love you, sooo...")

        # Interactions with Natsuki
        if message.author.id == self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']:
            if "w-well it's not like i love her back or anything!!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("No shocker there, you selfish bitch!")
            elif "what the hell?? yuri, why would you say something so mean??" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("Because it's the fucking truth, you little bitch!!")
                
        # Interactions with Sayori
        if message.author.id == self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']:
            if "well, of course she does! yuri loves everybody!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("No, I don't. In fact, I hate most people.")

            elif "yuri, it's me! sayori! your friend and vice president of the literature club!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("What the fuck?? ***I'M*** the Vice President, you stupid bitch! And I'm no friend of yours!!")

            elif "i-it's me, sayori! and i-i just wanted to hug you!" in message.content.lower():
                async with message.content.typing():
                    await asyncio.sleep(self.bot.config['type_speed'])
                await message.channel.send("Sorry, but I don't know you. Please get your messy, stupid self away from me.")


def setup(bot):
    bot.add_cog(InteractionsActTwo(bot))