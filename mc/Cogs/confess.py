import discord, asyncio
import discord.ext.commands as client


class Confess(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def confess(self, ctx, *, arg=None):
        async with ctx.message.channel.typing():
            await asyncio.sleep(int(self.bot.config['type_speed']))
        if arg is None:
            await ctx.send(f"*starts to blush* Ok, I'll admit it <@{ctx.author.id}>, I love you!")
        elif arg == f"<@{self.bot.config['sayori']['test_id' if self.bot.test_mode else 'public_id']}>":
            await ctx.send("Hey, Sayori?")
        elif arg == f"<@{self.bot.config['monika']['test_id' if self.bot.test_mode else 'public_id']}>":
            await ctx.send("Monika?")
        elif arg == f"<@{self.bot.config['yuri']['test_id' if self.bot.test_mode else 'public_id']}>":
            await ctx.send("I-I love you, Yuri.")
        elif arg == f"<@{self.bot.config['natsuki']['test_id' if self.bot.test_mode else 'public_id']}>":
            await ctx.send("H-Hey, Natsuki?")
        else:
            await ctx.send(f"*starts to blush* Ok, I'll admit it {arg}, I love you!")


def setup(bot):
    bot.add_cog(Confess(bot))
