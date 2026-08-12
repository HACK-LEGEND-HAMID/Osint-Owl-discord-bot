import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.default()
        )

    async def setup_hook(self):
        await self.load_extension("cogs.media")
        await self.load_extension("cogs.moderation")
        await self.load_extension("cogs.general_osint")
        await self.load_extension("cogs.mhakai")
        await self.load_extension("cogs.lua_res")
        await self.load_extension("cogs.python_res")
        await self.load_extension("cogs.ctf")
        await self.load_extension("cogs.game")
        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

bot.run(os.getenv("TOKEN"))
