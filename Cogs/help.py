import discord, asyncio
import discord.ext.commands as client


class Help(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def help(self,ctx):
        if self.b.doki == "mc":
            embed = discord.Embed(title="I'm MC, I guess.", description="So somehow my non-existent .chr file was turned into a discord bot file, or whatever the hell it's called, anyways I'm here because Sayori dragged me here. I don't have any talents or anything so I don't know why I'm here.", color=int(self.b.config["mc"]["embed_color"], base=16))
            embed.add_field(name="mc_ask", value="You can ask me anything, I really don't care.", inline=False)
            embed.add_field(name="mc_feed", value="I'll eat really anything, but I'm fine with my own food.", inline=False)
            embed.add_field(name="mc_headpat", value="Useless command.", inline=False)
            embed.add_field(name="mc_hug", value="You can hug me, I don't know why but you can.", inline=False)
            embed.add_field(name="mc_invite", value="I don't know why but you can invite me to your server, if you want to.", inline=False)
            embed.add_field(name="mc_quote", value="You can make me say a quote from the game, I don't know why you would want to, but you can.", inline=False)
            embed.add_field(name="mc_tickle", value="I'm not tickleish, don't bother.", inline=False)
            embed.add_field(name="mc_changelog", value="Check out what's been changed!", inline=False)
            embed.add_field(name="mc_confess", value="Don't use this at all!", inline=False)
            embed.add_field(name="mc_rename", value="You can change my name (this only works on servers, and you must be able to manage nicknames).", inline=True)
            embed.add_field(name="@MC", value="So use this (I think) to get my attention. You can also type 'mc_commands' for a full list of what I can do (not much) or mc_invite if (for some reason) you want me on your server.", inline=True)
            embed.add_field(name="I think that's all about me.", value="Most likely Cole will make me do more things (sadly) if I’m buggy blame Monika and let Cole know if you have any questions I guess, I’m going back to sleep now~")
        elif self.b.doki == "monika":
            embed = discord.Embed(title="Greetings! I'm Monika!", description="Cole ~~finally~~ turned my .chr file into a .py file so I can join Discord! I'm not fully self-aware like I was in DDLC, but this will have to suffice!", color=int(self.b.config["monika"]["embed_color"], base=16))
            embed.add_field(name="m_ask", value="Use this to ask me a yes-or-no question. I'm admittedly not the smartest person ~~in the game~~ on Earth, but I'll try my hardest to answer correctly!", inline=True)
            embed.add_field(name="m_delete", value="Do you need something 'deleted' from your server? I'll be happy to help!", inline=True)
            embed.add_field(name="m_feed", value="Would you like to feed me something? You can with this command!", inline=True)
            embed.add_field(name="m_headpat", value="Ahaha! I don't understand the appeal of patting girls on the head, but I suppose I can figure it out...", inline=True)
            embed.add_field(name="m_hug", value="I'm always open to giving a hug to anyone who wants one! Or, let's be honest, even if they *don't* want one!", inline=True)
            embed.add_field(name="m_invite", value="Use this to invite me to your Discord server! I would certainly love to see if you have your own literature club!", inline=True)
            embed.add_field(name="m_quote", value="You can have me say a quote from the game if you so wish!", inline=False)
            embed.add_field(name="m_tickle", value="O-Oh! Well, I guess there are worse things to do to me than tickling!", inline=True)
            embed.add_field(name="m_changelog", value="Check out what's been changed!", inline=True)
            embed.add_field(name="@Monika", value="Use this to get my attention, if you want. You can even try to use certain words or phrases to get certain responses. But that doesn't mean I'll understand everything you say! Type 'm_phrases' for a full list!", inline=True)
            embed.add_field(name="I do believe that's it!", value="I'm still in very early stages of development, but if Cole was able to create the other girls quickly, I'm sure I'll be finished before you know it!")
        elif self.b.doki == "natsuki":
            embed = discord.Embed(title="Hey, it's me, Natsuki.", description="Freaking Cole decided to turn my .chr file into a file that lets me be on this Discord server. It's not like I'm here because I want to be or anything, you dummies! A-anyway, here are the things I can do:", color=int(self.b.config["natsuki"]["embed_color"], base=16))
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
            embed = discord.Embed(title="Hi! I'm Sayori!", description="Cole was kind enough to turn my .chr file into a file that can let me interact with you guys to a certain extent! My commands are as follows:", color=int(self.b.config["sayori"]["embed_color"], base=16))
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
        elif self.b.doki == "yuri":
            if ctx.guild is None:
                embed = create_embed()
            elif ctx.guild.id in self.b.act2:
                embed = discord.Embed(title="Hello. I'm Yuri.", description="My .chr file was converted by Cole, so now I can join your Discord server. I just know that being with you will be the best thing to ever happen to both of us, ahaha! Here are all the things we can do together:", color=int(self.b.config["yuri"]["embed_color"], base=16))
                embed.add_field(name="y_act1/y_act2", value="You can use this to toggle between my Act 1 personality and my Act 2 one. This can only be used by server administrators. Honestly, I love you either way, so I don't care which one I'm on!", inline=True)
                embed.add_field(name="y_act", value="You can use this to check what act I'm on!", inline=True)
                embed.add_field(name="y_ask", value="You can ask me a yes-or-no question if you'd like, and I'll try my hardest to answer it for you!", inline=True)
                embed.add_field(name="y_feed", value="You can use this to feed me any of emojis available. Any of them. *(Format like this: 'y_feed :emoji:')*", inline=True)
                embed.add_field(name="y_headpat", value="You can use this to pat me on the head.", inline=True)
                embed.add_field(name="y_hug", value="I-I'm not too much of a hugger, but if you want me to hug you, I'll happily do it. It would be the best thing to ever happen in my life!", inline=True)
                embed.add_field(name="y_invite", value="You can use this to have me give you the invite link to let me join other servers. But why would you want that when it can be just us forever?", inline=True)
                embed.add_field(name="y_quote", value="You can use this to have me say one of my quotes from Doki Doki Literature Club.", inline=True)
                embed.add_field(name="y_tickle", value="You can use this to tickle me, which is so hot and sexy...", inline=True)
                embed.add_field(name="y_changelog", value="Check out what's been changed!", inline=True)
                embed.add_field(name="I believe that's everything.", value="Cole says more features are coming soon, so until then, this will have to suffice. If he doesn't add new things soon, I'm afraid he might not be breathing for too much longer... Feel free to visit Cole's Support Server to let him know that I'm counting on him to make me do anything possible to spend time with you.")
            else:
                embed = create_embed()
        embed.set_footer(text="Support Server: https://discord.gg/QnzsG38")
        await ctx.send(embed=embed)

    # Creates help embed for Act 1 Yuri
    def create_embed():
        e = discord.Embed(title="H-Hello. I'm Yuri.", description="My .chr file was converted by Cole, so now I can join your Discord server. I-I hope I don't become an inconvenience to you... A-Anyway, here are the things I can do:", color=int(self.b.config["yuri"]["embed_color"], base=16))
        e.add_field(name="y_act1/y_act2", value="Y-You can use this to toggle my Act 1 and Act 2 personalities, b-but this can only be done by a server administrator... Uu, could you please keep me on Act 1, though? I-I'm not proud of how I behave in Act 2 mode...", inline=True)
        e.add_field(name="y_act", value="You can use this to check what act i'm on!", inline=True)
        e.add_field(name="y_ask", value="You can ask me a yes-or-no question if you'd like, but please don't be disappointed if I don't know the answer or even give an incorrect one...", inline=True)
        e.add_field(name="y_feed", value="You can use this to feed me any of the food emojis available. *(Format like this: 'y_feed :food_emoji:')*", inline=True)
        e.add_field(name="y_headpat", value="You can use this to pat me on the head.", inline=True)
        e.add_field(name="y_hug", value="I-I'm not too much of a hugger, but if you want me to hug you or someone else on the server, then I suppose I can do that. Simply leave it blank if you want me to hug you, or @mention someone immediately after to have me hug them.", inline=True)
        e.add_field(name="y_invite", value="Y-You can use this to have me post my invite link so I can visit other servers. A-Although, I don't see why anyone would want that. I'm so useless...", inline=True)
        e.add_field(name="y_quote", value="You can use this to have me say one of my quotes from Doki Doki Literature Club, although some of them, I'm not proud to admit that I said... Uu...", inline=True)
        e.add_field(name="y_tickle", value="You can use this to tickle me, although I should warn you that I tend to have embarassing laughs...", inline=True)
        e.add_field(name="y_changelog", value="Check out what's been changed!", inline=True)
        e.add_field(name="I believe that's everything.", value="Cole says more features are coming soon, so until then, this will have to suffice. I hope you enjoy my presence on your Discord server, and if you have any questions, comments, or suggestions, feel free to visit Cole's Support Server. Thank you.", inline=True)
        return e


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))
