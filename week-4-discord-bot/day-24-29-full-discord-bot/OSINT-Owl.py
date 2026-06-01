import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ Logged in as {bot.user}")

EMOJIS = {
    "imposter": "<:killer:1510613232652648630>",
    "reddit": "<:NeonReddit:1510259794106122282>",
    "owl": "<:owl:1510610901517209712>",
    "anonymous": "<:anonymous:1510613189367304363>",
    "love": "<:love:1510613216642859148>",

}

async def emoji_autocomplete(
    interaction: discord.Interaction,
    current: str
):
    return [
        app_commands.Choice(name=name, value=name)
        for name in EMOJIS.keys()
        if current.lower() in name.lower()
    ][:25]

@tree.command(name="emoji", description="Send an emoji")
@app_commands.autocomplete(name=emoji_autocomplete)
async def emoji(interaction: discord.Interaction, name: str):

    await interaction.response.send_message(
        EMOJIS.get(name, "❌ Emoji not found")
    )
  
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
