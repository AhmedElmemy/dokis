import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType


class Ask(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def ask(self,ctx, arg1=None):
        if arg1 is None:
            if self.b.doki == "sayori":
                await ctx.send("I can't answer the question if you don't ask one, silly!")
            elif self.b.doki == "natsuki":
                await ctx.send("Hey! You wanted to ask me something so what is it?!")
            elif self.b.doki == "monika":
                await ctx.send("Ahaha! D-did you want to ask me something?")
            elif self.b.doki == "mc":
                await ctx.send("I can't answer a non-existent question.")
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    await ctx.send("Did you want to ask me something? S-sorry if i was bothering you! Uuu...")
                elif ctx.guild.id in self.b.act2:
                    await ctx.send("Ahaha... If you don't have a question, that's okay. I'd rather stare at you.")
                else:
                    await ctx.send("Did you want to ask me something? S-sorry if i was bothering you! Uuu...")
        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(int(self.b.config['type_speed']))
            if self.b.doki == "sayori":
                answer_list = ["Yes!", "No.", "Maybe.", "Possibly?", "Of course, silly!", "I'd say ask Monika, but she's busy being ~~a meanie~~ an amazing club president!", "I'd say ask Yuri, but she's a little shy at the moment.", "I'd say ask Natsuki, but she's busy baking some cookies for ~~me to steal~~ the club!", "You've got a better chance of having a happy ending in DDLC! Ehehe...~", "Maybe we should ask The Magic Conch, instead.", "As sure as I'm depressed!", "Not really.", "My Vice President Powers tell me yes!", "My Vice President Powers tell me no!", "My Vice President Powers tell me maybe!", "J-Just a little bit!"]
            elif self.b.doki == "natsuki":
                answer_list = ["Eh. Probably not.","I guess so.","How should I know, dummy?", "I don't know. Ask Monika if you want the answer that badly.", "No.","Pfft. In your dreams!", "Is manga literature?", "Yuri might know."]
            elif self.b.doki == "monika":
                answer_list = ["Yes!", "No!", "Ahaha! I-I don't really know, to be honest...", "As Club President, I say 'yes'!", "As Club President, I say 'no'!", "As Club President, I say 'maybe'!", "Uh... Well, uh... I think the Vice President would be better suited for this question!", "Y-Yuri's smart, right? I'm sure she can answer that!", "Maybe you can try asking Natsuki; she knows more than she lets on."]
            elif self.b.doki == "mc":
                answer_list = ["I don't know why you're asking me, go ask Sayori.", "Yes, I guess.", "No, I think; I don't care either way.", "Maybe? Monika would know.", "Yeh.", "No, just no."]
            elif self.b.doki == "yuri":
                if ctx.guild is None:
                    pass
                elif ctx.guild.id in self.b.act2:
                    answer_list = ["Yes.", "I don't know, and I don't care. I just want to look at you...", "No.", "Possibly, but who knows?", "Meet me in the closet and we'll find out... :kissing_closed_eyes:", "Ahaha! You're so silly to ask such a question!", "I'm not sure... I'll think about it while I'm touching myself to you tonight."]
                answer_list = ["Y-Yes.", "No...", "I'm not really sure.", "I don't believe so...", "I think that's a question best suited for Sayori.", "Perhaps Monika could be of better help?", "I-I don't know. I'm sorry...", "Natsuki might know.", "I believe so!"]
            await ctx.send(random.choice(answer_list))


def setup(bot):
    bot.add_cog(Ask(bot))
