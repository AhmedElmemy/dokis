import discord, asyncio
import discord.ext.commands as client


class Invite(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def invite(self,ctx):
        if self.b.doki == "mc":
            e = discord.Embed(title="My invite link...", description="Here's the link you can use to invite me to your server. Why you would, I don't know.", color=int(self.b.config["mc"]["embed_color"], base=16))
            e.add_field(name="Enjoy!", value="[Click here to invite me!](https://discordbots.org/bot/596407346176065552)", inline=True)
        elif self.b.doki == "monika":
            e = discord.Embed(title="My invite link!", description="Oh, you would like to add me to a new server? You can get my link below!", color=int(self.b.config["monika"]["embed_color"], base=16))
            e.add_field(name="Here it is!", value="[Click here to invite me!](https://discordbots.org/bot/436351740787294208)", inline=True)
        elif self.b.doki == "natsuki":
            e = discord.Embed(title="My invite link!", description="F-fine! I guess I can join someone else's server, too... but I probably won't like it!", color=int(self.b.config["natsuki"]["embed_color"], base=16))
            e.add_field(name="Here goes...", value="[Click here to invite me!](https://discordbots.org/bot/433834936450023424)", inline=True)
        elif self.b.doki == "sayori":
            e = discord.Embed(title="My invite link!", description="Here's the server invite link so anyone else here can invite me to their server!", color=int(self.b.config["sayori"]["embed_color"], base=16))
            e.add_field(name="Enjoy!", value="[Click here to invite me!](https://discordbots.org/bot/425696108455657472)", inline=True)
        elif self.b.doki == "yuri":
            if ctx.guild is None:
                e = create_embed()
            elif ctx.guild.id in self.b.act2:
                e = discord.Embed(title="My invite link!", description="Ahahaha! I suppose I could visit other servers, but you're all I need!", color=int(self.b.config["yuri"]["embed_color"], base=16))
                e.add_field(name="Still, here you are!", value="[Click here to invite me!](https://discordbots.org/bot/436350586670153730)", inline=True)
            else:
                e = create_embed()
        await ctx.send(embed=e)

    def create_embed():
        e = discord.Embed(title="My invite link!", description="Uuu, I don't know about this. W-What if they don't like me?", color=int(self.b.config["yuri"]["embed_color"], base=16))
        e.add_field(name="O-Oh, well... Here goes nothing...", value="[Click here to invite me!](https://discordbots.org/bot/436350586670153730)", inline=True)
        return e


def setup(bot):
    bot.add_cog(Invite(bot))
