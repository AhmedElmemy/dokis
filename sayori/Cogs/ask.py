import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Ask(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def ask(self,ctx, arg1=None):
        if arg1 is None:
            await ctx.send("I can't answer the question if you don't ask one, silly!")
        else:
            answer_list = ["Yes!", "No.", "Maybe.", "Possibly?", "Of course, silly!", "I'd say ask Monika, but she's busy being ~~a meanie~~ an amazing club president!", "I'd say ask Yuri, but she's a little shy at the moment.", "I'd say ask Natsuki, but she's busy baking some cookies for ~~me to steal~~ the club!", "You've got a better chance of having a happy ending in DDLC! Ehehe...~", "Maybe we should ask The Magic Conch, instead.", "As sure as I'm depressed!", "Not really.", "My Vice President Powers tell me yes!", "My Vice President Powers tell me no!", "My Vice President Powers tell me maybe!", "J-Just a little bit!"]            
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(answer_list))


def setup(bot):
    bot.add_cog(Ask(bot))
