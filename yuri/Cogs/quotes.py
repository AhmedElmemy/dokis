import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Quotes(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def quote(self,ctx): 
        quote_list = ["Here's a suggestion. Have you considered killing yourself? It would be beneficial to your mental health.", "After all, doesn't a hot cup of tea help you enjoy a good book?", "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?", "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment.", "Monika, please mind your own business for once. Or do you want to tell me there's something wrong with helping involve MC in club activities?", "Yes! I have terrible reading posture! So that's why we should sit on the floor.", "The thing is, I'm kind of into knives... They're just...so pretty...", "Just...for a little longer. It feels really nice...", "Sorry that my lifestyle is too much for someone of your mental age to comprehend!", "D-Did you just accuse me of cutting myself?? What the fuck is wrong with your head?!", "I love you so much that I even touch myself with the pen I stole from you.", "I just want to pull your skin open and crawl inside of you.", "Stagnating air is common foreshadowing that something terrible is about to happen..."]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(quote_list))


def setup(bot):
    bot.add_cog(Quotes(bot))
