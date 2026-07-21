import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime,timedelta

class CTF(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.submissions = {}
        self.ctf_ative = False 
        self.correct = ""
        self.start_time = None

ADMIN_IDS = [1519702679843115028,1352440514498269255,1502702326551675082]

    async def ctf(self, interaction: discord.Interaction, flag: str):
       if interaction.user.id not in ADMIN_IDS:
          await interaction.response.send_message("Admin Only",ephemeral=True) 
          return

       self.ctf_active = True 
       self.correct_answer = flag
       self.start_time = datetime.now()
       self.submissions = {}

       await interaction.response.send_message(f"✅ CTF Started!\nFlag: ||{flag}||\n⏰ 24 Hours Timer ON")  
    
    @app_commands.command(name="ctf_submit",description="Submit Your Flag")
    async def ctf_submit(self,interaction:discord.Interaction,answer:str):
    
       if not self.ctf_active:
          await interaction.response.send_message("No CTF Active",ephemeral=True)
          return
       elapsed = datetime.now() - self.start_time
       if elapsed > timedelta(hours=24):
          await interaction.response.send_message("CTF Expired")
          return
     
       user_id = str(interaction.user.id) 
       if user_id in self.submissions:
          await interaction.response.send_message("Already Submitted!",ephemeral=True)
          return 
       

       self.submissions[user_id]={
       "username":interaction.user.name,
       "answer":answer,
       "time":datetime.now(),
       "correct": answer == self.correct_answer
}   
      await interaction.response.send_message("Submitted!",ephemeral=True)
    
    @app_command.command(name="ctf_end",description="End CTF (ADMIN)")
    async def ctf_end(self,interaction:discord.Interaction):
       if interaction.user.id not in ADMIN_IDS:
           await interaction.response.send_mesaage("Admin Only",ephemeral=True)
           return
       self.ctf_active = False
       results={"winners":[],"losers":[]}
       for submission in self.submissions.values():
           key="winners" if submission["correct"] else "losers"
           result[key].append(submission)
       if winners:
          embed.add_field(
          name=f"✅ Winners ({len(winners)})",
          value="\n".join(w["username"] for w in winners),
          inline=False
         )
       else:
          embed.add_field(name="✅ Winners",value="None 😢",inline=False)
       if losers:
          embed.add_field(
                name=f"❌ Wrong Answers ({len(losers)})",
                value="\n".join(l["username"] for l in losers),
                inline=False
            )
       await interaction.response.send_message(embed=embed) 


async def setuo(bot):
   await bot.add_cog(CTF(bot))
