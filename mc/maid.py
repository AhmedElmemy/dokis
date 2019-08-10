import discord, os, traceback, sys, json, asyncio
from discord.ext import commands
from Cogs.config import conf


config = json.loads(open('../config.json', 'r').read())

if "true" in config['test_mode'].lower():
    print('''---------------------Testing Mode--------------------- 
Warning!

You are currently running the Pythonic Doki Bot's in testing mode!
Please disable testing mode before launching this code. 
If you are unsure how to turn testing mode off:

1. Go to the config
2. Find "test_mode ="
3. Change "False" to "True"
---------------------Testing Mode--------------------- \n''')
    bot = commands.Bot
else:
    bot = commands.AutoShardedBot

async def prefix(bot, message):
  return [conf.prefix1, conf.prefix2]

class maid(bot):
    
    def __init__(self):
        super().__init__(command_prefix=prefix, status=discord.Status.idle, activity=discord.Game(name="Starting Up..."))

        # Load command cogs.
        for file in os.listdir("Cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                if name == "config" or name == "checks":
                    pass
                else:
                    try:
                        self.load_extension(f"Cogs.{name}")
                        print(f"Loaded {name}")
                    except (discord.ClientException, ModuleNotFoundError):
                        print('Failed to load Cog {name}')
                        print(traceback.format_exc())

        # Load event cogs.
        for file in os.listdir("Events"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.load_extension(f"Events.{name}")
                    print(f"Loaded {name}")
                except (discord.ClientException, ModuleNotFoundError):
                    print('Failed to load Cog {name}')
                    print(traceback.format_exc())

    async def on_ready(self):
        print("\n")
        print(f"[SUCCESS] Connected to Discord as: {self.user}")

        if conf.sharding is False:
            print(f"[WARNING] Sharding: Disabled")
        else:
            print("[INFO] Sharding: Enabled")
            print(f"[INFO] Using {len(self.shards)} shard(s)")

        print(f"[INFO] Config name: '{conf.name}'")
        print(f"[INFO] Default Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'")
        print(f"[INFO] I'm currently in [{len(self.guilds)}] server(s).")

        self.loop.create_task(self.status_task())

    async def status_task(self):
        while not self.is_closed():
            for list in conf.playing_msg:
                await self.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)


client = maid()
client.run(config['mc_token'])
