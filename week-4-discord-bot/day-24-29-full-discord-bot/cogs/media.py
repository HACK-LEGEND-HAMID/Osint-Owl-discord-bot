import discord
from discord.ext import commands
from discord import app_commands

EMOJIS = {
    "imposter": "<:killer:1510613232652648630>",
    "reddit": "<:NeonReddit:1510259794106122282>",
    "owl": "<:owl:1510610901517209712>",
    "anonymous": "<:anonymous:1510613189367304363>",
    "love": "<:love:1510613216642859148>",
    "florkangel":"<:florkangel:1511683579611054080>",
    "florkdevil":"<:florkdevil:1511683559763476550>",
    "flowerforyou":"<:flowersforyou:1511683533872304201>",
    "mhakverifiedbadge":"<:metaverifiedbadge:1511683495670317086>",
    "googleit":"<:googleit:1511683325826170991>",
    "alert":"<:alert:1511683305358102619>",
    "dragon":"<:dragon:1511680859336347788>",
    "snow-angel":"<:snowangel:1511680833033863179>",
    "kali-linux":"<:kali:1511680814969127028>",
    "macdonald":"<:mcdonalds:1511680794241007616>",
    "owner":"<:owner:1510613306199511191>",
}

class media(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def emoji_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str
    ):
        return [
            app_commands.Choice(name=name, value=name)
            for name in EMOJIS.keys()
            if current.lower() in name.lower()
        ][:25]

    @app_commands.command(
        name="emoji",
        description="Send an emoji"
    )
    @app_commands.autocomplete(name=emoji_autocomplete)
    async def emoji(
        self,
        interaction: discord.Interaction,
        name: str
    ):
        await interaction.response.send_message(
            EMOJIS.get(name, "❌ Emoji not found")
        )

async def setup(bot):
    await bot.add_cog(media(bot))
