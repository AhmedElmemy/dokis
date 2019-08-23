import discord, asyncio
import discord.ext.commands as client


class Help(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def help(self,ctx):
        if self.b.doki == "mc":
            embed = discord.Embed(title="I'm MC, I guess.", description="So somehow my non-existent .chr file was turned into a discord bot file, or whatever the hell it's called, anyways I'm here because Sayori dragged me here. I don't have any talents or anything so I don't know why I'm here.", color=self.b.config[self.b.doki]['embed_color'])
            embed.add_field(name="mc_ask", value="You can ask me anything, I really don't care.", inline=False)
            embed.add_field(name="mc_feed", value="I'll eat really anything, but I'm fine with my own food.", inline=False)
            embed.add_field(name="mc_headpat", value="Useless command.", inline=False)
            embed.add_field(name="mc_hug", value="You can hug me, I don't know why but you can.", inline=False)
            embed.add_field(name="mc_invite", value="I don't know why but you can invite me to your server, if you want to.", inline=False)
            embed.add_field(name="mc_quote", value="You can make me say a quote from the game, I don't know why you would want to, but you can.", inline=False)
            embed.add_field(name="mc_tickle", value="I'm not tickleish, don't bother.", inline=False)
            embed.add_field(name="mc_changelog", value="Check out what's been changed!", inline=False)
            embed.add_field(name="mc_confess", value="Don't use this at all!", inline=False)
            embed.add_field(name="mc_rename", value="You can change my name (note, this only for the server and you must have manage nicknames or administrator permissions)", inline=True)
            embed.add_field(name="@MC", value="So use this (I think) to get my attention. You can also type 'mc_commands' for a full list of what I can do (not much) or mc_invite if for some reason you want me on your server.", inline=True)
            embed.add_field(name="I think that's all about me.", value="Most likely Cole will make me do more things (sadly) if I’m buggy blame Monika and let Cole know if you have any questions I guess, I’m going back to sleep now~")
        elif self.b.doki == "monika":
            embed = discord.Embed(title="Greetings! I'm Monika!", description="Cole ~~finally~~ turned my .chr file into a .py file so I can join Discord! I'm not fully self-aware like I was in DDLC, but this will have to suffice!", color=0x12ba01)
            embed.add_field(name="m_ask", value="Use this to ask me a yes-or-no question. I'm admittedly not the smartest person ~~in the game~~ on Earth, but I'll try my hardest to answer correctly!", inline=True)
            embed.add_field(name="m_delete", value="Do you need something 'deleted' from your server? I'll be happy to help!", inline=True)
            embed.add_field(name="m_feed", value="Would you like to feed me something? You can with this command!", inline=True)
            embed.add_field(name="m_headpat", value="Ahaha! I don't understand the appeal of patting girls on the head, but I suppose I can figure it out...", inline=True)
            embed.add_field(name="m_hug", value="I'm always open to giving a hug to anyone who wants one! Or, let's be honest, even if they *don't* want one!", inline=True)
            embed.add_field(name="m_tickle", value="O-Oh! Well, I guess there are worse things to do to me than tickling!", inline=True)
            embed.add_field(name="m_changelog", value="Check out what's been changed!", inline=True)
            embed.add_field(name="@Monika", value="Use this to get my attention, if you want. You can even try to use certain words or phrases to get certain responses. But that doesn't mean I'll understand everything you say! Type 'm_phrases' for a full list!", inline=True)
            embed.add_field(name="I do believe that's it!", value="I'm still in very early stages of development, but if Cole was able to create the other girls quickly, I'm sure I'll be finished before you know it!")
        elif self.b.doki == "natsuki":
            embed = discord.Embed(title="Hey, it's me, Natsuki.", description="Freaking Cole decided to turn my .chr file into a file that lets me be on this Discord server. It's not like I'm here because I want to be or anything, you dummies! A-anyway, here are the things I can do:", color=conf.norm)
            embed.add_field(name="n_ask", value="You can ask me any yes-or-no question with this. But don't get mad if I don't know the answer or if I give the wrong answer!", inline=True)
            embed.add_field(name="n_feed", value="Y-you don't have to or anything, but I guess you could feed me some food i-if you really wanted to... *(Format like this: 'n_feed :food_emoji:')*", inline=True)
            embed.add_field(name="n_headpat", value="You can use this to pat me on the head, but why any normal person would want to, I have no clue...", inline=True)
            embed.add_field(name="n_hug", value="Ugh. Hugs are gross, but if you want me to hug you or anyone on the server, I guess I can do that for you... Just leave it blank if you want me to hug you or @mention someone to have me hug them. *(Format like this: n_hug @mention)*", inline=True)
            embed.add_field(name="n_invite", value="You can use this to show the link to invite me to other servers. But don't think that I'll enjoy it, you dummy!", inline=True)
            embed.add_field(name="n_motivate", value="I-it's not like I want to, but if you need motivation or encouragement, I'll try to help you out, I guess.", inline=True)
            embed.add_field(name="n_quote", value="You can use this to make me say one of my quotes from the game.", inline=True)
            embed.add_field(name="n_recipe", value="Do you like baking, like me? Well, I've got a few recipes in my cookbook; feel free to check them out!", inline=True)
            embed.add_field(name="n_tickle", value="You can use this to... TICKLE ME?? Oh, don't you dare use that unless you want a trip to the hospital!", inline=True)
            embed.add_field(name="n_changelog", value="Check out what's been changed!", inline=True)
            embed.add_field(name="@Natsuki", value="Use this to get my attention, if you want. You can even try to use certain words or phrases to get certain responses. But that doesn't mean I'll understand everything you say! Type 'n_phrases' for a full list!", inline=True)
            embed.add_field(name="I guess that's it...", value="Cole will make me do more stuff soon, but I'm not looking forward to it! If you want, you can go visit his Support Server and give him a piece of my mind! Anyway, see you later, ~~bakas~~ everyone!")
        elif self.b.doki == "sayori":
            embed = discord.Embed(title="Hi! I'm Sayori!", description="Cole was kind enough to turn my .chr file into a file that can let me interact with you guys to a certain extent! My commands are as follows:", color=conf.norm)
            embed.add_field(name="s_ask", value="Use this to ask me a yes-or-no question and receive an answer! Will I always be correct? Probably not, but my answers could yield some silly results!~", inline=True)
            embed.add_field(name="s_feed", value="Use this to feed me any of the foods available in the 'food' section of the Discord Emojis! Don't worry, I have a big stomach, so you can feed me as much as you want! *(Format like this: s_feed :food_emoji:)*", inline=True)
            embed.add_field(name="s_headpat", value="Use this to pat me on the head! :grin:", inline=True)
            embed.add_field(name="s_hug", value="Use this to have me hug someone! Leave it blank to have me hug you, or mention someone to have me hug them! *(Format like this: s_hug @mention)*", inline=True)
            embed.add_field(name="s_invite", value="Use this to put my Discord invite link in the chat so anyone can invite me to their own server!", inline=True)
            embed.add_field(name="s_joke", value="Use this to have me tell a random joke!", inline=True)
            embed.add_field(name="s_lifeline", value="I-Is someone on the server talking about ending their life...? Use this to pull up the National Suicide Prevention Lifeline. It doesn't really guarantee that they'll call it, but at least it's something you can do to try and help!", inline=True)
            embed.add_field(name="s_poems", value="Use this to read one of the poems from Doki Doki Literature Club!", inline=True)
            embed.add_field(name="s_quote", value="Use this to have me say one of my quotes from the game!", inline=True)
            embed.add_field(name="s_swear", value="Use this to have me swear! Why you would want me to, I'm not sure, but the option is there!", inline=True)
            embed.add_field(name="s_tickle", value="Use this to make me laugh!", inline=True)
            embed.add_field(name="s_changelog", value="Check out what's been changed!", inline=True)
            embed.add_field(name="@Sayori", value="Use this to either get my attention or to use special 'trigger words/phrases' to get certain responses out of me! Type 's_phrases' or `s_commands` for a full list!", inline=True)
            embed.add_field(name="And that's about it!", value="I'm sure Cole will add more stuff for me to do soon, but for now, I hope you enjoy my presence on the server! If you have any questions, comments, or bugs, let Cole know! Oh, and please don't be a meanie :unamused:. That's all for now. Bye!~")
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
