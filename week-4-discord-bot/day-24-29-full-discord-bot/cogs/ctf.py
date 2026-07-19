import discord
from discord import app_commands
from discord.ext import commands

class CTF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.submission = {}
       
    @app_commands.command(name="ctf", description="Use this Command for CTF Task")
    async def ctf(self, interaction: discord.Interaction):
    
