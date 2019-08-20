import discord, asyncio
import discord.ext.commands as client


class Commands(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command(aliases=['phrases'])
    async def commands(self,ctx):
        if self.b.doki == "mc":
            e = discord.Embed(title="Phrases!", description="Here are all the commands/words/phrases you can use when you @mention me, although I hope you don't do this.", color=self.b.config['mc']['embed_color'])
            e.add_field(name="Hi, Hello", value="Nothing wrong with a greeting, even when I don't want to do it.", inline=True)
            e.add_field(name="Test", value="Just to see if I'm fine (which I usually am).", inline=True)
            e.add_field(name="I love you, ILY", value="Uhhhhh...", inline=False)
            e.add_field(name="@mention loves you", value="No no no no no no no", inline=True)
            e.add_field(name="Goodnight, Good night, Good morning", value="While not required, it's still nice to recieve a message like this when you wake up/go to sleep.", inline=True)
            e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="No, I'm not.", inline=True)
            e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="In case you ever do something wrong.", inline=True)
        elif self.b.doki == "monika":
            e = discord.Embed(title="Phrases!", description="Here are all the words/phrases you can use when you @mention me! Though it's ***VERY*** important that the @mention is at the very beginning!", color=self.b.config['monika']['embed_color'])
            e.add_field(name="Hi, Hello", value="It's always good to greet your Club President~!", inline=True)
            e.add_field(name="Test", value="This is to see if I am working properly ~~as a Discord bot~~.", inline=False)
            e.add_field(name="I love you, ILY", value="It seems unprofessional to do this, but if you must, feel free to tell if you like! ~~I love you too, by the way...~~", inline=True)
            e.add_field(name="@mention loves you", value="Does someone else in the server loves me? Let me know by formatting the message like this: ***@Monika @mention loves you***", inline=True)
            e.add_field(name="Goodnight, Good night, Good morning", value="While not required, it's still nice to recieve a message like this when you wake up/go to sleep.", inline=True)
            e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="This seems very unprofessional, but I'll take the compliment anyway!", inline=True)
            e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="Apologizing is the right thing to do when you did something wrong.", inline=True)
            e.add_field(name="I'm (sick|puking|not feeling (good|great))", value="I hope you get well soon, then!", inline=True)
        elif self.b.doki == "natsuki":
            e = discord.Embed(title="Phrases!", description="Here are all the words/phrases you can use when you @mention me! You don't have to do this, but if you do, @mention me at the very beginning!", color=self.b.config['natsuki']['embed_color'])
            e.add_field(name="Hi, Hello", value="I-It's not like you have to greet me or anything!", inline=True)
            e.add_field(name="Test", value="I'm usually working fine, you dummy!", inline=False)
            e.add_field(name="I love you, ILY", value="R-Really? You, out of all people, actually l-love me?!", inline=True)
            e.add_field(name="@mention loves you", value="Someone else on this server l-loves me? Just make sure you tell me like this: ***@Natsuki @mention loves you***", inline=True)
            e.add_field(name="Goodnight, Good night, Good morning", value="You definitely don't need to bother me in the morning or at night! Y-You don't!", inline=True)
            e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="***WHAT? N-NO, I'M NOT!!!***", inline=True)
            e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="Well, at least you can acknowledge that you were a jerk!", inline=True)
            e.add_field(name="I'm (sick|puking|not feeling (good|great))", value="I hope you get well, then! I-It's not like I care or anything...", inline=True)
        elif self.b.doki == "sayori":
            e = discord.Embed(title="Phrases!", description="Here are all the words/phrases you can use when you @mention me! Though it's ***VERY*** important that the @mention is at the very beginning!", color=self.b.config['sayori']['embed_color'])
            e.add_field(name="Hi, Hello", value="Nothing wrong with a simple hello every now and then, right?", inline=True)
            e.add_field(name="Test", value="Just to see if I'm working properly!", inline=True)
            e.add_field(name="I love you, ILY", value="Even though I'm not worthy of being loved, you're still free to tell me that you love me if you'd like! Ehehe...", inline=True)
            e.add_field(name="@mention loves you", value="Want to let me know if someone in the server loves me? Let me know by formatting the message like this: ***@Sayori @mention loves you***", inline=True)
            e.add_field(name="Goodnight, Good night, Good morning", value="While not required, it's still nice to receive a message like this when you wake up/go to sleep.", inline=True)
            e.add_field(name="@mention is a meanie, @mention is being a meanie", value="Someone in the server being a meanie? Use this to let me know so I can call them out on it! (Full message should look like this: ***@Sayori @mention is (being) a meanie***)", inline=True)
            e.add_field(name="You are cute, You're cute, You are so cute, You're so cute, You are beautiful, You're beautiful, You are so beautiful, You're so beautiful, You are pretty, You're pretty, You are so pretty, You're so pretty", value="What? A girl likes to be complimented!", inline=True)
            e.add_field(name="Sorry, Apologize (as long as the word is in there somewhere)", value="Did you accidentally hurt me? Feel free to tell me that you're sorry! It's the right thing to do.", inline=True)
            e.add_field(name="I'm (sick|puking|not feeling (good|great))", value="Oh my are you sick? Well I'll wish you luck to get better then!", inline=True)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Commands(bot))
