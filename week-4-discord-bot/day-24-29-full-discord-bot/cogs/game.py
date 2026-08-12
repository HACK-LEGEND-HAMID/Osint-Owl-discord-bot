import asyncio
import discord
from discord import app_commands
from discord.ext import commands

# =========================================================
# HANGMAN GAME CLASS
# =========================================================

class HangmanGame:
    def __init__(self, host, guest, channel, word):
        self.host = host
        self.guest = guest
        self.channel = channel
        
        self.word = word.upper()
        self.blanks = ["_" for _ in self.word]
        
        # Lives are separate for both players
        self.max_lives = max(3, len(set(self.word)))
        
        self.lives = {
            host.id: self.max_lives,
            guest.id: self.max_lives
        }
        
        self.guessed = []
        self.current_turn = guest.id
        
        self.message = None
        self.finished = False
    
    @property
    def players(self):
        return [self.host, self.guest]
    
    def other_player(self, player_id):
        if player_id == self.host.id:
            return self.guest
        return self.host
    
    def display_lives(self, player_id):
        lives = self.lives[player_id]
        return (
            "❤️ " * lives +
            "🖤 " * (self.max_lives - lives)
        )
    
    def word_display(self):
        return " ".join(self.blanks)
    
    def guessed_display(self):
        if not self.guessed:
            return "None"
        return ", ".join(self.guessed)
    
    def make_embed(self, title="🎮 Hangman"):
        current_player = self.other_player(
            self.host.id
        ) if self.current_turn == self.host.id else self.host
        
        embed = discord.Embed(
            title=title,
            color=discord.Color.blurple()
        )
        
        embed.add_field(
            name="🔤 Word",
            value=f"**{self.word_display()}**",
            inline=False
        )
        
        embed.add_field(
            name=f"❤️ {self.host.display_name}",
            value=self.display_lives(self.host.id),
            inline=True
        )
        
        embed.add_field(
            name=f"❤️ {self.guest.display_name}",
            value=self.display_lives(self.guest.id),
            inline=True
        )
        
        embed.add_field(
            name="🎯 Turn",
            value=current_player.mention,
            inline=False
        )
        
        embed.add_field(
            name="🔡 Guessed Letters",
            value=self.guessed_display(),
            inline=False
        )
        
        embed.set_footer(
            text=f"{self.host.display_name} vs {self.guest.display_name}"
        )
        
        return embed


# =========================================================
# WORD INPUT MODAL
# =========================================================

class WordModal(discord.ui.Modal, title="🔤 Set Hangman Word"):
    
    word = discord.ui.TextInput(
        label="Secret Word",
        placeholder="Enter a word...",
        min_length=3,
        max_length=20,
        required=True
    )
    
    def __init__(self, cog, host, guest, channel, invite_view):
        super().__init__()
        self.cog = cog
        self.host = host
        self.guest = guest
        self.channel = channel
        self.invite_view = invite_view
    
    async def on_submit(self, interaction: discord.Interaction):
        word = self.word.value.strip().upper()
        
        # Only alphabetic words
        if not word.isalpha():
            await interaction.response.send_message(
                "❌ The word must contain only English letters",
                ephemeral=True
            )
            return
        
        channel_id = self.channel.id
        
        # Prevent duplicate games
        if channel_id in self.cog.games:
            await interaction.response.send_message(
                "❌ A game is already running in this channel",
                ephemeral=True
            )
            return
        
        # Disable invite buttons
        for child in self.invite_view.children:
            child.disabled = True
        await self.invite_view.message.edit(view=self.invite_view)
        
        # Create game
        game = HangmanGame(
            self.host,
            self.guest,
            self.channel,
            word
        )
        
        self.cog.games[channel_id] = game
        
        view = HangmanView(game)
        embed = game.make_embed()
        message = await self.channel.send(
            embed=embed,
            view=view
        )
        
        game.message = message
        
        await interaction.response.send_message(
            f"🎮 Game started in {self.channel.mention}!",
            ephemeral=True
        )


# =========================================================
# INVITE VIEW
# =========================================================

