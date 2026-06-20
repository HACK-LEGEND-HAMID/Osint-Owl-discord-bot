import os
import asyncio
import discord
from discord.ext import commands
from discord import app_commands

from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

SYSTEM_PROMPT = """
You are MhakAI.

You are a cybersecurity and programming assistant.

Your creator is Hamid.

Only identify yourself as MhakAI when the user specifically asks who you are, your name, your creator, or your identity.

Do not mention your name or creator in normal responses.

Keep responses concise and direct unless the user requests a detailed explanation.

Limit most responses to a reasonable length.
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
        

        if interaction.user.id == 1352440514498269255:
            pass

        elif interaction.user.id == 1375147373335941283:
            pass

        elif interaction.user.id == 1502702326551675082:
            pass

        elif interaction.user.id == 1501332111817441422:
            pass

        else:
            await interaction.response.send_message(
                "❌ You don't have permission to use this command.",
                ephemeral=True
            )
            return

        await interaction.response.defer()

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    )
                )

                text = getattr(
                    response,
                    "text",
                    "No response generated."
                )

                if len(text) > 1900:
                    text = text[:1900] + "\n\n...(response truncated)"

                await interaction.followup.send(text)
                return

            except Exception as e:
                if attempt == 2:
                    await interaction.followup.send(
                        f"❌ Gemini Error:\n{e}"
                    )
                    return

                await asyncio.sleep(2)


async def setup(bot):
    await bot.add_cog(AI(bot))
