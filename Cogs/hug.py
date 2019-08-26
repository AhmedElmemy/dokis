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
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    hug_list = [f"Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs <@{ctx.author.id}>*", f"Just let me know if this is too much for you... *hugs <@{ctx.author.id}>*", f"*hugs <@{ctx.author.id}>* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
                elif ctx.guild.id in self.b.act2:
                    hug_list = [f"*hugs <@{ctx.author.id}>* Ahaha... I could hug you forever...!", f"Oh, you have no idea how long I've been waiting for you to say that!! *hugs <@{ctx.author.id}>*", f"*hugs <@{ctx.author.id}>* Mmm... You smell so wonderful! I wish I could smell this smell forever!", f"Uhuhu... You can even grab my ass while we hug if you wanted. I don't mind ;) *hugs <@{ctx.author.id}>*", f"*hugs <@{ctx.author.id}>* Oh, you're pressing hard against my chest. I must say, I really, really love it!"]
                else:
                    hug_list = [f"Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs <@{ctx.author.id}>*", f"Just let me know if this is too much for you... *hugs <@{ctx.author.id}>*", f"*hugs <@{ctx.author.id}>* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
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
            elif self.b.doki == "yuri":
                await ctx.send("I'm not getting everyone's attention.")
            
        elif message == ('f<@{self.b.user.id}>' or self.b.doki or "yourself"):
            if self.b.doki == "mc":
                hug_list = ["There's no way I'm going to do that.", "Alright, fine. *hugs myself*", "*hugs myself* This feels weird."]
            elif self.b.doki == "monika":
                hug_list = ["Ehehe! This is quite odd, but if it'll make you happy, then who am I to deny you that? *hugs myself*", "*hugs myself* Ahaha! This isn't just some trick to make me look silly, is it?", "Well, as Club President, it's my job to set a good example! *hugs myself*"]
            elif self.b.doki == "natsuki":
                hug_list = ["...fine. *hugs myself*", "Well, if you say so... *hugs myself*", "*hugs myself* Huh. Now I see why you guys like my hugs so much."]
            elif self.b.doki == "sayori":
                hug_list = ["A hug for me? Yay! *hugs myself*", "Well, if you insist! *hugs myself*", "Awww, you're too kind! *hugs myself*", "How can I say no to that? *hugs myself*"]
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    hug_list = ["What? O-Okay, I suppose... *hugs myself*", "*hugs myself* Oh, dear, this must look so embarassing! Uuuu...!"]
                elif ctx.guild.id in self.b.act2:
                    await ctx.send("But I don't ***want*** to hug myself! I want to hug ***YOU!!!***")
                    return
                else:
                    hug_list = ["What? O-Okay, I suppose... *hugs myself*", "*hugs myself* Oh, dear, this must look so embarassing! Uuuu...!"]
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
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    hug_list = [f"Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs {message}*", f"Just let me know if this is too much for you... *hugs {message}*", f"*hugs {message}* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
                elif ctx.guild.id in self.b.act2:
                    if message == (f"<@{self.b.config['mc']['test_id' if self.b.test_mode else 'public_id']}>" or "mc"):
                        await ctx.send(f"Hey <@{self.b.config['mc']['test_id' if self.b.test_mode else 'public_id']}>, get your sexy body over here and fuck me~")
                    else:
                        await ctx.send("No. I refuse to hug anyone other than you.")
                    return
                else:
                    hug_list = [f"Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs {message}*", f"Just let me know if this is too much for you... *hugs {message}*", f"*hugs {message}* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(self.b.config['type_speed'])
            await ctx.send(random.choice(hug_list))


def setup(bot):
    bot.add_cog(Hug(bot))
