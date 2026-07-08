import discord
from discord.ext import commands
from discord import app_commands
from .resources.lua_resources import LUA_BASICS

LUA_RESOURCES= { 
  "lua_basics":LUA_BASICS,
}

class Lua_resourcesSelect(discord.ui.Select):
    def __init__(self):

        options =[
             discord.SelectOption(
                 label="Lua Basics",
                 value="lua_basics",
                 emoji="🌍"
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
         description=LUA_RESOURCES[category],
         color=discord.Color.blue()
      )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


class Lua_resourcesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Lua_resourcesSelect())


class Lua_resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="lua_resources",
        description="view Lua resources"
    )
    async def resources(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title=":books:Lua Learning Resources ",
            description="Choose a category from the dropdown menu below."
        )

        await interaction.response.send_message(
            embed=embed,
            view=Lua_resourcesView()
        )


async def setup(bot):
    await bot.add_cog(Lua_resources(bot))
