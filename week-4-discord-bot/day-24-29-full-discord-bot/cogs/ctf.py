import discord
from discord import app_commands
from discord.ext import commands

class CTF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.submission = {}
        self.ctf_ative = False 

    @app_commands.command(name="ctf", description="Use this Command for CTF Task")
    async def ctf(self, interaction: discord.Interaction, name: str, age: int):
        await interaction.response.send_message(f"My name is {name} and Age is {age}")
    
