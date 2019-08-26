import discord, random, asyncio
import discord.ext.commands as client


class Quotes(client.Cog):

    def __init__(self, bot):
         self.b = bot

    @client.command()
    async def quote(self,ctx):
        # TODO: Change quotes for MC. These ones are all Sayori's.
        if self.b.doki == "mc":
            quote_list = ["I want breakfast.", "AAAAAaaaaAAAAAAAAHH!!!!", "get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head", "I made eggs and toast!", "It's bad to skip breakfast! I get all cranky...", "I was playing with the crayons and smacked my forehead into the shelf!", "Yuri's boobs are just as they've always been! Big and beautiful!", "I did something bad, and now I have to accept the revolution!", "This isn't the napping club!", "I'm fine with--looking like a unicorn--", "So, if I keep it unbuttoned then I won't get a boyfriend, right?"]
        elif self.b.doki == "monika":
            quote_list = ["As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!", "I'm confident that we can all really grow this club before we graduate!", "Then that makes it official! Welcome to the Literature Club!", "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom.", "I guess you could say that I had some kind of epiphany recently. It's been influencing my poems a bit.", "...That's my advice for today! Thanks for listening~", "Wait...is this tip even about writing? What am I even talking about? Ahaha!", "Humans aren't two-dimensional creatures. I think you'd know that better than anyone.", "Also, that joke makes no sense in translation!", "And I also care about the well-being of my club members, you know?", "Have you thought that maybe you've always seen her as so cheerful because that's just how she is when she's around you?", "C-Catchphrase? I don't have a catchphrase...", "Yay, you picked me!", "You kind of left her hanging this morning, you know?", "Don't worry. I probably know a lot more than you think."]
        elif self.b.doki == "natsuki":
            quote_list = ["MANGA IS LITERATURE!", "I'M NOT CUTE!", "Well, you know what?! I wasn't the one whose boobs magically grew a size bigger as soon as MC started showing up!!", "Whoa, be careful or you might cut yourself on that edge, Yuri. Oh, my bad... You already do, don't you?", "Freaking Monika!", "***fucking monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm***", "You really shouldn't do that kind of thing to girls...unless you really like them...", "And just because I don't have a mature and sexy figure like Yuri doesn't mean you should treat me like--", "You really need to...beat...the crap out of it!", "If you really just came for the cupcakes, I would be super pissed."]
        elif self.b.doki == "sayori":
            quote_list = ["I want breakfast.", "AAAAAaaaaAAAAAAAAHH!!!!", "get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head get out of my head", "I made eggs and toast!", "It's bad to skip breakfast! I get all cranky...", "I was playing with the crayons and smacked my forehead into the shelf!", "Yuri's boobs are just as they've always been! Big and beautiful!", "I did something bad, and now I have to accept the revolution!", "This isn't the napping club!", "I'm fine with--looking like a unicorn--", "So, if I keep it unbuttoned then I won't get a boyfriend, right?"]
        elif self.b.doki == "yuri":
            quote_list = ["Here's a suggestion. Have you considered killing yourself? It would be beneficial to your mental health.", "After all, doesn't a hot cup of tea help you enjoy a good book?", "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?", "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment.", "Monika, please mind your own business for once. Or do you want to tell me there's something wrong with helping involve MC in club activities?", "Yes! I have terrible reading posture! So that's why we should sit on the floor.", "The thing is, I'm kind of into knives... They're just...so pretty...", "Just...for a little longer. It feels really nice...", "Sorry that my lifestyle is too much for someone of your mental age to comprehend!", "D-Did you just accuse me of cutting myself?? What the fuck is wrong with your head?!", "I love you so much that I even touch myself with the pen I stole from you.", "I just want to pull your skin open and crawl inside of you.", "Stagnating air is common foreshadowing that something terrible is about to happen..."]
        async with ctx.message.channel.typing():
            await asyncio.sleep(int(self.b.config['type_speed']))
        await ctx.send(random.choice(quote_list))


def setup(bot):
    bot.add_cog(Quotes(bot))
