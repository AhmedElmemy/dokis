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
                await ctx.send("Hey! At least let me recover from you tickling me!")
            elif ctx.command == "hug":
                await ctx.send("You just hugged me! C-Can't you wait a bit before you do it again?")
            elif ctx.command == "motivate":
                await ctx.send("I just motivated someone! I need time to get ready!")
            elif ctx.command == "headpat":
                await ctx.send("Ugh. Can you let me fix my hair first?!")


def setup(bot):
    bot.add_cog(Cooldown(bot))