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



@tree.command(
    name="verify_user",
    description="Verify a user"
)
@app_commands.describe(
    user="User to verify",
    password="Verification password"
)
async def verify_user(
    interaction: discord.Interaction,
    user: discord.Member,
    password: str
):

    OWNER_ID =  1352440514498269255
    VERIFY_PASSWORD = "MySecretPassword123"
    VERIFIED_ROLE_ID = 1511721117621026846

    if interaction.user.id != OWNER_ID:
        await interaction.response.send_message(
            "❌ Only the Owner can Use This Command."
        )
        return

    if password != VERIFY_PASSWORD:
        await interaction.response.send_message(
            "❌ Invalid password."
        )
        return

    role = interaction.guild.get_role(VERIFIED_ROLE_ID)

    if role is None:
        await interaction.response.send_message(
            "❌ Verified role not found."
        )
        return

    await user.add_roles(role)

    await interaction.response.send_message(
            f"{EMOJIS.get("mhakverifiedbadge")}  {user.mention} has been verified and given the {role.mention} role!"
)
  
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
