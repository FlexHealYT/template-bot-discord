import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
from discord.ui import Select, View, Modal, TextInput, Button

import traceback

class Cours1Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label = "Acceder au cours suivant", emoji="⏭️",custom_id = "ch1", style = discord.ButtonStyle.primary)
    async def button1(self, interaction, button):
        user = interaction.user
        await interaction.response.send_modal(Cours1Modal(self))

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
        
class Cours1Modal(Modal, title="Variables"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    answer1 = TextInput(label="Texte est chaine de caractères ?",
                        style=discord.TextStyle.short,
                        placeholder="Oui/Non", 
                        required=True,
                        min_length=3,
                        max_length=3)
    answer2 = TextInput(
                    label="Fonction pour afficher une variable ?",
                    style=discord.TextStyle.short,
                    placeholder="Fonction()",
                    required=True,
                    min_length=5,
                    max_length=7)
    answer3 = TextInput(
                    label="Fonction pour convertir un string en nombre ?",
                    style=discord.TextStyle.short,
                    placeholder="Fonction()",
                    required=True,
                    min_length=5,
                    max_length=7)
    answer4 = TextInput(
                    label="Fonction pour saisir une valeur ?",
                    style=discord.TextStyle.short,
                    placeholder="Fonction()",
                    required=True,
                    min_length=5,
                    max_length=7)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "oui" and \
        answer2.lower() == "print()" and \
        answer3.lower() == "int()" and \
        answer4.lower() == "input()":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role1 = guild.get_role(1232422284921147535)  # Récupérer role1
            role2 = guild.get_role(1232422438915018762)  # Récupérer role2
            if role1 and role2:
                await member.add_roles(role1)  # Ajouter role1
                await member.add_roles(role2)  # Ajouter role2
        else:
            await interaction.response.send_message(f'Tu as fait une erreur ! Réessaie !', ephemeral=True)







class Cours2Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label = "Acceder au cours suivant", emoji="⏭️",custom_id = "ch2", style = discord.ButtonStyle.primary)
    async def button1(self, interaction, button):
        user = interaction.user
        await interaction.response.send_modal(Cours2Modal(self))

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
        
class Cours2Modal(Modal, title="Variables"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    answer1 = TextInput(label="Une chaine de caractères est un ... ?",
                        style=discord.TextStyle.short,
                        placeholder="Réponse...",
                        required=True,
                        min_length=3,
                        max_length=7)
    answer2 = TextInput(
                    label="Un nombre entier est un ... ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=3,
                    max_length=7)
    answer3 = TextInput(
                    label="Un nombre a virgule est un ... ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=3,
                    max_length=7)
    answer4 = TextInput(
                    label="Le type à valeur changeable est une ...  ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=3,
                    max_length=7)
    answer5 = TextInput(
                    label="Le type à valeur inchangeable est un ...  ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=3,
                    max_length=7)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value
        answer5 = self.answer5.value
        if \
        answer1.lower() == "str" or answer1.lower() == "string" and \
        answer2.lower() == "int" or answer2.lower() == "integer" and \
        answer3.lower() == "float" and \
        answer4.lower() == "liste" or answer4.lower() == "list" and \
        answer5.lower() == "tuple":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role2 = guild.get_role(1232422438915018762)
            role3 = guild.get_role(1232422457764221119)  # Récupérer role1
            if role3:
                await member.add_roles(role3)  # Ajouter role1
                await member.remove_roles(role2)
        else:
            await interaction.response.send_message(f'Tu as fait une erreur ! Réessaie !', ephemeral=True)








class Cours3Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label = "Acceder au cours suivant", emoji="⏭️",custom_id = "ch2", style = discord.ButtonStyle.primary)
    async def button1(self, interaction, button):
        user = interaction.user
        await interaction.response.send_modal(Cours3Modal(self))

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
        
class Cours3Modal(Modal, title="Variables"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    answer1 = TextInput(label="Quel mot pour utiliser \"si\" ?",
                        style=discord.TextStyle.short,
                        placeholder="Sans les :",
                        required=True,
                        min_length=2,
                        max_length=4)
    answer2 = TextInput(
                    label="Quel mot pour utiliser \"sinon\" ?",
                    style=discord.TextStyle.short,
                    placeholder="Sans les :",
                    required=True,
                    min_length=2,
                    max_length=4)
    answer3 = TextInput(
                    label="Quel est le dernier élément utile ?",
                    style=discord.TextStyle.short,
                    placeholder="Sans les :",
                    required=True,
                    min_length=2,
                    max_length=4)
    answer4 = TextInput(
                    label="Comment exprime-t-on une égalité ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=2,
                    max_length=4)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "if" and \
        answer2.lower() == "else" and \
        answer3.lower() == "elif" and \
        answer4.lower() == "==":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role3 = guild.get_role(1232422457764221119)  # Récupérer role1
            role4 = guild.get_role(1232422481332015245)  # Récupérer role1
            if role4:
                await member.remove_roles(role3)
                await member.add_roles(role4)  # Ajouter role1
        else:
            await interaction.response.send_message(f'Tu as fait une erreur ! Réessaie !', ephemeral=True)




class Cours4Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label = "Acceder au cours suivant", emoji="⏭️",custom_id = "ch2", style = discord.ButtonStyle.primary)
    async def button1(self, interaction, button):
        user = interaction.user
        await interaction.response.send_modal(Cours4Modal(self))

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
        
