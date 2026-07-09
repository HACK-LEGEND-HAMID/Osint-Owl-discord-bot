import discord
import aiohttp
import random
from discord.ext import commands
from discord import app_commands

EMOJIS = {
    "imposter": "<:killer:1510613232652648630>",
    "reddit": "<:NeonReddit:1510259794106122282>",
    "owl": "<:owl:1510610901517209712>",
    "anonymous": "<:anonymous:1510613189367304363>",
    "love": "<:love:1510613216642859148>",
    "florkangel": "<:florkangel:1511683579611054080>",
    "florkdevil": "<:florkdevil:1511683559763476550>",
    "flowerforyou": "<:flowersforyou:1511683533872304201>",
    "mhakverifiedbadge": "<:metaverifiedbadge:1511683495670317086>",
    "googleit": "<:googleit:1511683325826170991>",
    "alert": "<:alert:1511683305358102619>",
    "dragon": "<:dragon:1511680859336347788>",
    "snow-angel": "<:snowangel:1511680833033863179>",
    "kali-linux": "<:kali:1511680814969127028>",
    "macdonald": "<:mcdonalds:1511680794241007616>",
    "owner": "<:owner:1510613306199511191>",
}

class media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = None

    async def cog_load(self):
        self.session = aiohttp.ClientSession()

    async def emoji_autocomplete(self, interaction: discord.Interaction, current: str):
        return [
            app_commands.Choice(name=name, value=name)
            for name in EMOJIS.keys()
            if current.lower() in name.lower()
        ][:25]

    @app_commands.command(name="emoji", description="Send an emoji")
    @app_commands.autocomplete(name=emoji_autocomplete)
    async def emoji(self, interaction: discord.Interaction, name: str):
        await interaction.response.send_message(EMOJIS.get(name, "❌ Emoji not found"))

    async def fetch_quote(self):
        """Try 2 free APIs with proper headers"""
        apis = [
            {
                "url": "http://api.quotable.io/random",
                "parse": lambda d: {"quote": d['content'], "author": d['author']}
            },
            {
                "url": "https://zenquotes.io/api/random",
                "parse": lambda d: {"quote": d[0]['q'], "author": d[0]['a']}
            }
        ]
        
        headers = {"User-Agent": "DiscordBot/1.0"}
        random.shuffle(apis)

        for api in apis:
            try:
                async with self.session.get(api["url"], headers=headers, timeout=10) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return api["parse"](data)
            except Exception as e:
                print(f"API Error: {api['url']} -> {e}")
                continue
        return None

    @app_commands.command(name="quote", description="Get a random quote")
    async def quote(self, interaction: discord.Interaction):
        await interaction.response.defer()

        quote_data = await self.fetch_quote()

        if quote_data:
            embed = discord.Embed(
                description=f"*{quote_data['quote']}*",
                color=discord.Color.random()
            )
            embed.set_author(name=f"💬 {quote_data['author']}")
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("❌ Failed to fetch quote. Check terminal for errors.")

    async def cog_unload(self):
        if self.session:
            await self.session.close()

async def setup(bot):
    await bot.add_cog(media(bot))
