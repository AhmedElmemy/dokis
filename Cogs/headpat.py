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
        await ctx.send(random.choice(headpat_list))


def setup(bot):
    bot.add_cog(Headpat(bot))
