import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Motivate(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def motivate(self,ctx, *, message=None): 
        member = ctx.message.content.split(" ")[0]
        if message is None: #No argument? Just assume it's you
            user = ctx.author
            motivate_list = [f"I believe in you {user.name}, you stupid sack of shit!", "C'mon, dummy! You can do it!", "*grabs shoulders* You've got this! I know you do!", "I'll bake you as many cupcakes as you want!", "You better do good or I'll shatter your shins!", "C'mon! Don't be a lazy goofball like Sayori!", "You better not act as dense as MC!", "DO IT! Just DO IT!!!", "Don't let your dreams be dreams!"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(int(self.b.config['type_speed']))  
            await ctx.send(random.choice(motivate_list))

        elif message == ('@everyone' or '@here'):
            await ctx.send("There is no way I'm going to motivate everyone here!")
            
        elif message == 'y_act' or message == 'y_act1' or message == 'y_act2':
            async with ctx.message.channel.typing():
                await asyncio.sleep(int(self.b.config['type_speed']))  
            await ctx.send("Nice try, Baka.")

        else: 
            motivate_list = [f"I believe in you {message}, you stupid sack of shit!", "C'mon, dummy! You can do it!", "*grabs shoulders* You've got this! I know you do!", "I'll bake you as many cupcakes as you want!", "You better do good or I'll shatter your shins!", "C'mon! Don't be a lazy goofball like Sayori!", "You better not act as dense as MC!", "DO IT! Just DO IT!!!", "Don't let your dreams be dreams!"]
            async with ctx.message.channel.typing():
                await asyncio.sleep(int(self.b.config['type_speed']))  
            await ctx.send(random.choice(motivate_list))


def setup(bot):
    bot.add_cog(Motivate(bot))
