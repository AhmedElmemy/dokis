import traceback, sys, discord, Cogs.checks
from discord.ext import commands

checks = Cogs.checks

class CommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound) or isinstance(error, commands.CheckFailure):
            return

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command.")

        else:
            tra = traceback.format_exception_only(type(error), error)
            e = discord.Embed(description="`Was this supposed to happen?` ```py\n%s\n``` \nLooks like you encountered an issue! If you want, you can report this by clicking [here!](https://forms.gle/hJ3KHVwKMFzfs5eq9) (It takes you to a form where you can explain the bug in detail.)" % ''.join(tra), file=sys.stderr, color=conf.err)
            e.set_author(name="That's an issue!",icon_url=ctx.message.author.avatar_url)
            e.set_footer(text="v"+ver)
            await ctx.send(embed=e)
            print(f"Warning! The command '{ctx.command}' has just Errored!")
            print(f"Traceback: %s" % ''.join(tra))


def setup(bot):
    bot.add_cog(CommandError(bot))
