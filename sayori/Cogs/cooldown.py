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
            if str(ctx.command) == "tickle":
                await ctx.send("Time out! Time out!! Ahaha!")
            elif str(ctx.command) == "hug":
                await ctx.send("Give me a few seconds; I'm still getting over how nice that last hug was!")
            elif str(ctx.command) == "joke":
                await ctx.send("Hold on! I need time to think of another joke for you...")
            elif str(ctx.command) == "headpat":
                await ctx.send("Let me fix my bow real quick...")
            elif str(ctx.command) == "ask":
                await ctx.send("Please, please! I can only answer so many of your questions at once!")
            elif str(ctx.command) == "swear":
                await ctx.send("Jus' gotta get tis soap outta ma mout...")
            elif str(ctx.command) == ("help" or "commands" or "phrases"):
                await ctx.send("You just asked for that list. It shouldn't be too far up!")
            elif str(ctx.command) == "invite":
                await ctx.send("Hey, you just asked for the link, you goofball!")
            elif str(ctx.command) == "feed":
                await ctx.send("Hol' on. Shtill eatin'.")
            elif str(ctx.command) == "poems":
                await ctx.send("I just pulled the list up, you silly goose! No need to pull it up again right away!")
            elif str(ctx.command) == "quote":
                await ctx.send("I've got a lot of quotes; I just need to think of another one real fast...")


def setup(bot):
    bot.add_cog(Cooldown(bot))