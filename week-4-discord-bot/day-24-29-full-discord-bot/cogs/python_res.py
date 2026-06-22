import discord
from discord.ext import commands
from discord import app_commands
from .resources.python_resources import PYTHON_BASICS, PYTHON_INTERMEDIATE, PYTHON_ADVANCED
PYTHON_RESOURCES = {
        "python_basics":PYTHON_BASICS,
        "python_intermediate":PYTHON_INTERMEDIATE,
        "python_advanced":PYTHON_ADVANCED,
}

class Python_resourcesSelect(discord.ui.Select):
    def __init__(self):

        options =[
             discord.SelectOption(
                 label="Python Basics",
                 value="python_basics",
                 emoji="🌐"
                 ),
             discord.SelectOption(
                label="Python Intermediate",
                value="python_intermediate",
                emoji="📘"
                 ),
             discord.SelectOption(
                label="Python Advanced",
                value="python_advanced",
                emoji="🌀"
                 ),
           ]

        super().__init__(
             placeholder="Select a resources category...",
             options=options
                )

    async def callback(self,
                       interaction:discord.Interaction
                       ):

        category = self.values[0]

        embed = discord.Embed(
         title=f"{category.replace('_',' ').title()}",
         description=PYTHON_RESOURCES[category],
         color=discord.Color.green()  
      )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


class Python_resourcesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Python_resourcesSelect())


class Python_resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="python_resources",
        description="view python resources"
    )
    async def resources(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title=":books:Python Learning Resources ",
            description="Choose a category from the dropdown menu below."
        )

        await interaction.response.send_message(
            embed=embed,
            view=Python_resourcesView()
        )


async def setup(bot):
    await bot.add_cog(Python_resources(bot))
