import discord, asyncio
import discord.ext.commands as client


class Feed(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def feed(self,ctx, arg1=None):
        if arg1 is None: # If you don't provide an emoji.
            if self.b.doki == "mc":
                await ctx.send("It's fine, I brought my own food...")
            elif self.b.doki == "monika":
                await ctx.send("I suppose I am a bit hungry... What do you recommend?")
            elif self.b.doki == "natsuki":
                await ctx.send("H-hey! Don't feel like you have to feed me anything! I'm okay!")
            elif self.b.doki == "sayori":
                await ctx.send("You wanna feed me something? I'm open for anything!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Well, I suppose I wouldn't mind a quick meal ~~if it was from you~~.")
                else:
                    await ctx.send("I'll eat anything you like, darling. Anything." if ctx.guild.id in self.b.act2 else "Well, I suppose I wouldn't mind a quick meal ~~if it was from you~~.")
            
        elif arg1 == "🍪":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("I mean, it's not made by Natsuki but I'll eat it.")
            elif self.b.doki == "monika":
                await ctx.send("Not as homemade as Natsuki's, but it's still very delicious! Thank you!")
            elif self.b.doki == "natsuki":
                await ctx.send("I suppose a cookie wouldn't hurt.")
            elif self.b.doki == "sayori":
                await ctx.send("A cookie?? Yummy! Thank you so much!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Oh, the chocolate chips just melt in my mouth!")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Oh, the chocolate chips just melt in my mouth!")

        #------------------- Cookie -------------------

        elif arg1 == ("🍣" or  "🍱" or "🍛" or  "🍙" or  "🍚" or  "🍘" or  "🍜" or "🍢" or "🍡" or "🍥"):
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("I mean, it's from my homeland. *eats happily*")
            elif self.b.doki == "monika":
                await ctx.send("Aw, you brought me a meal from my home? How thoughtful of you!")
            elif self.b.doki == "natsuki":
                await ctx.send("Ah, this is a more familiar meal.")
            elif self.b.doki == "sayori":
                await ctx.send("Oooo! Japanese food! Reminds me of home!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Ah... Now this is something I recognize and love. Er, not that I don't love the other foods I've been offered! Uuu... why do I say these things...")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Ah... Now this is something I recognize and love. Er, not that I don't love the other foods I've been offered! Uuu... why do I say these things...")
        #------------------- Japanese Food ------------------- 

        elif arg1 == "🍕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Yay, pizza!")
            elif self.b.doki == "monika":
                await ctx.send("Ah... There's pepperoni on it... You do remember I'm a vegetarian, right?")
            elif self.b.doki == "natsuki":
                await ctx.send("F-fine, I'll have a slice.")
            elif self.b.doki == "sayori":
                await ctx.send("I love pizza! Thanks!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("A slice of pizza never hurt, right...?")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "A slice of pizza never hurt, right...?")
        #------------------- Pizza ------------------- 

        elif arg1 == "🍔":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Yay, I love hamburgers!")
            elif self.b.doki == "monika":
                await ctx.send("Is it a veggie burger? If not, I'll have to respectfully decline.")
            elif self.b.doki == "natsuki":
                await ctx.send("...only because there's cheese on it...")
            elif self.b.doki == "sayori":
                await ctx.send("Mmmmm! Burgers are delicious!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Fast food? I-I suppose that'll do.")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Fast food? I-I suppose that'll do.")
        #------------------- Burger ------------------- 

        elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Burr, cold.")
            elif self.b.doki == "monika":
                await ctx.send("Ah, nothing like some cold treats to brighten your day!")
            elif self.b.doki == "natsuki":
                await ctx.send("Thanks, I guess. I was actually feeling a bit warm.")
            elif self.b.doki == "sayori":
                await ctx.send("AHH! Brain freeze!!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Uhuhu. A nice, cold treat on a nice, warm day is just an amazing combination.")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Uhuhu. A nice, cold treat on a nice, warm day is just an amazing combination.")
        #------------------- Cold Foods ------------------- 

        elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍷" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("What the fuck? I'm not drinking alcohol!")
            elif self.b.doki == "monika":
                await ctx.send("Oh! Ahaha... A-As curious as I am, I'm afraid I cannot allow alcoholic beverages here.")
            elif self.b.doki == "natsuki":
                await ctx.send("Hey, what's the idea?? You trying to get me drunk??")
            elif self.b.doki == "sayori":
                await ctx.send("H-Hey! I'm too young for that!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("T-Thank you, but I'll have to kindly decline.")
                else:
                    await ctx.send("I'm too young for this, but I'll drink it because you want me to! *chugs*" if ctx.guild.id in self.b.act2 else "T-Thank you, but I'll have to kindly decline.")
        #------------------- Alcohol ------------------- 

        elif arg1 == ("☕" or "🍵"):
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Time to start the day...")
            elif self.b.doki == "monika":
                await ctx.send("Ah, thank you! I've been needing something to wake me up a bit!" if arg1 == "☕" else "It's like I'm back in the clubroom! All I need is one of Natsuki's cupcakes.")
            elif self.b.doki == "natsuki":
                await ctx.send("I don't really like coffee that much, but thanks, anyway." if arg1 == "☕" else "*sips* Just the right temperature. I guess you're not inconsiderate, after all!")
            elif self.b.doki == "sayori":
                await ctx.send("Ah, the delicious beverage known as coffee! Where would I be without thee?" if arg1 == "☕" else "How could I refuse a hot cup of tea? Thank you!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("I-I'm more of a tea drinker. I'm sorry..." if arg1 == "☕" else "Ah, thank you so much. All I need now is a good book.")
                else:
                    await ctx.send("*gulp gulp gulp* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else ("I-I'm more of a tea drinker. I'm sorry..." if arg1 == "☕" else "Ah, thank you so much. All I need now is a good book."))
        #---------------- Coffee or Tea ----------------

        elif arg1 == "🍞" or arg1 == "🥖":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == ("mc" or "sayori"):
                await ctx.send("I mean, I suppose I could survive off of plain bread...")
            elif self.b.doki == "monika":
                await ctx.send("It's a start, but I'll need to go to the grocery store to make a proper sandwich. ~~Would you like to come with?~~")
            elif self.b.doki == "natsuki":
                await ctx.send("Well, it's more than Papa gives me...")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Hm... I suppose I need more ingredients than this, don't you think?")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Hm... I suppose I need more ingredients than this, don't you think?")
        #------------------- Bread ------------------- 

        elif arg1 == "🌶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("***HOTHOTHOTHOTHOT!!!***")
            elif self.b.doki == "monika":
                await ctx.send("*cough cough* Oh, my! That certainly caught me off-guard!")
            elif self.b.doki == "natsuki":
                await ctx.send("H-Hey!! My freaking mouth is on fire!!!")
            elif self.b.doki == "sayori":
                await ctx.send("***OWOWOWOWHOTHOTHOTHOT!!!***")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("O-Oh! Oh my goodness! That has quite a kick!!")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id is self.b.act2 else "O-Oh! Oh my goodness! That has quite a kick!!")
        #------------------- Hot Pepper -------------------

        elif arg1 == "🍳":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Ugh, breakfast foods, great.")
            elif self.b.doki == "monika":
                await ctx.send("Hm... as a vegetarian, would it even be okay to eat this...?")
            elif self.b.doki == "natsuki":
                await ctx.send("Sunny-side up? How did you know that's how I liked them?")
            elif self.b.doki == "sayori":
                await ctx.send("I made eggs and toast!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Oh, I didn't know you knew how to cook eggs!")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Oh, I didn't know you knew how to cook eggs!")
        #------------------- Cooking -------------------

        elif arg1 == "🌮" or arg1 == "🌯":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Noche de taco maravilloso!")
            elif self.b.doki == "monika":
                await ctx.send("Well, I'm always in the mood for something different!")
            elif self.b.doki == "natsuki":
                await ctx.send("Mexican, huh? Not my first choice, but it's still pretty good...")
            elif self.b.doki == "sayori":
                await ctx.send("Ole!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Hehe. A little 'south of the border' meal, huh? Uu, well I suppose that doesn't apply to me because I'm from Japan, not the United States, but... uuu, I'm sorry, I should just stop talking, shouldn't I?")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Hehe. A little 'south of the border' meal, huh? Uu, well I suppose that doesn't apply to me because I'm from Japan, not the United States, but... uuu, I'm sorry, I should just stop talking, shouldn't I?")
        #------------------- Mexican -------------------

        elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send(f"Something sweet? For me? Thanks, <@{ctx.author.id}>")
            elif self.b.doki == "monika":
                await ctx.send("Sweets! A girl's best friend!")
            elif self.b.doki == "natsuki":
                await ctx.send("Well, I suppose it would be nice to eat a sweet that I didn't bake, for once.")
            elif self.b.doki == "sayori":
                await ctx.send("Sweets! My one, true weakness!! *omnomnomnomnom*")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    if arg1 == "🍫":
                        await ctx.send("Oh! This brings up some... memories... with MC...")
                    else:
                        await ctx.send("I suppose a sweet wouldn't be such a bad idea...")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else ("Oh! This brings up some... memories... with MC..." if arg1 == "🍫" else "I suppose a sweet wouldn't be such a bad idea..."))
        #------------------- Sweets -------------------

        elif arg1 == "🍿":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            await ctx.send("*crunch crunch crunch*")
        #------------------- Popcorn -------------------

        elif arg1 == "🍼" or arg1 == "🍭":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("I-I'm not a baby...")
            elif self.b.doki == "monika":
                await ctx.send("U-Um... I'm not sure what you're insinuating here...")
            elif self.b.doki == "natsuki":
                await ctx.send("I feel like there's a loli joke to be made here...")
            elif self.b.doki == "sayori":
                await ctx.send("Hey! I'm not a baby!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("I-I'm not sure what you're insinuating, b-but I don't have a need for th-that...")
                else:
                    await ctx.send("Oh, are you into that kind of thing? Well, I'll happily play along for you. Wah! Waah!" if ctx.guild.id in self.b.act2 else "I-I'm not sure what you're insinuating, b-but I don't have a need for th-that...")
        #------------------- Baby Bottle -------------------

        elif arg1 == "🥚":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Don't I need to cook this first?")
            elif self.b.doki == "monika":
                await ctx.send("Oh, you silly goose! Are you trying to be funny?")
            elif self.b.doki == "natsuki":
                await ctx.send("I'm not so hungry that I'll eat a raw egg! Er, I mean I'm not hungry!")
            elif self.b.doki == "sayori":
                await ctx.send("I feel like I should cook this, first...")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Oh, is it hard-boiled? Oh... no, it's not...")
                else:
                    await ctx.send("Uhuhuhu! Raw eggs? Now you're just being silly, but I'll still accept!" if ctx.guild.id in self.b.act2 else "Oh, is it hard-boiled? Oh... no, it's not...")
        #------------------- Egg ------------------- '''

        elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Well, what are we eating?")
            elif self.b.doki == "monika":
                await ctx.send("I've got my silverware ready! What are we eating with them?")
            elif self.b.doki == "natsuki":
                await ctx.send("I'd prefer actual food here, please! N-not that you have to give me any or anything...")
            elif self.b.doki == "sayori":
                await ctx.send("I didn't know you could eat silverware!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Ah, I'm generally used to chopsticks, but silverware will suffice.")
                else:
                    await ctx.send("Well, I'll admit that it wasn't as disgusting as I had originally assumed!" if ctx.guild.id in self.b.act2 else "Ah, I'm generally used to chopsticks, but silverware will suffice.")
        #------------------- Silverware -------------------
        
        elif arg1 == "🥛":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Milk? Thanks, I guess.")
            elif self.b.doki == "monika":
                await ctx.send("I suppose it's a good thing I'm not a vegan! Ahaha~!")
            elif self.b.doki == "natsuki":
                await ctx.send("What, you didn't have strawberry milk?? Ah, whatever. I guess this is fine...")
            elif self.b.doki == "sayori":
                await ctx.send("Ah, a nice, cold glass of milk is always welcoming!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Th-Thank you. I love a nice glass of milk.")
                else:
                    await ctx.send("*gulp gulp gulp* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Th-Thank you. I love a nice glass of milk.")
        #------------------- Milk -------------------
        
        elif arg1 == "🎂":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send(f"It's not my birthday, and even if it was, I don't want a cake <@{ctx.author.id}>")
            elif self.b.doki == "monika":
                await ctx.send("How wonderful, but I don't believe it's my birthday just yet...")
            elif self.b.doki == "natsuki":
                await ctx.send("Huh? It's not my birthday!")
            elif self.b.doki == "sayori":
                await ctx.send("It's not my birthday, but I accept!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Oh, I-I'm sorry, but you must be confused; it's not my birthday...")
                else:
                    await ctx.send("It's not my birthday, but I'll still eat this cake!" if ctx.guild.id in self.b.act2 else "Oh, I-I'm sorry, but you must be confused; it's not my birthday...")
        #------------------- Birthday Cake -------------------

        elif arg1 == "🔪" and self.b.doki == ("mc" or "yuri"):
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("I'm not Act 2 Yuri; feed that to her.")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Uuuu!! Th-that's not food!")
                else:
                    await ctx.send("Mmmm.... I just wanna rub the blade across my tongue and taste the blood... Maybe I could let you taste it, as well..." if ctx.guild.id in self.b.act2 else "Uuuu!! Th-that's not food!")
        #------------------- Knife ------------------- 

        elif arg1 == "🖊️" and self.b.doki == "yuri":
            if ctx.guild is None:
                await ctx.send("Uuuu!! Th-that's not food!")
            else:
                await ctx.send("Oh, I do believe this is the one with my juices on it. *licks* Mmm... Tasty..." if ctx.guild.id in self.b.act2 else "Uuuu!! Th-that's not food!")
        #------------------- Pen ------------------- 

        elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("Um, thanks? *eats the food*")
            elif self.b.doki == "monika":
                await ctx.send("A nice meal is always great! Thank you~")
            elif self.b.doki == "natsuki":
                await ctx.send("...t-thank you. *slowly eats*")
            elif self.b.doki == "sayori":
                await ctx.send("*om nom nom* Thank you! That was delicious! :grin:")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Oh, you didn't really have to, but thank you so much. *munch munch*")
                else:
                    if arg1 == "🍆":
                        await ctx.send("Mmmm.... I wish this was your long, hard cock... :smirk: I can shove it all the way down my throat, if you'd like..." if ctx.guild.id in self.b.act2 else "Oh, you didn't really have to, but thank you so much. *munch munch*")
                    elif arg1 == "🍑":
                        await ctx.send("It's so sweet and juicy... I just wanna lick all the juices up!" if ctx.guild.id in self.b.act2 else "Oh, you didn't really have to, but thank you so much. *munch munch*")
                    else:
                        await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Oh, you didn't really have to, but thank you so much. *munch munch*")
        #------------------- Misc -------------------

        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            if self.b.doki == "mc":
                await ctx.send("I don't think I can eat that.")
            elif self.b.doki == "monika":
                await ctx.send("Um.. not to be rude, but I don't think this is edible.")
            elif self.b.doki == "natsuki":
                await ctx.send("Are you trying to hurt me?? That's not food!")
            elif self.b.doki == "sayori":
                await ctx.send("Ptoo ptoo! This isn't food, you meanie!")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Uuuu!! Th-that's not food!")
                else:
                    await ctx.send("*munch munch munch* Does that please you, my beloved?" if ctx.guild.id in self.b.act2 else "Uuuu!! Th-that's not food!")
        #------------------- Not Listed -------------------


def setup(bot):
    bot.add_cog(Feed(bot))
