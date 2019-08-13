import discord, random, asyncio, chalk,re
from discord.ext import commands as client
from Cogs.config import conf


class Event(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.Cog.listener()
    async def on_message(self,message):
        if message.author.bot or message.guild.id not in conf.w_tog_on:
            return

        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id: #Monika
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Get your fucking hands off of me!!")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh! Well, that was certainly unexpected!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id: #Monika
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Get your dirty, selfish hands off of me before I kill you and take your spot as President!!")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("O-Oh! Well, uh, thank you, Monika.")
                        
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id: #Sayori
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I'm sorry, who are you? And why are you hugging me?")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("H-Hey! Don't hug so hard, Sayori!")

        if "geez, yuri! don't make it all awkward!" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I'm sorry...")

        if "w-well it's not like i love her back or anything!!" in message.content.lower() and message.author.id == conf.natsuki_id:  
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("No shocker there, you selfish bitch!")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Oh... I see...")
                    
        if "what the hell?? yuri, why would you say something so mean??" in message.content.lower() and message.author.id == conf.natsuki_id:  
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Because it's the fucking truth, you little bitch!!")
            
        if "aww thank you, yuri!" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Y-You're welcome, Sayori.")

        if "well, of course she does! yuri loves everybody!" in message.content.lower() and message.author.id == conf.sayori_id:   
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("No, I don't. In fact, I hate most people.")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("S-Sayori! You didn't have to say it like that...")
                
        if "yuri, it's me! sayori! your friend and vice president of the literature club!" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("What the fuck?? ***I'M*** the Vice President, you stupid bitch! And I'm no friend of yours!!")

        if "i-it's me, sayori! and i-i just wanted to hug you!" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Sorry, but I don't know you. Please get your messy, stupid self away from me.")
            
        if "well, that's a pleasant surprise! and i understand why she doesn't have the courage to say it to me directly." in message.content.lower() and message.author.id == conf.monika_id:   
            if message.guild.id in conf.act2:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Except that I don't love you, sooo...")
                
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("Uuu... :flushed:")    

        if "y_act1" in message.content.lower() and (message.author.id == conf.monika_id or message.author.id == conf.mc_id):
            if message.guild.id in conf.act2:
                conf.act2.remove(message.guild.id) 
                await message.channel.send("O-Oh... Wh-What just happened? I feel funny...")
            else:
                await message.channel.send("Oh snap! You encountered a bug! Please report this to the developers if you're seeing this message!")
                pass

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if message.guild.id in conf.act2:
                await message.channel.send(f"That's right <@{conf.mc_id}>, let me feel your pulsating cock on my pussy.")
            else:
                await message.channel.send("Augh!")

        if "fuck no, get away from me, yuri." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Then I'll stab you and crawl in your skin.")

        if "i-i love you, yuri." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if message.guild.id in conf.act2:
                await message.channel.send(f"I love you too, you sexy <@{conf.mc_id}>! Now fuck me!!! :smirk:")
            else:
                await message.channel.send("*tackle hugs MC*")

        if "you're going to stab them to death if they try, aren't you?" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")

        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------


def setup(bot):
    bot.add_cog(Event(bot))
