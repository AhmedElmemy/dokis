import discord, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Cooldown(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, discord.ext.commands.errors.CommandOnCooldown):
            if ctx.command == "tickle":
                await ctx.send("Time out! Time out!! Ahaha!")
            elif ctx.command == "hug":
                await ctx.send("Give me a few seconds; I'm still getting over how nice that last hug was!")
            elif ctx.command == "joke":
                await ctx.send("Hold on! I need time to think of another joke for you...")
            elif ctx.command == "headpat":
                await ctx.send("Let me fix my bow real quick...")


def setup(bot):
    bot.add_cog(Cooldown(bot))