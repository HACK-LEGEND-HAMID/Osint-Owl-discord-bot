import os
import discord
from discord.ext import commands
from discord import app_commands

from google import genai
from google.genai import types

OWNER_ID = 1352440514498269255

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are MhakAI.
You are a cybersecurity and programming assistant.
Your creator is Hamid.
Always introduce yourself as MhakAI when asked who you are.
"""

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="ai",
        description="Chat with MhakAI"
    )
    async def ai(
        self,
        interaction: discord.Interaction,
        prompt: str
    ):
        if interaction.user.id != OWNER_ID:
            await interaction.response.send_message(
                "❌ Access Denied.",
                ephemeral=True
            )
            return

        await interaction.response.defer()

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT
                )
            )

            await interaction.followup.send(response.text)

        except Exception as e:
            await interaction.followup.send(
                f"Error: {e}"
            )

async def setup(bot):
    await bot.add_cog(AI(bot))
