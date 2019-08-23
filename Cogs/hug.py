import discord, random, asyncio
import discord.ext.commands as client


class Hug(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def hug(self,ctx, *, message=None):
        member = ctx.message.content.split(" ")[0]
        if message is None:
            if self.b.doki == "mc":
                hug_list = [f"Uh, ok? *hugs <@{ctx.author.id}>*", f"I don't do hugs, <@{ctx.author.id}>", f"I mean, if you want. *hugs <@{ctx.author.id}>*", "No thanks, I'm fine.", f"If it makes you happy, then fine. *hugs <@{ctx.author.id}>*", "*runs away*"]
            elif self.b.doki == "monika":
                hug_list = [f"As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs <@{ctx.author.id}>*", f"Of course I'll hug you! You don't have to even ask twice! *hugs <@{ctx.author.id}>*",f"Have you had a rough day? Here, I'll make it a little better! *hugs <@{ctx.author.id}>*"]
            elif self.b.doki == "natsuki":
                hug_list = [f"F-fine, but only because I'll look like a jerk if I don't! *hugs <@{ctx.author.id}>*", f"I guess a quick hug never hurt anyone... *hugs <@{ctx.author.id}>*"]
            elif self.b.doki == "sayori":
                hug_list = [f"One hug, coming right up! *hugs <@{ctx.author.id}>*", f"I'll try not to squeeze too hard! *hugs <@{ctx.author.id}>*", f"Time for the super-mega-cinnamon-bun hug! *hugs <@{ctx.author.id}>*", f"How could I say no to a hug? *hugs <@{ctx.author.id}>*", f"Yay, hugs! *hugs <@{ctx.author.id}>*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])  
            await ctx.send(random.choice(hug_list))

        elif message.lower() == ('@everyone' or '@here'):
            if self.b.doki == "mc":
                await ctx.send("No.")
            elif self.b.doki == "monika":
                await ctx.send("I don't think I can hug everyone here.")
            elif self.b.doki == "natsuki":
                await ctx.send("I am not hugging everyone, dummy.")
            elif self.b.doki == "sayori":
                await ctx.send("We don't need to get everyone's attention!")
            
        elif message == 'f<@{self.b.user.id}>':
            if self.b.doki == "mc":
                hug_list = ["There's no way I'm going to do that.", "Alright, fine. *hugs myself*", "*hugs myself* This feels weird."]
            elif self.b.doki == "monika":
                hug_list = ["Ehehe! This is quite odd, but if it'll make you happy, then who am I to deny you that? *hugs myself*", "*hugs myself* Ahaha! This isn't just some trick to make me look silly, is it?", "Well, as Club President, it's my job to set a good example! *hugs myself*"]
            elif self.b.doki == "natsuki":
                hug_list = ["...fine. *hugs myself*", "Well, if you say so... *hugs myself*", "*hugs myself* Huh. Now I see why you guys like my hugs so much."]
            elif self.b.doki == "sayori":
                hug_list = ["A hug for me? Yay! *hugs myself*", "Well, if you insist! *hugs myself*", "Awww, you're too kind! *hugs myself*", "How can I say no to that? *hugs myself*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            await ctx.send(random.choice(hug_list))

        else:
            if self.b.doki == "mc":
                hug_list = [f"Uh, ok? *hugs {message}*", f"I don't do hugs, <@{ctx.author.id}>", f"I mean, if you want. *hugs {message}*", "No thanks, I'm fine.", f"If it makes you happy, then fine. *hugs {message}*","*runs away*"]
            elif self.b.doki == "monika":
                hug_list = [f"As Club President, this seems unprofessional. As your friend, I'll happily help! *hugs {message}*", f"Of course I'll hug you! You don't have to even ask twice! *hugs {message}*",f"Have you had a rough day? Here, I'll make it a little better! *hugs {message}*"]
            elif self.b.doki == "natsuki":
                hug_list = [f"F-fine, but only because I'll look like a jerk if I don't! *hugs {message}*", f"I guess a quick hug never hurt anyone... *hugs {message}*"]
            elif self.b.doki == "sayori":
                hug_list = [f"One hug, coming right up! *hugs {message}*", f"I'll try not to squeeze too hard! *hugs {message}*", f"Time for the super-mega-cinnamon-bun hug! *hugs {message}*", f"How could I say no to a hug? *hugs {message}*", f"Yay, hugs! *hugs {message}*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            await ctx.send(random.choice(hug_list))


def setup(bot):
    bot.add_cog(Hug(bot))
