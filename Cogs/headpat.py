import discord, asyncio, random
import discord.ext.commands as client


class Headpat(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def headpat(self,ctx):   
        async with ctx.message.channel.typing():
            await asyncio.sleep(self.b.config['type_speed'])
        if self.b.doki == "mc":
            await ctx.send("Stop it!")
            return
        elif self.b.doki == "monika":
            headpat_list = ["Ahaha!~ I-I'm not sure what to say!", "Be careful; you may knock my bow down!", "E-Easy now!", "This doesn't really seem like the type of thing one does to their President, but I suppose I'll let it slide!"]
        elif self.b.doki == "natsuki":
            headpat_list = ["Hey! Don't pat me so hard!", "Geez, you're gonna mess up my hair!", "...okay, I guess that kinda felt nice...", "What do I look like, a puppy??", "T-thanks, I guess..."]
        elif self.b.doki == "sayori":
            headpat_list = ["Hehehe!~", "Just don't mess up my bow!", "S-stop being so silly! :blush:", "Well, my hair's already pretty messy, so I don't see an issue!", "Hehehe! Thank you!"]
        elif self.b.doki == "yuri":
            if ctx.guild is None:
                headpat_list = ["Mmm... :relaxed:", "Oh... I'm not sure how to feel about that...", "H-Hey, could you be a little more gentle, please?", "That feels rather nice...", "T-Thank you."]
            elif ctx.guild.id in self.b.act2:
                headpat_list = ["Oh, only my head is being pat? Shame.", "Huhuhu. I love it when you do cute things like that to me!", "Mmm... You know what would be better? If you moved that hand somewhere else...", "Oh, am I your dog or something? That's okay. I'll be anything you want me to be, my love."]
            else:
                headpat_list = ["Mmm... :relaxed:", "Oh... I'm not sure how to feel about that...", "H-Hey, could you be a little more gentle, please?", "That feels rather nice...", "T-Thank you."]
        await ctx.send(random.choice(headpat_list))


def setup(bot):
    bot.add_cog(Headpat(bot))
