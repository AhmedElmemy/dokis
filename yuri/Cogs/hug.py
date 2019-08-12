import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Hug(client.Cog):

    def __init__(self, bot):
         self.b = bot
         self.hug_list = ["Y-you want me to hug you? Well, o-okay, I guess I can do that for you... *hugs %s*", "Just let me know if this is too much for you... *hugs %s*", "*hugs %s* Mmm... this feels nice... ***OH!*** I-I'm sorry, I didn't mean for that to sound weird!"]
         self.selfhug_list = ["What? O-Okay, I suppose... *hugs myself*", "*hugs myself* Oh, dear, this must look so embarassing! Uuuu...!"]
         self.act2_hug_list = ["*hugs %s* Ahaha... I could hug you forever...!", "Oh, you have no idea how long I've been waiting for you to say that!! *hugs %s*", "*hugs %s* Mmm... You smell so wonderful! I wish I could smell this smell forever!", "Uhuhu... You can even grab my ass while we hug if you wanted. I don't mind ;) *hugs %s*", f"*hugs %s* Oh, you're pressing hard against my chest. I must say, I really, really love it!"]

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def hug(self,ctx, *, message=None):
        if message == ("@everyone" or "@here"):
            await ctx.send("I'm not getting everyone's attention.")
            return

        if ctx.guild is None: # Runs in direct messages. Always do Act 1.
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if message is None: #No argument? Just assume it's you
                user = ctx.author
                await ctx.send(random.choice(self.hug_list) % (f"<@{user.id}>"))
            
            elif message.lower() == (f'<@{self.b.user.id}>' or "yuri" or "yourself"): # Oh no it's me!
                await ctx.send(random.choice(self.selfhug_list))

            else: # Argument, okay let's spit whatever the user just said
                async with ctx.message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await ctx.send(random.choice(self.hug_list) % (message))

        else: # Runs in guilds.
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            if message is None: #No argument? Just assume it's you
                user = ctx.author
                if ctx.guild.id not in conf.act2:
                    await ctx.send(random.choice(self.hug_list) % (f"<@{user.id}>"))
                else:
                   await ctx.send(random.choice(self.act2_hug_list) % (f"<@{user.id}>"))
            
            elif message.lower() == (f'<@{self.b.user.id}>' or "yuri" or "yourself"): # Oh no it's me!
                if ctx.guild.id not in conf.act2:
                    await ctx.send(random.choice(self.selfhug_list))
                else:
                    await ctx.send("But I don't ***want*** to hug myself! I want to hug ***YOU!!!***")

            elif ctx.guild.id in conf.act2 and message.lower() == (f"<@{conf.mc_id}>" or "mc"):
                await ctx.send(f"Hey <@{conf.mc_id}>, get your sexy body over here and fuck me~")

            else: # Argument, okay let's spit whatever the user just said
                if ctx.guild.id not in conf.act2:
                    await ctx.send(random.choice(self.hug_list) % (message))
                else:
                    await ctx.send("No. I refuse to hug anyone other than you.")

        
def setup(bot):
    bot.add_cog(Hug(bot))
