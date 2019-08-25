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
        #------------------- Alcohol ------------------- 

        elif arg1 == "☕" or arg1 == "🍵":
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
        #------------------- Birthday Cake -------------------

        elif arg1 == "🔪" and self.b.doki == "mc":
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            await ctx.send("I'm not Act 2 Yuri; feed that to her.")
        #------------------- Knife ------------------- 

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
        #------------------- Not Listed -------------------


def setup(bot):
    bot.add_cog(Feed(bot))
