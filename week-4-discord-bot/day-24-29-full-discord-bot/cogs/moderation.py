import discord
from discord.ext import commands
from discord import app_commands
from datetime import timedelta
from cogs.media import EMOJIS

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
            name="ban",
            description="Ban a user from your server"
            )
    @app_commands.default_permissions(
            ban_members=True
            )
    async def ban(
              self,
              interaction:discord.Interaction,
              user: discord.Member,
              reason:str="No Reason Provided"):
        try:
            await user.send(f"You were banned from{interaction.guild.name}\nReason:{reason}")
        except:
            pass

        await user.ban(reason=reason)
 
        await interaction.response.send_message(
       f"{user.mention} banned \nReason:{reason}"
            )
    @app_commands.command(
            name="kick",
            description="Kick a user from your server"
            )
    
    @app_commands.default_permissions(
            kick_members=True
            )
    async def kick(
            self,
            interaction: discord.Interaction,
            user: discord.Member,
            reason:str= "No Reason Provided"
            ):
        try:
            await user.send(
                    f"You were kicked from {interaction.guild.name}\nReason:{reason}"
                    )
        except:
            pass

        await user.kick(reason=reason)
        await interaction.response.send_message(
             f"👟{user.mention} kicked\nReason:{reason}"
                )
    @app_commands.command(
    name="timeout",
    description="Timeout a user"
)
    @app_commands.default_permissions(
    moderate_members=True
)
    async def timeout(
       self,
       interaction: discord.Interaction,
       user: discord.Member,
       minutes: int,
       reason: str = "No reason provided"
):
        await user.timeout(
          timedelta(minutes=minutes),
          reason=reason
    )

        await interaction.response.send_message(
           f"⏰ {user.mention} timed out for {minutes} minutes.\nReason: {reason}"
    )     
    @app_commands.command(
      name="untimeout",
      description="Untimeout a User"
      )
    @app_commands.default_permissions(
     moderate_members=True
)
    async def untimeout(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
 ):
        await user.timeout(None)
        await interaction.response.send_message(
            f"{user.mention} Timeout Removed "
             )

async def setup(bot):
    await bot.add_cog(moderation(bot))
