import discord, random, asyncio
import discord.ext.commands as client
from Cogs.config import conf


class Hug(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def hug(self,ctx, *, message=None):
        member = ctx.message.content.split(" ")[0]
        if message is None:
            user = ctx.author
            hug_list = [f"Uh, ok? *hugs <@{user.id}>*", f"I don't do hugs, <@{user.id}>", f"I mean, if you want. *hugs <@{user.id}>*", "No thanks, I'm fine.", f"If it makes you happy, then fine. *hugs <@{user.id}>*", "*runs away*"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        elif message == '@everyone' or message == '@here':
            await ctx.send("No.")
            
        elif message == 'f<@{self.b.user.id}>':
            hug_list = [f"...fine. *hugs myself*", "Well, if you say so... *hugs myself*", "*hugs myself* Huh. Now I see why you guys like my hugs so much."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))

        else:
            hug_list = [f"Uh, ok? *hugs {message}*", f"I don't do hugs, <@{ctx.author.id}>", f"I mean, if you want. *hugs {message}*", "No thanks, I'm fine.", f"If it makes you happy, then fine. *hugs {message}*","*runs away*"] 
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send(random.choice(hug_list))


def setup(bot):
    bot.add_cog(Hug(bot))
