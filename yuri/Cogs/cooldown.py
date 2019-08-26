import discord, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Cooldown(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, discord.ext.commands.errors.CommandOnCooldown):
            if ctx.guild is None:
                pass
            elif ctx.guild.id in self.bot.act2:
                if ctx.command == "tickle":
                    await ctx.send("Oh! So you want to tickle me that badly, do you?")
                elif ctx.command == "hug":
                    await ctx.send("Another hug so soon? I can still feel the last hug you just gave me!")
                elif ctx.command == "headpat":
                    await ctx.send("Let me fix my hair first! I can't look like a mess in front of my love!")
                return
            if ctx.command == "tickle":
                await ctx.send("Please, not so soon. You just tickled me a few seconds ago.")
            elif ctx.command == "hug":
                await ctx.send("Give me a moment. I'm still recovering from that last hug...")
            elif ctx.command == "headpat":
                await ctx.send("I need to fix my hair. Uuuuuu...")


def setup(bot):
    bot.add_cog(Cooldown(bot))