import random

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord import app_commands

class Choice(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Pile", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "pile"
        self.stop()
    
    @discord.ui.button(label="Face", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "face"
        self.stop()


class Chifumi(discord.ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(
                label="Ciseaux", description="Vous choisissez ciseaux.", emoji="✂"
            ),
            discord.SelectOption(
                label="Pierre", description="Vous choisissez pierre.", emoji="🪨"
            ),
            discord.SelectOption(
                label="Papier", description="Vous choisissez papier.", emoji="🧻"
            ),
        ]
        super().__init__(
            placeholder="Choisissez...",    
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction) -> None:
        choices = {
            "pierre": 0,
            "papier": 1,
            "ciseaux": 2,
        }
        user_choice = self.values[0].lower()
        user_choice_index = choices[user_choice]

        bot_choice = random.choice(list(choices.keys()))
        bot_choice_index = choices[bot_choice]

        result_embed = discord.Embed(color=0xBEBEFE)
        result_embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.display_avatar.url
        )

        winner = (3 + user_choice_index - bot_choice_index) % 3
        if winner == 0:
            result_embed.description = f"**C'est un match nul !**\nVous avez choisi {user_choice} et j'ai choisi {bot_choice}."
            result_embed.colour = 0xF59E42
        elif winner == 1:
            result_embed.description = f"**Vous avez gagné !**\nVous avez choisi {user_choice} et j'ai choisi {bot_choice}."
            result_embed.colour = 0x57F287
        else:
            result_embed.description = f"**Vous avez perdu !**\nVous avez choisi {user_choice} et j'ai choisi {bot_choice}."
            result_embed.colour = 0xE02B2B

        await interaction.response.edit_message(
            embed=result_embed, content=None, view=None
        )


class ChifumiView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.add_item(Chifumi())


class FunGog(commands.Cog, name="fun"):
    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.hybrid_command(
        name="fait_aléatoire", 
        description="Obtenez un fait aléatoire."
    )
    async def random_fact(self, context: Context) -> None:
        """
        Obtenez un fait aléatoire.

        :param context: Le contexte de la commande hybride.
        """
        # Ouvrir le fichier texte
        with open("random_fact.txt", "r", encoding="utf-8") as file:
            phrases = file.readlines()
        
        # Choisir une phrase aléatoire
        random_phrase = random.choice(phrases).strip()
        
        # Créer l'embed avec la phrase choisie
        embed = discord.Embed(description=random_phrase, color=0xD75BF4)
        
        # Envoyer l'embed
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="citations", 
        description="Obtenez une citation."
    )
    async def citations(self, context: Context) -> None:
        """
        Obtenez un fait aléatoire.

        :param context: Le contexte de la commande hybride.
        """
        # Ouvrir le fichier texte
        with open("citations.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Choisir une ligne aléatoire
        random_line_index = random.randint(0, len(lines) - 1)
        random_phrase = lines[random_line_index].strip()
        
        while random_phrase == "%":
            random_line_index = random.randint(0, len(lines) - 1)
            random_phrase = lines[random_line_index].strip()

        # Vérifier si la ligne commence par "- "
        if random_phrase.startswith("- "):
            # Utiliser cette ligne comme titre d'embed
            title = random_phrase.strip()
            
            # Récupérer la ligne précédente
            if random_line_index > 0:
                description = lines[random_line_index - 1].strip()
            else:
                description = ""
        else:
            # Si la ligne ne commence pas par "- ", utiliser la ligne comme description de l'embed
            # Utiliser cette ligne comme titre d'embed
            description = random_phrase.strip()
            
            # Récupérer la ligne précédente
            if random_line_index > 0:
                title = lines[random_line_index + 1].strip()
            else:
                title = ""
            
        # Créer l'embed avec le titre et la description
        embed = discord.Embed(title=title, description=description, color=0xD75BF4)       

        # Envoyer l'embed
        await context.send(embed=embed, ephemeral=True)


    @commands.hybrid_command(
        name="pile_ou_face", description="Faites un lancer de pièce, mais donnez votre pari avant."
    )
    async def pile_ou_face(self, context: Context) -> None:
        """
        Faites un lancer de pièce, mais donnez votre pari avant.

        :param context: Le contexte de la commande hybride.
        """
        buttons = Choice()
        embed = discord.Embed(description="Quel est votre pari?", color=0xBEBEFE)
        message = await context.send(embed=embed, view=buttons)
        await buttons.wait()  # Nous attendons que l'utilisateur clique sur un bouton.
        result = random.choice(["pile", "face"])
        if buttons.value == result:
            embed = discord.Embed(
                description=f"Correct ! Vous avez deviné `{buttons.value}` et j'ai lancé la pièce à `{result}`.",
                color=0xBEBEFE,
            )
        else:
            embed = discord.Embed(
                description=f"Oups ! Vous avez deviné `{buttons.value}` et j'ai lancé la pièce à `{result}`, meilleure chance la prochaine fois !",
                color=0xE02B2B,
            )
        await message.edit(embed=embed, view=None, content=None)

    @app_commands.command(
        name="chifumi", description="Jouez au jeu de pierre-papier-ciseaux contre le bot."
    )
    async def chifumi(self, interaction: discord.Interaction) -> None:
        """
        Jouez au jeu de pierre-papier-ciseaux contre le bot.

        :param context: Le contexte de la commande hybride.
        """
        view = ChifumiView()
        await interaction.response.send_message("Veuillez faire votre choix", view=view)


async def setup(bot) -> None:
    await bot.add_cog(FunGog(bot))
