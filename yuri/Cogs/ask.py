import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Ask(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self.answer_list = ["Y-Yes.", "No...", "I'm not really sure.", "I don't believe so...", "I think that's a question best suited for Sayori.", "Perhaps Monika could be of better help?", "I-I don't know. I'm sorry...", "Natsuki might know.", "I believe so!"]

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def ask(self,ctx, arg1=None):
        if ctx.guild is None:
            if arg1 is None:
                await ctx.send("Did you want to ask me something? S-sorry if i was bothering you! Uuu...")
            else:
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await ctx.send(random.choice(self.answer_list))

        else:
            if arg1 is None:
                if ctx.guild.id not in conf.act2:
                    await ctx.send("Ahaha... If you don't have a question, that's okay. I'd rather stare at you.")
                else:
                    await ctx.send("Did you want to ask me something? S-sorry if i was bothering you! Uuu...")
                return

            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if ctx.guild.id not in conf.act2:
                await ctx.send(random.choice(self.answer_list))
            else:
                answer_list2 = ["Yes.", "I don't know, and I don't care. I just want to look at you...", "No.", "Possibly, but who knows?", "Meet me in the closet and we'll find out... :kissing_closed_eyes:", "Ahaha! You're so silly to ask such a question!", "I'm not sure... I'll think about it while I'm touching myself to you tonight."]
                await ctx.send(random.choice(answer_list2))
        

def setup(bot):
    bot.add_cog(Ask(bot))
