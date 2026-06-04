import discord
from discord.ext import commands
from discord import app_commands
from cogs.media import EMOJIS

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="verify_user",
        description="Verify a user"
    )
    @app_commands.describe(
        user="User to verify",
        password="Verification password"
    )
    async def verify_user(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        password: str
    ):

        OWNER_ID = 1352440514498269255
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

        role = interaction.guild.get_role(
            VERIFIED_ROLE_ID
        )

        if role is None:
            await interaction.response.send_message(
                "❌ Verified role not found."
            )
            return

        await user.add_roles(role)

        await interaction.response.send_message(
            f'{EMOJIS["mhakverifiedbadge"]} {user.mention} has been verified and given the {role.mention} role!'
        )

async def setup(bot):
    await bot.add_cog(moderation(bot))
