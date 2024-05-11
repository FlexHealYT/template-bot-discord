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
        # Make sure we know what the error actually isanswer1.lower() == "import { ... }"
        traceback.print_exception(type(error), error, error.__traceback__)
        
class Cours1Modal(Modal, title="Variables"):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    answer1 = TextInput(label="Quelle variable stocke une valeur numérique ?",
                        style=discord.TextStyle.short,
                        placeholder="Réponse...",
                        required=True,
                        min_length=5,
                        max_length=20)
    answer2 = TextInput(
                    label="Quelle variable stocke du texte ?",
                    style=discord.TextStyle.short,
                    placeholder="Sans accent si en fr",
                    required=True,
                    min_length=5,
                    max_length=20)
    answer3 = TextInput(
                    label="Quelle variable stocke seulement 2 valeurs ?",
                    style=discord.TextStyle.short,
                    placeholder="Sans accent si en fr",
                    required=True,
                    min_length=5,
                    max_length=20)
    answer4 = TextInput(
                    label="Quelle variable peux stocker > 1 valeur ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=5,
                    max_length=20)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "nombre" or answer1.lower() == "number" and \
        answer2.lower() == "chaine de caracteres" or answer2.lower() == "string" and \
        answer3.lower() == "booleen" or answer3.lower() == "boolean" and \
        answer4.lower() == "tableau" or answer4.lower() == "array":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role2 = guild.get_role(1232423071625908276)
            role3 = guild.get_role(1232423094690381966)  # Récupérer role1
            if role3 and role2:
                await member.add_roles(role3)  # Ajouter role1
                await member.remove_roles(role2)  # Ajouter role2
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

    answer1 = TextInput(label="Comment déclarer une variable changeable ?",
                        style=discord.TextStyle.short,
                        placeholder="Réponse...",
                        required=True,
                        min_length=1,
                        max_length=5)
    answer2 = TextInput(
                    label="Comment déclarer une variable inchangeable ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=1,
                    max_length=5)
    answer3 = TextInput(
                    label="On peut utiliser \"@\" dans une variable ?",
                    style=discord.TextStyle.short,
                    placeholder="Oui/Non",
                    required=True,
                    min_length=1,
                    max_length=5)
    answer4 = TextInput(
                    label="On peut utiliser \"$\" dans une variable ?",
                    style=discord.TextStyle.short,
                    placeholder="Oui/Non",
                    required=True,
                    min_length=1,
                    max_length=5)
    answer4 = TextInput(
                    label="Quel élément à la fin de chaque phrase ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=1,
                    max_length=5)

    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value
        answer5 = self.answer5.value
        if \
        answer1.lower() == "let" and \
        answer2.lower() == "const" and \
        answer3.lower() == "non" and \
        answer4.lower() == "oui" and \
        answer5.lower() == ";" :
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role1 = guild.get_role(1232422284921147535)  # Récupérer role1
            role2 = guild.get_role(1232423071625908276)  # Récupérer role2
            if role2:
                await member.add_roles(role1)  # Ajouter role1
                await member.add_roles(role2)
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
                        placeholder="Uniquement le mot",
                        required=True,
                        min_length=1,
                        max_length=8)
    answer2 = TextInput(
                    label="Que mettre autour de la condition ?",
                    style=discord.TextStyle.short,
                    placeholder="Sans espaces",
                    required=True,
                    min_length=1,
                    max_length=8)
    answer3 = TextInput(
                    label="Que mettre autour des actions à effectuer ?",
                    style=discord.TextStyle.short,
                    placeholder="Sans espaces",
                    required=True,
                    min_length=1,
                    max_length=8)
    answer4 = TextInput(
                    label="Quel opérateur JavaScript utilise par \"? :\" ?",
                    style=discord.TextStyle.short,
                    placeholder="Sans accent",
                    required=True,
                    min_length=1,
                    max_length=8)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "if" and \
        answer2.lower() == "()" or answer2.lower() == "(" or answer2.lower() == ")" and \
        answer3.lower() == "{}" or answer3.lower() == "{" or answer3.lower() == "}" and \
        answer4.lower() == "ternaire":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role3 = guild.get_role(1232423094690381966)  # Récupérer role1
            role4 = guild.get_role(1232423127309615104)  # Récupérer role1
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

    answer1 = TextInput(label="Utilité principale de la boucle \'for\' ?",
                        style=discord.TextStyle.short,
                        placeholder="Sans accent",
                        required=True,
                        min_length=5,
                        max_length=10)
    answer2 = TextInput(
                    label="Boucle exécutée tant que condition vraie ?",
                    style=discord.TextStyle.short,
                    placeholder="Seulement le mot-clé",
                    required=True,
                        min_length=5,
                        max_length=10)
    answer3 = TextInput(
                    label="Le mot pour sortir de la boucle ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                        min_length=5,
                        max_length=10)
    answer4 = TextInput(
                    label="Boucle garantissant une exécution ?",
                    style=discord.TextStyle.short,
                    placeholder="mot1...mot2",
                    required=True,
                        min_length=5,
                        max_length=10)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "iterations" or answer1.lower() == "iteration" and \
        answer2.lower() == "while" and \
        answer3.lower() == "break" and \
        answer4.lower() == "do...while":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role4 = guild.get_role(1232423127309615104)  # Récupérer role1
            role5 = guild.get_role(1232423146314010685)  # Récupérer role1
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
                        placeholder="Juste le mot",
                        required=True,
                        min_length=2,
                        max_length=18)
    answer2 = TextInput(
                    label="Comment déclarer une fonction anonyme ?",
                    style=discord.TextStyle.short,
                    placeholder="Remplace ce qui peut varier par \"...\"",
                    required=True,
                    min_length=2,
                    max_length=18)
    answer3 = TextInput(
                    label="Que rajouter dans une fonction fléchée ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=2,
                    max_length=18)
    answer4 = TextInput(
                    label="Comment appelle-t-on la fonction maFonction ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse...",
                    required=True,
                    min_length=2,
                    max_length=18)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value

        if answer1.lower() == "function" and \
        answer2.lower() == "function() { ... }" or answer2.lower() == "function() {...}" and \
        answer3.lower() == "=>" and \
        answer4.lower() == "mafonction()":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as maintenant accès au prochain cours !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role5 = guild.get_role(1232423146314010685)  # Récupérer role1
            role6 = guild.get_role(1232423178404368547)  # Récupérer role1
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

    answer1 = TextInput(label="Comment importer des fonctions spécifiques ?",
                        style=discord.TextStyle.short,
                        placeholder="Remplace ce qui peut varier par \"...\"",
                        required=True,
                        min_length=1,
                        max_length=27)
    answer2 = TextInput(
                    label="Quel symbole importe tout un module ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse",
                    required=True,
                    min_length=1,
                    max_length=27)
    answer3 = TextInput(
                    label="Comment importer une fonction par défaut ?",
                    style=discord.TextStyle.short,
                    placeholder="Remplace ce qui peut varier par \"...\"",
                    required=True,
                    min_length=1,
                    max_length=27)    
    answer4 = TextInput(
                    label="Comment utiliser la \"fonction1\" importée ?",
                    style=discord.TextStyle.short,
                    placeholder="Réponse",
                    required=True,
                    min_length=1,
                    max_length=27)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        answer2 = self.answer2.value
        answer3 = self.answer3.value
        answer4 = self.answer4.value


        if answer1.lower() == "import { ... }" or answer1.lower() == "import {...}" and \
        answer2.lower() == "*" and \
        answer3.lower() == "import ... from ..." and \
        answer4.lower() == "fonction1();":
            await interaction.response.send_message(f'Bravo ! Tu as tout juste ! Tu as fini d\'apprendre les bases de JavaScript !', ephemeral=True)
            member = interaction.user
            guild = member.guild
            role6 = guild.get_role(1232423178404368547)  # Récupérer role1
            roleMASTER = guild.get_role(1233099331750330529)
            if role6:
                await member.remove_roles(role6)
                await member.add_roles(roleMASTER)  # Ajouter role1
        else:
            await interaction.response.send_message(f'Tu as fait une erreur ! Réessaie !', ephemeral=True)