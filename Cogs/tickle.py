import discord, asyncio, random
import discord.ext.commands as client


class Tickle(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def tickle(self,ctx):
        if self.b.doki == "mc":
            laughs = ["I'm not ticklish, please stop.", "What is this? Why are you tickling me?", "Why are you doing this? I am not ticklish!"]
        elif self.b.doki == "monika":
            laughs = ["Ahahahaha!!", "Hehehehehe!", "N-Now, hold on! Th-This isn't right! Ahahaha!!", "Ehehehehehehe!!!"]
        elif self.b.doki == "natsuki":
            laughs = ["H-hey! Cut that out!! Ahahahaha!!", "Hehehehe!!", "Ehehehe!", "STOP IT! STOP! EHEHEHEHE!!!", "I'm gonna break your ribs for this! Hehehe!"]
        elif self.b.doki == "sayori":
            laughs = ["Hehehehehe!~", "Ahahahaha!!", "*giggles*", "**PFFFT AHAHAHAHAHAHHAHAHAHHAHA!!!!!**", "Ehehe!~", "WAHAHAHAHAHA!!!~"]
        async with ctx.message.channel.typing():
            await asyncio.sleep(self.b.config['type_speed'])  
        await ctx.send(random.choice(laughs))


def setup(bot):
    bot.add_cog(Tickle(bot))
