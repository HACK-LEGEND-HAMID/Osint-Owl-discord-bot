import discord
from discord.ext import commands
from discord import app_commands
from .resources.general_search import GENERAL_SEARCH

RESOURCES = {
        "general_search":GENERAL_SEARCH
        }

class ResourcesSelect(discord.ui.Select):
    def __init__(self):

        options =[
             discord.SelectOption(
                 label="General Search",
                 value="general_search",
                 emoji="🌐"
                 )

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
         title=f"{category.replace('_'," ").title()}",
       description=RESOURCES[category]
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


class ResourceView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ResourcesSelect())


class Resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="resources",
        description="View OSINT resources"
    )
    async def resources(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title=":books: OSINT Resources",
            description="Choose a category from the dropdown menu below."
        )

        await interaction.response.send_message(
            embed=embed,
            view=ResourceView()
        )


async def setup(bot):
    await bot.add_cog(Resources(bot))
