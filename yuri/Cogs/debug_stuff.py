import discord, Cogs.checks, asyncio, sys
import discord.ext.commands as client
from Cogs.config import conf


checks = Cogs.checks
class Debug(client.Cog):

    def __init__(self, bot):
         self.b = bot 


    @checks.dev()
    @client.command(enabled=True)
    async def debug(self,ctx):
        pv = ".".join(map(str, sys.version_info[:3]))
        e = discord.Embed(title=f'''Version: {conf.version}
Name: {conf.name}
Username: {self.b.user.name}
Prefix 1: {conf.prefix1}
Prefix 2: {conf.prefix2}
Testing Mode: {conf.test_mode}
Sharding: {conf.sharding}
Type Speed: {conf.type_speed}
Discord.py Version: {discord.__version__}
Python Version: {pv}
''',color=0x36393f)
        e.set_author(name=f"Hiya {ctx.author.name}!", icon_url=ctx.author.avatar_url)

        if ctx.guild.id in conf.w_tog_off:
            e2 = discord.Embed(title=f'''Does Guild use chat triggers: No
''',color=0x36393f)
        else:
            e2 = discord.Embed(title=f'''Does Guild use chat triggers: Yes
''',color=0x36393f)        

        if conf.sharding is True:
            e3 = discord.Embed(title=f'''Number of Shards: {len(self.b.shards)}
Total Guilds: {len(self.b.guilds)}
''',color=0x36393f)
        else:
            pass

        if not ctx.guild.id in conf.act2:
            e4 = discord.Embed(title=f'''Is Guild in ACT2: No
''',color=0x36393f)
        else:
            e4 = discord.Embed(title=f'''Is Guild in ACT2: Yes
''',color=0x36393f)


        e5 = discord.Embed(title=f'''Doki ID's:
Monika: {conf.monika_id}
Natsuki: {conf.natsuki_id}
Sayori: {conf.sayori_id}
Yuri: {conf.yuri_id}
MC: {conf.mc_id}
''',color=0x36393f)

        await ctx.send(embed=e)
        await ctx.send(embed=e2)
        if conf.sharding is True:
            await ctx.send(embed=e3)
        await ctx.send(embed=e4)
        await ctx.send(embed=e5)


def setup(bot):
    bot.add_cog(Debug(bot))
