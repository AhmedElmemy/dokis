import discord, asyncio
import discord.ext.commands as client


class Rename(client.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    @client.guild_only()
    async def rename(self, ctx, name):
        if not ctx.message.channel.permissions_for(ctx.message.author).manage_nicknames:
            await ctx.send("You don't have the proper permissions to change my name.")
            return
        async with ctx.message.channel.typing():
            await asyncio.sleep(self.bot.config['type_speed'])
        try:
            await ctx.message.author.guild.me.edit(nick=f"{name}")
            await ctx.send(f"Ok, guess {name} is my name now.")
        except:
            await ctx.send("I was unable to change my name. Maybe I don't have permission to do this.")


def setup(bot):
    bot.add_cog(Rename(bot))