import discord, os, subprocess, Cogs.checks, asyncio
import discord.ext.commands as client

checks = Cogs.checks

class Developer(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @checks.dev()
    async def shutdown(self,ctx):
        embed = discord.Embed(title = "Closing this instance...",color=int(self.b.config[self.b.doki]["embed_color"], base=16))
        await ctx.send(embed=embed)
        await self.b.change_presence(status=discord.Status.dnd)
        await quit()

    @client.command()
    @checks.dev()
    async def restart(self,ctx):
        embed = discord.Embed(title = "Give me a moment to restart...",color=int(self.b.config[self.b.doki]["embed_color"], base=16))
        await ctx.send(embed=embed)
        await self.b.change_presence(status=discord.Status.idle)
        print("A developer has restarted the bot!")
        print("\n")
        if self.b.test_mode:
            subprocess.call([sys.executable, f"doki.py {self.b.doki} -test"])
        else:
            subprocess.call([sys.executable, f"doki.py {self.b.doki}"])
        await quit()

    @client.command()
    @checks.dev()
    async def say(self, ctx, *, message):
        try:
            await ctx.message.delete()
            await ctx.send(message)
        except discord.errors.Forbidden:
            await ctx.send(message)

    # Pulled from my bot (Axiro) for the sake of development. -iDroid
    @client.command()
    @checks.dev()
    async def pull(self, ctx):
        if self.b.doki is not "monika":
            return
        c = subprocess.call(('git', 'pull'))
        if c != 0:
            await ctx.send("Updating from Git failed.")
            return
        await ctx.send("Successfully updated from Git.")


def setup(bot):
    bot.add_cog(Developer(bot))