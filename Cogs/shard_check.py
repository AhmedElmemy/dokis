import discord, asyncio
import discord.ext.commands as client


class ShardCheck(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    @client.guild_only()
    async def shard(self,ctx): 
        if self.b.test_mode is True:
            await ctx.send("Sharding is disabled on testing mode!")
        else:
            await ctx.send(f"You're on **Shard {ctx.guild.shard_id}**.")


def setup(bot):
    bot.add_cog(ShardCheck(bot))
