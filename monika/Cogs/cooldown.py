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
                await ctx.send("Hold on. I'm still recovering from that last tickle...")
            elif ctx.command == "hug":
                await ctx.send("You're giving me hugs too quickly! ~~It's a bit unprofessional for me to do hugs, though.~~")
            elif ctx.command == "headpat":
                await ctx.send("Let me fix my head bow first.")


def setup(bot):
    bot.add_cog(Cooldown(bot))