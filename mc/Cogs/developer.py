import discord, json, platform, os, subprocess, Cogs.checks, chalk, sys, traceback, asyncio, textwrap
from discord.ext import commands as client
from os import listdir
from os.path import isfile, join
from Cogs.config import conf

checks = Cogs.checks
Cogs = "Cogs"

class Developer(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self._last_result = None

    @client.command()
    @checks.dev()
    async def shutdown(self,ctx):
        embed = discord.Embed(title = "Closing this instance...",color = conf.norm)
        await ctx.send(embed=embed)
        await self.b.change_presence(status=discord.Status.dnd)
        await quit()

    @client.command()
    @checks.dev()
    async def restart(self,ctx):
        embed = discord.Embed(title = "Give me a moment to restart...",color = conf.norm)
        await ctx.send(embed=embed)
        await self.b.change_presence(status=discord.Status.idle)
        print(chalk.yellow("A developer has restarted the bot!"))
        print("\n")
        subprocess.call([sys.executable, "maid.py"])
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
        c = subprocess.call(('git', 'pull'))
        if c != 0:
            await ctx.send("Updating from Git failed.")
            return
        await ctx.send("Successfully updated from Git.")


def setup(bot):
    bot.add_cog(Developer(bot))