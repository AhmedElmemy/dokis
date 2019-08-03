import discord, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Cooldown(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, discord.ext.commands.errors.CommandOnCooldown):
            ## TODO: Sort list in alphabetical order.
            if ctx.command == "tickle":
                await ctx.send("Time out! Time out!! Ahaha!")
            elif ctx.command == "hug":
                await ctx.send("Give me a few seconds; I'm still getting over how nice that last hug was!")
            elif ctx.command == "joke":
                await ctx.send("Hold on! I need time to think of another joke for you...")
            elif ctx.command == "headpat":
                await ctx.send("Let me fix my bow real quick...")
            elif ctx.command == "ask":
                await ctx.send("Please, please! I can only answer so many of your questions at once!")
            elif ctx.command == "swear":
                await ctx.send("Jus' gotta get tis soap outta ma mout...")
            elif ctx.command == ("help" or "commands" or "phrases"):
                await ctx.send("You just asked for that list. It shouldn't be too far up!")
            elif ctx.command == "invite":
                await ctx.send("Hey, you just asked for the link, you goofball!")
            elif ctx.command == "feed":
                await ctx.send("Hol' on. Shtill eatin'.")
            elif ctx.command == "poems":
                await ctx.send("I just pulled the list up, you silly goose! No need to pull it up again right away!")
            elif ctx.command == "quote":
                await ctx.send("I've got a lot of quotes; I just need to think of another one real fast...")


def setup(bot):
    bot.add_cog(Cooldown(bot))