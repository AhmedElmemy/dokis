import discord, asyncio
import discord.ext.commands as client


class toggle(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    @client.has_permissions(manage_messages=True)
    @client.guild_only()
    async def toggle(self,ctx):
        if ctx.guild.id not in self.b.w_tog_off: # Disable chat triggers.
            self.b.w_tog_off.insert(0, ctx.guild.id)
            if self.b.doki == "mc":
                await ctx.send("I won't react to triggers in chat anymore.")
            elif self.b.doki == "monika":
                await ctx.send("Ok, I guess you don't want to hear from me.")
            elif self.b.doki == "natsuki":
                await ctx.send("Fine, I won't react to chat triggers.")
            elif self.b.doki == "sayori":
                await ctx.send("Okay, I won't react to the triggers in chat!")
        else: # Enables chat triggers.
            self.b.w_tog_off.remove(ctx.guild.id)
            if self.b.doki == "mc":
                await ctx.send("Fine, I'll start reacting to triggers again.")
            elif self.b.doki == "monika":
                await ctx.send("Ok, I guess you do want to hear from me.")
            elif self.b.doki == "natsuki":
                await ctx.send("Fine, I'll react to chat triggers.")
            elif self.b.doki == "sayori":
                await ctx.send("Okay, I'll react to the triggers in chat!")


def setup(bot):
    bot.add_cog(toggle(bot))
