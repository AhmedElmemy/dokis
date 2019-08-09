import discord, random, asyncio, chalk, re
from discord.ext import commands as client
from Cogs.config import conf


class Event(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.Cog.listener()
    async def on_ready(self): #When the bot is ready
        print("\n")
        print(chalk.green(f"[SUCCESS] Connected to Discord as: {self.b.user}"))
        if conf.sharding is False: #If sharding is disabled
            print(chalk.red(f"[WARNING] Sharding: Disabled"))
        elif conf.sharding is True: #If sharding is Enabled
            print(chalk.green("[INFO] Sharding: Enabled"))
            print(chalk.yellow(f"[INFO] Using SHARD's {self.b.shard_ids}")) #Shows us how many shards we are currently using

        print(chalk.cyan(f"[INFO] Config name: '{conf.name}'")) #Shows us the name defined in the config
        print(chalk.cyan(f"[INFO] Default Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'")) #Shows us the 2 prefixes defined in the config
        print(chalk.cyan("[INFO] Are you braindead: Most Likely")) #Yup
        print(chalk.cyan(f"[INFO] I'm currently in [{len(self.b.guilds)}] server(s).")) #Shows us how many servers we are in
        aaa = True
        for guild in self.b.guilds: #Set all guild the doki is in to have triggers enabled on startup otherwise they no be in list which means triggers are off.
            conf.w_tog_on.insert(0, guild.id)
        while aaa: #A loop to make the game activity change every 900 seconds
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    @client.Cog.listener()
    async def on_guild_join(self,guild):
        conf.w_tog_on.insert(0, guild.id)
        # Remember to add a message here

    @client.Cog.listener()
    async def on_message(self,message):
        if message.author.bot or message.guild.id not in conf.w_tog_on:
            return
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        trigger_words = ["rope", "poetry"]

        # ------------------------------------------------------------------------------------------------------------------------------------------------
        mct =  message.content.lower().split(" ") # (MCT | Message Contents)
        for word in mct:
            if message.content.lower() in trigger_words:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                if word == trigger_words[0]:
                    await message.channel.send("NO!")
                else:
                    await message.channel.send("Oh... you make poems too, cool.")
                return
                        
            # -------------------------------------------------------Tagging-------------------------------------------------------
        if re.search(f"^<@!?{self.b.user.id}>", message.content):

            hello_list = ["Hi, I guess.", "Hello..."]
            afternoon_list = ["Is it a good afternoon?", "What? It's the afternoon?", "Ehhhhhh..."]

            # ---------------------------------------------------- Responding -----------------------------------------------------
            content = re.sub(f'^<@!?{self.b.user.id}>', "", message.content).strip()
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if content == "":
                await message.channel.send("Hm? What is it?")

            elif re.search(r"(^|[^A-Za-z])(hi|hello|hey)([^A-Za-z]|$)", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(hello_list))

            elif re.search("((^|\s)ily(\s|$)|(^|\s)i\s.*love.*you)", message.content, re.IGNORECASE):
                await message.channel.send("...")

            elif re.search("good.*morning", message.content, re.IGNORECASE):
                await message.channel.send(":zzz: Huh- morning already?")

            elif re.search("good.*afternoon", message.content, re.IGNORECASE):
                await message.channel.send(random.choice(afternoon_list))

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

        # -------------------------------------------------------Tagging-------------------------------------------------------



        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------

        if f"aww, you're the best hugger, <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("No I'm not...")

        if f"aww you're such a sweetheart, <@{conf.mc_id}>" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("You will always be my closest friend, Sayori.")

        if "augh!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Sorry...")

        if f"hey <@{conf.mc_id}>, get your sexy body over here and fuck me~" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Fuck no, get away from me, Yuri.")

        if "then i'll stab you and crawl in your skin." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Yeah, fuck no.")
            await asyncio.sleep(1)
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("y_act1")

        if f"that's right <@{conf.mc_id}>, let me feel your pulsating cock on my pussy." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oh hell no...")

        if f"ah! you scared me, <@{conf.mc_id}>" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Sorry, I'm a dumbass.")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*muffled screaming*")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Finnnnnnne, Sayori.")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("No, it's fine...")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.author.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Augh!")

        if f"yes, <@{self.b.user.id}>?" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-I love you, Sayori.")

        if "i-i do too! *hugs mc*" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*hugs back*")

        if f"yes, <@{conf.mc_id}>?" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I need to tell you something.")

        if "hmm?" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I love you, Monika.")

        if "*tackle hugs mc*" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*hugs back*")

        if f"i love you too, you sexy <@{self.b.user.id}>! now fuck me!!!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Oh hell no!")

        if "what do you want, dummy?" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I-I love you, Natsuki...")

        if "well, i-i do too..." in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("*hugs Natsuki*")

        if "ha! i'm sure he does! i-i'll believe it when he tells me that himself!" in message.content.lower() and message.author.id == conf.natsuki_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("I'm not surprised she would say that, given how much of a tsundere she is.")

        if "he does? well, that's nice to hear. ~~i'm still not letting anyone else take him from me, though.~~" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("~~Of course you won't let anyone take me from you. You'll just delete them if they try.~~")

        if "yay! my best friend loves me!!!" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("Uhhhhhhh...")

        if "of course he loves me! and i will make sure **nobody** takes him away from me!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("You're going to stab them to death if they try, aren't you?")
    
        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------

        
def setup(bot):
    bot.add_cog(Event(bot))