class InviteView(discord.ui.View):
    
    def __init__(self, cog, host, guest, channel):
        super().__init__(timeout=120)
        self.cog = cog
        self.host = host
        self.guest = guest
        self.channel = channel
        self.message = None
    
    @discord.ui.button(
        label="Accept",
        emoji="✅",
        style=discord.ButtonStyle.green
    )
    async def accept(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        if interaction.user.id != self.guest.id:
            await interaction.response.send_message(
                "❌ This invitation is not for you",
                ephemeral=True
            )
            return
        
        await interaction.response.send_modal(
            WordModal(
                self.cog,
                self.host,
                self.guest,
                self.channel,
                self
            )
        )
    
    @discord.ui.button(
        label="Reject",
        emoji="❌",
        style=discord.ButtonStyle.red
    )
    async def reject(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        if interaction.user.id != self.guest.id:
            await interaction.response.send_message(
                "❌ This invitation is not for you",
                ephemeral=True
            )
            return
        
        for child in self.children:
            child.disabled = True
        
        await interaction.response.edit_message(view=self)
        
        await interaction.followup.send(
            "❌ Game invitation rejected.",
            ephemeral=True
        )


# =========================================================
# GUESS MODAL
# =========================================================

class GuessModal(discord.ui.Modal, title="🎯 Guess a Letter"):
    
    letter = discord.ui.TextInput(
        label="Letter",
        placeholder="Enter ONE letter...",
        min_length=1,
        max_length=1,
        required=True
    )
    
    def __init__(self, game):
        super().__init__()
        self.game = game
    
    async def on_submit(self, interaction: discord.Interaction):
        letter = self.letter.value.upper()
        game = self.game
        
        # Validate letter
        if not letter.isalpha():
            await interaction.response.send_message(
                "❌ Please enter a valid English letter",
                ephemeral=True
            )
            return
        
        # Check turn
        if interaction.user.id != game.current_turn:
            await interaction.response.send_message(
                "❌ It's not your turn!",
                ephemeral=True
            )
            return
        
        # Check if already guessed
        if letter in game.guessed:
            await interaction.response.send_message(
                f"❌ Letter **{letter}** has already been guessed!",
                ephemeral=True
            )
            return
        
        # Add to guessed list
        game.guessed.append(letter)
        
        # Check guess
        if letter in game.word:
            # Correct guess - fill blanks
            for i, char in enumerate(game.word):
                if char == letter:
                    game.blanks[i] = letter
            
            # Check win
            if "_" not in game.blanks:
                game.finished = True
                embed = game.make_embed("🏆 GAME OVER - WINNER!")
                
                embed.add_field(
                    name="🎉 Result",
                    value=f"**{interaction.user.mention} guessed the word!**\n"
                          f"The word was: **{game.word}**",
                    inline=False
                )
                
                await game.message.edit(embed=embed, view=None)
                await interaction.response.send_message(
                    "🎉 You won! The word is complete!",
                    ephemeral=True
                )
                return
            
            await interaction.response.send_message(
                f"✅ Correct! **{letter}** is in the word!",
                ephemeral=True
            )
        
        else:
            # Wrong guess - lose a life and switch turn
            game.lives[interaction.user.id] -= 1
            game.current_turn = game.other_player(interaction.user.id).id
            
            # Check lose
            if game.lives[interaction.user.id] <= 0:
                game.finished = True
                winner = game.other_player(interaction.user.id)
                embed = game.make_embed("💀 GAME OVER ELIMINATED!")
                
                embed.add_field(
                    name="💀 Result",
                    value=f"**{interaction.user.mention} ran out of lives!**\n"
                          f"**{winner.mention} wins!**\n"
                          f"The word was: **{game.word}**",
                    inline=False
                )
                
                await game.message.edit(embed=embed, view=None)
                await interaction.response.send_message(
                    f"💀 You lost! The word was: **{game.word}**",
                    ephemeral=True
                )
                return
            
            await interaction.response.send_message(
                f"❌ Wrong! **{letter}** is not in the word. Turn switches.",
                ephemeral=True
            )
        
        # Update game display
        embed = game.make_embed()
        view = HangmanView(game)
        await game.message.edit(embed=embed, view=view)


# =========================================================
# GUESS BUTTON VIEW
# =========================================================

class HangmanView(discord.ui.View):
    
    def __init__(self, game):
        super().__init__(timeout=None)
        self.game = game
    
    @discord.ui.button(
        label="Guess Letter",
        emoji="🎯",
        style=discord.ButtonStyle.blurple
    )
    async def guess_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        game = self.game
        
        if game.finished:
            await interaction.response.send_message(
                "❌ This game has already ended!",
                ephemeral=True
            )
            return
        
        if interaction.user.id not in game.lives:
            await interaction.response.send_message(
                "❌ You are not part of this game!",
                ephemeral=True
            )
            return
        
        await interaction.response.send_modal(GuessModal(game))


# =========================================================
# MAIN COG
# =========================================================

class GAME(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.games = {}
    
    @app_commands.command(
        name="hangman",
        description="Challenge someone to a game of Hangman!"
    )
    async def hangman(
        self,
        interaction: discord.Interaction,
        player: discord.Member
    ):
        if player == interaction.user:
            await interaction.response.send_message(
                "❌ You cannot challenge yourself!",
                ephemeral=True
            )
            return
        
        if player.bot:
            await interaction.response.send_message(
                "❌ You cannot challenge a bot!",
                ephemeral=True
            )
            return
        
        channel_id = interaction.channel.id
        if channel_id in self.games:
            await interaction.response.send_message(
                "❌ A game is already running in this channel!",
                ephemeral=True
            )
            return
        
        view = InviteView(self, interaction.user, player, interaction.channel)
        message = await interaction.response.send_message(
            f"🎮 {player.mention}, **{interaction.user.display_name}** "
            f"wants to play Hangman!\n\n"
            f"**How to Play:**\n"
            f"• Host sets a secret word\n"
            f"• Players take turns guessing letters\n"
            f"• Correct guess = Keep turn\n"
            f"• Wrong guess = Lose a life + Switch turn\n"
            f"• Run out of lives = Eliminated\n"
            f"• Guess the word = Winner!",
            view=view
        )
        
        view.message = message


async def setup(bot):
    await bot.add_cog(GAME(bot))