class Cours4Modal(Modal, title="Variables"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    answer1 = TextInput(label="La boucle pour voyager dans une liste ?",
                        style=discord.TextStyle.short,
                        placeholder="Seulement le mot-clé",
                        required=True,
                        min_length=3,
                        max_length=8)
    answer2 = TextInput(
                    label="La boucle pendant que ?",
                    style=discord.TextStyle.short,
                    placeholder="Seulement le mot-clé",
                    required=True,
                    min_length=3,
                    max_length=8)
    answer3 = TextInput(
                    label="Le mot pour sortir de la boucle ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=3,
                    max_length=8)
    answer4 = TextInput(
                    label="Le mot pour passer au tour suivant ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=3,
                    max_length=8)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "for" and \
        answer2.lower() == "while" and \
        answer3.lower() == "break" and \
        answer4.lower() == "continue":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role4 = guild.get_role(1232422481332015245)  # Récupérer role1
            role5 = guild.get_role(1232422517767929931)  # Récupérer role1
            if role5:
                await member.remove_roles(role4)
                await member.add_roles(role5)  # Ajouter role1
        else:
            await interaction.response.send_message(f'Tu as fait une erreur ! Réessaie !', ephemeral=True)





class Cours5Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label = "Acceder au cours suivant", emoji="⏭️",custom_id = "ch2", style = discord.ButtonStyle.primary)
    async def button1(self, interaction, button):
        user = interaction.user
        await interaction.response.send_modal(Cours5Modal(self))

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
        
class Cours5Modal(Modal, title="Variables"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    answer1 = TextInput(label="Comment définir une fonction ?",
                        style=discord.TextStyle.short,
                        placeholder="Réponse...",
                        required=True,
                        min_length=3,
                        max_length=9)
    answer2 = TextInput(
                    label="Elle fais une suite d'... ?",
                    style=discord.TextStyle.short,
                    placeholder="Avec un \"s\"",
                    required=True,
                    min_length=3,
                    max_length=9)
    answer3 = TextInput(
                    label="Grâce à quoi on récupère une valeur ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=3,
                    max_length=9)
    answer4 = TextInput(
                    label="Elle peut prendre des ... ?",
                    style=discord.TextStyle.short,
                    placeholder="Avec un \"s\"",
                    required=True,
                    min_length=3,
                    max_length=9)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "def" and \
        answer2.lower() == "actions" and \
        answer3.lower() == "return" and \
        answer4.lower() == "arguments":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role5 = guild.get_role(1232422517767929931)  # Récupérer role1
            role6 = guild.get_role(1232422542862581761)  # Récupérer role1
            if role6:
                await member.remove_roles(role5)
                await member.add_roles(role6)  # Ajouter role1
        else:
            await interaction.response.send_message(f'Tu as fait une erreur ! Réessaie !', ephemeral=True)







class Cours6Button(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)

    @discord.ui.button(label = "Acceder au cours suivant", emoji="⏭️",custom_id = "ch2", style = discord.ButtonStyle.primary)
    async def button1(self, interaction, button):
        user = interaction.user
        await interaction.response.send_modal(Cours6Modal(self))

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)
        
class Cours6Modal(Modal, title="Variables"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    answer1 = TextInput(label="Importer le module TKINTER",
                        style=discord.TextStyle.short,
                        placeholder="Sans majuscules",
                        required=True,
                        min_length=14,
                        max_length=28)
    answer2 = TextInput(
                    label="Importer le module TKINTER avec l'alias TK",
                    style=discord.TextStyle.short,
                    placeholder="Sans majuscules",
                    required=True,
                    min_length=14,
                    max_length=28)
    answer3 = TextInput(
                    label="Importer la fonction mainloop",
                    style=discord.TextStyle.short,
                    placeholder="Uniquement la FONCTION mainloop dans le module TKINTER",
                    required=True,
                    min_length=14,
                    max_length=28)
    answer4 = TextInput(
                    label="Importer le fichier situé dans co/file.py",
                    style=discord.TextStyle.short,
                    placeholder="Chemin: co/file.py",
                    required=True,
                    min_length=14,
                    max_length=28)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value


        if answer1.lower() == "import tkinter" and \
        answer2.lower() == "import tkinter as tk" and \
        answer3.lower() == "from tkinter import mainloop" and \
        answer4.lower() == "import co.file":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as fini d\'apprendre les bases de python !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role6 = guild.get_role(1232422542862581761)  # Récupérer role1
            roleMASTER = guild.get_role(1233099162023755817)
            if role6:
                await member.remove_roles(role6)
                await member.add_roles(roleMASTER)  # Ajouter role1
        else:
            await interaction.response.send_message(f'Tu as fait une erreur ! Réessaie !', ephemeral=True)