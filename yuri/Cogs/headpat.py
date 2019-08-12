import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Headpat(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self.headpat_list = ["Mmm... :relaxed:", "Oh... I'm not sure how to feel about that...", "H-Hey, could you be a little more gentle, please?", "That feels rather nice...", "T-Thank you."]

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def headpat(self,ctx):
        if ctx.guild is None:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await ctx.send(random.choice(self.headpat_list))

        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if ctx.guild.id not in conf.act2:
                await ctx.send(random.choice(self.headpat_list))
            else:
                headpat_list2 = ["Oh, only my head is being pat? Shame.", "Huhuhu. I love it when you do cute things like that to me!", "Mmm... You know what would be better? If you moved that hand somewhere else...", "Oh, am I your dog or something? That's okay. I'll be anything you want me to be, my love."]
                await ctx.send(random.choice(headpat_list2))


def setup(bot):
    bot.add_cog(Headpat(bot))
