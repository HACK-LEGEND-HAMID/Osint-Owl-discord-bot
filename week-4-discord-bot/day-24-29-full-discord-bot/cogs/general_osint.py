import discord
from discord.ext import commands
from discord import app_commands
from .resources.general_search import GENERAL_SEARCH, SOCIAL_MEDIA_TOOLS,TWITTER_TOOLS,FACEBOOK_TOOLS,REDDIT_TOOLS,USERNAME_CHECK_TOOLS,NATIONAL_SEARCH_ENGINES,META_SEARCH_ENGINES,CODE_SEARCH_TOOLS,EMAIL_OSINT_TOOLS,PHONE_OSINT_TOOLS,DOMAIN_IP_TOOLS

GENERAL_OSINT_TOOLS = {
        "general_search":GENERAL_SEARCH,
        "social_media_tools":SOCIAL_MEDIA_TOOLS,
        "twitter_tools":TWITTER_TOOLS,
        "facebook_tools":FACEBOOK_TOOLS,       
        "reddit_tools":REDDIT_TOOLS,
        "username_check_tools":USERNAME_CHECK_TOOLS,
        "national_search_engine":NATIONAL_SEARCH_ENGINES,
        "meta_search_engines":META_SEARCH_ENGINES,
        "code_search_tools":CODE_SEARCH_TOOLS,
        "email_osint_tools":EMAIL_OSINT_TOOLS,
        "phone_osint_tools":PHONE_OSINT_TOOLS,
        "domain_ip_tools":DOMAIN_IP_TOOLS,
}

class General_osintSelect(discord.ui.Select):
    def __init__(self):

        options =[
             discord.SelectOption(
                 label="General Search",
                 value="general_search",
                 emoji="🌐"
                 ),
             discord.SelectOption(
                label="Github Cyber Resources",
                value="github_cyber",
                emoji="📜"
                 ),
             discord.SelectOption(
                label = "Social Media OSINT Tools",
                value="social_media_tools",
                emoji="📱"
                  ),
             discord.SelectOption(
                label = "Twitter OSINT Tools",
                value = "twitter_tools",
                emoji = "🐦"
                  ),
             discord.SelectOption(
                label = "Facebook OSINT Tools",
                value = "facebook_tools",
                emoji = "📘"

                 ),
                  discord.SelectOption(
                label="Reddit OSINT Tools",
                value="reddit_tools",
                emoji="👽"
                 ),

             discord.SelectOption(
                label="Username Check Tools",
                value="username_check_tools",
                emoji="👤"
                 ),

             discord.SelectOption(
                label="National Search Engines",
                value="national_search_engine",
                emoji="🌍"
                 ),

             discord.SelectOption(
                label="Meta Search Engines",
                value="meta_search_engines",
                emoji="🧠"
                 ),

             discord.SelectOption(
                label="Code Search Tools",
                value="code_search_tools",
                emoji="💻"
                 ),

             discord.SelectOption(
                label="Email OSINT Tools",
                value="email_osint_tools",
                emoji="📧"
                 ),

             discord.SelectOption(
                label="Phone OSINT Tools",
                value="phone_osint_tools",
                emoji="📞"
                 ),

             discord.SelectOption(
                label="Domain & IP Tools",
                value="domain_ip_tools",
                emoji="🌐"
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
         title=f"{category.replace('_'," ").title()}",
       description=GENERAL_OSINT_TOOLS[category]
        )

        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )


class General_osintView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(General_osintSelect())


class General_osint(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="general_osint",
        description="View OSINT Tools"
    )
    async def resources(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title=":books:General OSINT Tools ",
            description="Choose a category from the dropdown menu below."
        )

        await interaction.response.send_message(
            embed=embed,
            view=General_osintView()
        )


async def setup(bot):
    await bot.add_cog(General_osint(bot))
