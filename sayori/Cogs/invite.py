import discord, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Invite(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def invite(self,ctx):
            e = discord.Embed(title="My invite link!", description="Here's the server invite link so anyone else here can invite me to their server!", color=conf.norm)
            e.add_field(name="Enjoy!", value="[Click here to invite me!](https://discordbots.org/bot/425696108455657472)", inline=True)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Invite(bot))
