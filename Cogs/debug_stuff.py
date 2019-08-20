import discord, Cogs.checks, asyncio, sys
import discord.ext.commands as client


checks = Cogs.checks
class Debug(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @checks.dev()
    @client.command(enabled=True)
    async def debug(self,ctx):
        e = discord.Embed(title=f"Debug information for {self.b.doki}", description=f"**Version: {self.b.config['version']} \n\
        **Username:** {self.b.user.name} \n\
        **Prefix:** {self.b.config[self.b.doki]['prefix']} \n\
        **Testing Mode:** {self.b.test_mode} \n\
        **Type Speed:** {self.b.config['type_speed']} \n\
        **Discord.py Version:** {discord.__version__} \n\
        **Python Version:** {'.'.join(map(str, sys.version_info[:3]))}",color=0x36393f)
        e.set_author(name=f"Hello, {ctx.author.name}!", icon_url=ctx.author.avatar_url)

        # TODO: Move to database.
        #if ctx.guild.id in conf.w_tog_off:
            #e2 = discord.Embed(title=f'''Does Guild use chat triggers: No''',color=0x36393f)
        #else:
            #e2 = discord.Embed(title=f'''Does Guild use chat triggers: Yes''',color=0x36393f)        

        if self.b.test_mode is False:
            e3 = discord.Embed(title=f'''Number of Shards: {len(self.b.shards)} Total Guilds: {len(self.b.guilds)}''',color=0x36393f)
        else:
            pass

        e4 = discord.Embed(title="Doki IDs:", description=f"**Monika:** {self.b.config['monika']['test_id' if self.b.test_mode else 'public_id']} \n\
        **Natsuki:** {self.b.config['natsuki']['test_id' if self.b.test_mode else 'public_id']} \n\
        **Sayori:** {self.b.config['natsuki']['test_id' if self.b.test_mode else 'public_id']} \n\
        **Yuri:** {self.b.config['natsuki']['test_id' if self.b.test_mode else 'public_id']} \n\
        **MC:** {self.b.config['natsuki']['test_id' if self.b.test_mode else 'public_id']}",color=0x36393f)

        await ctx.send(embed=e)
        #await ctx.send(embed=e2)
        if self.b.test_mode is False:
            await ctx.send(embed=e3)
        await ctx.send(embed=e4)


def setup(bot):
    bot.add_cog(Debug(bot))
