import asyncio, discord, importlib, json, os, random, re, rstr, sqlite3, sre_yield, sys, traceback
from discord.ext import commands

try:
    dokiName = sys.argv[1].lower()
except:
    print("Please specify a doki (Monika, Natsuki, Sayori, Yuri) or MC.")
    quit()
try:
    test_mode = sys.argv[2] == '-test'
except:
    test_mode = False

config = json.loads(open("config.json", "r").read())

if not os.path.exists(dokiName) or config[dokiName] is None:
    print('No doki was found!')
    sys.exit(0)

class doki(commands.Bot if test_mode else commands.AutoShardedBot):
    
    def __init__(self):
        super().__init__(command_prefix=sre_yield.AllStrings(config[dokiName]["prefix"]), status=discord.Status.idle, activity=discord.Game(name="Starting Up..."))
        self.doki = dokiName
        self.test_mode = test_mode
        self.config = config
        self.w_tog_off = []

        # Exclusively for Yuri
        if dokiName == "yuri":
            self.act2 = []
        
        # Load universal command cogs.
        for file in os.listdir("Cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                if name == "checks":
                    pass
                else:
                    try:
                        self.load_extension(f"Cogs.{name}")
                        print(f"Loaded Cog: {name}")
                    except (discord.ClientException, ModuleNotFoundError):
                        print('Failed to load Cog: {name}')
                        print(traceback.format_exc())

        # Load character-specific command cogs.
        for file in os.listdir(f"{dokiName}/Cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.load_extension(f"{dokiName}.Cogs.{name}")
                    print(f"Loaded Cog: {name}")
                except (discord.ClientException, ModuleNotFoundError):
                    print('Failed to load Cog: {name}')
                    print(traceback.format_exc())

        # Load event cogs.
        for file in os.listdir(f"{dokiName}/Events"):
            if file.endswith(".py"):
                name = file[:-3]
                try:
                    self.load_extension(f"{dokiName}.Events.{name}")
                    print(f"Loaded Event: {name}")
                except (discord.ClientException, ModuleNotFoundError):
                    print('Failed to load Event: {name}')
                    print(traceback.format_exc())

    async def on_ready(self):
        print()
        print(f"[SUCCESS] Connected to Discord as: {self.user}")
        print(f"[INFO] Testing Mode: {'Enabled' if test_mode else 'Disabled'}")

        if test_mode:
            print(f"[WARNING] Sharding: Disabled")
        else:
            print("[INFO] Sharding: Enabled")
            print(f"[INFO] Using {len(self.shards)} shard(s)")

        print(f"[INFO] Character File: '{dokiName}.chr'")
        print(f"[INFO] Prefix Regex: '{config[dokiName]['prefix']}'")
        print(f"[INFO] I'm currently in [{len(self.guilds)}] server(s).")

        self.loop.create_task(self.status_task())

    async def status_task(self):
        while not self.is_closed():
            for game in config[dokiName]["playing"]:
                await self.change_presence(activity=discord.Game(name=game))
                await asyncio.sleep(900)

try:
    print(f"Loading {dokiName}.chr")
    client = doki()
    client.run(json.loads(open("tokens.json", "r").read())[dokiName])
except Exception as error:
    print(f"Could not run {dokiName}.chr!")
    print(traceback.format_exc())