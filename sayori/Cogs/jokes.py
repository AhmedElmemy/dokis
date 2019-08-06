import discord, random, asyncio
import discord.ext.commands as client
from discord.ext.commands.cooldowns import BucketType
from Cogs.config import conf


class Jokes(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    @client.cooldown(1, 7, BucketType.user)
    async def joke(self,ctx): 
        joke_list = ["What do you call a mix between a fish and an elephant? Swimming trunks!", "I was going to tell a joke about a skunk, but, honestly, it really stinks.", "Why did the rooster cross the road? To prove he wasn't a chicken!", "Why did the golfer wear two pairs of pants? In case he got a hole in one!", "I have severe depression. That's not a joke, it's a cry for help.", "My life. Ehehe...~", "What do you get when you cross an author and an alcoholic? Ernest Hemmingway!", "What do you call fake spaghetti? An im-pasta!", "Why don't cannibals eat clowns? Because they taste funny...", "What do you call a bird that sticks to everything? A vel-crow!", "What do you call a sleepwalking nun? A Roamin' Catholic!", "What's brown and sticky? A stick!", "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels.", "How many tickles does it take to make an octopus laugh? Ten tickles!", "Why do stadiums get hot after games? All the fans left!", "What do attorneys wear to court? Lawsuits!", "Why are there gates around cemeteries? Everyone is dying to get in!", "Why did the baby strawberry cry? His parents were in a jam!", "I was gonna tell a joke about a broken pencil, but it's pointless.", "The past, present, and future walk into a bar. It was tense.", "How do you comfort the Grammar Police? \"There, they're, their...\"", "Is there a word in the English language that uses all 5 vowels, as well as 'y'? Unquestionably!", "Once, I was spacing out in class and my English teacher asked me to name two pronouns. Not sure who she was talking to, I replied, \"Who, me?\"", "Why do writers feel so cold? They're surrounded by drafts!", "A man went into a library and asked for a book on how to commit suicide. The librarian replies, \"Why would I give you that? You won't return it!\"", "\"I'm sorry\" and \"I apologize\" mean the same thing. Unless you're at a funeral.", "A dyslexic man walks into a bra..."]
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(joke_list))


def setup(bot):
    bot.add_cog(Jokes(bot))
