import discord
import traceback
import asyncio
import os
import aiofiles
from datetime import datetime
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
from discord.ui import Select, View, Modal, TextInput, Button

class CloseTicketModal(Modal, title="Fermer"):
    def __init__(self, bot, channel, log_channel_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot
        self.channel = channel
        self.log_channel_id = log_channel_id

    answer1 = TextInput(label="Pourquoi fermer le ticket ?",
                        style=discord.TextStyle.long,
                        placeholder="Raison...", 
                        required=True,
                        min_length=2,
                        max_length=2000)
    
    async def on_submit(self, interaction: discord.Interaction):
        answer1 = self.answer1.value
        embed = discord.Embed(
            title="Ticket fermé"
        )
        embed.add_field(name="Ticket", value=self.channel.name, inline=False)
        embed.add_field(name="Raison", value=answer1, inline=False)
        embed.add_field(name="Fermé par", value=interaction.user.mention, inline=False)
        
        # Save messages to file
        await self.save_messages_to_file()
        
        log_channel = self.bot.get_channel(self.log_channel_id)
        if log_channel is None:
            await interaction.response.send_message("Le salon de log est introuvable.", ephemeral=True)
            return
        await interaction.response.send_message(f'Le ticket sera clos dans 5 secondes')
        await asyncio.sleep(5)
        await self.channel.delete()
        await log_channel.send(embed=embed)

    async def save_messages_to_file(self):
        # Creating the directory if it doesn't exist
        if not os.path.exists("./ticket_logs"):
            os.makedirs("./ticket_logs")
        
        # File name format: channel_name_date_time.txt
        file_name = f"./ticket_logs/{self.channel.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

        # Writing messages to the file
        async with aiofiles.open(file_name, mode="w", encoding="utf-8") as file:
            async for message in self.channel.history(limit=None):
                await file.write(f"{message.author.display_name}: {message.content}\n")

        return file_name

class ClaimTicket(discord.ui.View):
    def __init__(self, bot, utilisateur_id, salon_id, salon):
        super().__init__()
        self.bot = bot
        self.utilisateur_id = utilisateur_id
        self.salon_id = salon_id
        self.salon = salon  # Ajouter l'attribut salon

    @discord.ui.button(label="Claim le ticket", emoji="🧑‍🔧", custom_id="claim", style=discord.ButtonStyle.green)
    async def button2(self, interaction, button):
        if interaction is None or interaction.user is None:
            return
        user = await self.bot.fetch_user(interaction.user.id)
        opener = await self.bot.fetch_user(self.utilisateur_id)
        
        salon = self.salon
        if user is None:
            await interaction.response.send_message("L'utilisateur spécifié est introuvable.", ephemeral=True)
            return
        if opener is None:
            await interaction.response.send_message("Jsp", ephemeral=True)
            return
        if salon is None:
            await interaction.response.send_message("Le salon spécifié est introuvable.", ephemeral=True)
            return
        await salon.set_permissions(interaction.guild.default_role, send_messages=False, view_channel=False)
        
        overwrite = {
            salon.guild.default_role: discord.PermissionOverwrite(read_messages=False, view_channel=False),
            discord.utils.get(salon.guild.roles, id=1198232712910221342): discord.PermissionOverwrite(read_messages=True, view_channel=True, send_messages=False)
        }
        await salon.edit(overwrites=overwrite)

        perms = salon.overwrites_for(user)
        perms.send_messages = True
        perms.read_messages = True
        perms.read_message_history = True
        perms.view_channel = True
        perms.connect = False
        perms.speak = False
        perms.use_voice_activation = False
        perms.add_reactions = False
        perms.manage_messages = False
        perms.manage_permissions = False
        perms.manage_channels = False
        await salon.set_permissions(user, overwrite=perms)

        perms = salon.overwrites_for(opener)
        perms.send_messages = True
        perms.read_messages = True
        perms.read_message_history = True
        perms.view_channel = True
        perms.connect = False
        perms.speak = False
        perms.use_voice_activation = False
        perms.add_reactions = False
        perms.manage_messages = False
        perms.manage_permissions = False
        perms.manage_channels = False
        await salon.set_permissions(opener, overwrite=perms)
        
        # Disable the clicked button
        view = JustClose(self.bot, self.salon)
        await interaction.message.edit(view=view)
        await interaction.response.send_message(f"{opener.mention} c'est {user.mention} qui s'occupera de votre ticket !")

    @discord.ui.button(label="Fermer le ticket", emoji="🔒", custom_id="close", style=discord.ButtonStyle.red)
    async def button1(self, interaction, button):
        if interaction is None or interaction.user is None:  # Vérifiez si l'interaction est valide
            return
        user = interaction.user
        log_channel_id = 1231927294264606741
        await interaction.response.send_modal(CloseTicketModal(self.bot, self.salon, log_channel_id))  # Utiliser l'attribut salon

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        if interaction is None or interaction.user is None:  # Vérifiez si l'interaction est valide
            return
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)
        

class JustClose(discord.ui.View):
    def __init__(self, bot, salon):
        super().__init__()
        self.bot = bot
        self.salon = salon

    @discord.ui.button(label="Fermer le ticket", emoji="🔒", custom_id="close", style=discord.ButtonStyle.red)
    async def button1(self, interaction, button):
        if interaction is None or interaction.user is None:  # Vérifiez si l'interaction est valide
            return
        user = interaction.user
        log_channel_id = 1231927294264606741
        await interaction.response.send_modal(CloseTicketModal(self.bot, self.salon, log_channel_id))  # Utiliser l'attribut salon

    async def on_error(self, interaction: discord.Interaction, error: Exception, item: discord.ui.Item) -> None:
        if interaction is None or interaction.user is None:  # Vérifiez si l'interaction est valide
            return
        await interaction.response.send_message('Oups ! Quelque chose ne va pas.', ephemeral=True)
        traceback.print_exception(type(error), error, error.__traceback__)

class Ticket(discord.ui.Select):
    def __init__(self, bot, interaction):  
        self.bot = bot
        self.interaction = interaction  
        super().__init__(
            placeholder="Ouvre un ticket !",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(
                    label="Recrutements",
                    description="Ouvre un ticket pour te faire recruter !",
                    value='0',
                    emoji="🗒️"
                ),
                discord.SelectOption(
                    label="Partenariats",
                    description="Ouvre un ticket afin de faire un partenariat avec nous !",
                    value='1',
                    emoji="🤝"
                ),
                discord.SelectOption(
                    label="Support",
                    description="Ouvre un ticket si tu as besoin d'aide !",
                    value='2',
                    emoji="❓"
                )
            ]
        )
        
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == '0':
            category_id = 1230623083560435733
            mention_id = 1232028126150922303
        elif self.values[0] == '1':
            category_id = 1230623041629978665
            mention_id = 1232680255970349087
        elif self.values[0] == '2':
            category_id = 1230623133975974059
            mention_id = 1198232712910221342


        category = self.bot.get_channel(category_id)
        mention = self.bot.get_guild(1196194673623044286).get_role(mention_id)

        overwrites = {
            category.guild.default_role: discord.PermissionOverwrite(read_messages=False, view_channel=False),
            discord.utils.get(category.guild.roles, id=1198232712910221342): discord.PermissionOverwrite(read_messages=True, view_channel=True),
            category.guild.me: discord.PermissionOverwrite(read_messages=True, view_channel=True),
            interaction.user: discord.PermissionOverwrite(read_messages=True, view_channel=True)
        }

        ticket_channel = await category.create_text_channel(name=f"{interaction.user.name}", overwrites=overwrites)
        await interaction.response.send_message(f"{interaction.user.mention}, votre ticket a été créé avec succès dans {category.name}. Pour le retrouver, veuillez vous rendre dans {ticket_channel.mention}", ephemeral=True)
        await ticket_channel.send(mention.mention)
        await ticket_channel.purge()
        await ticket_channel.send(f"{interaction.user.mention}, votre ticket a été créé avec succès dans {category.name}.", view=ClaimTicket(self.bot, interaction.user.id, ticket_channel.id, ticket_channel))

class TicketView(discord.ui.View):
    def __init__(self, bot, interaction):  # Ajoutez 'interaction' comme argument
        self.bot = bot
        self.interaction = interaction  # Utilisez 'interaction' passé comme argument
        super().__init__()
        self.add_item(Ticket(self.bot, interaction))  # Passer 'interaction' lors de l'initialisation de Ticket


class TicketCog(commands.Cog, name="ticket"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="panel",
        description="Envoie le panel"
    )
    @commands.has_permissions(administrator=True)
    async def panel(self, ctx):  # Assurez-vous de passer 'ctx' ou toute autre interaction ici
        embed = discord.Embed(
        title="Ticket",
        description="Besoin d'aide ? Ouvrez un ticket !\n🗒️ Recrutements --> Ouvre un ticket pour être recruté !\n🤝 Partenariats --> Ouvre un ticket pour faire une collaboration !\n❓ Support --> Pose une question !", 
        color=discord.Color.blue())

        await ctx.send(view=TicketView(self.bot, ctx), embed=embed)  # Passer 'ctx' ici

async def setup(bot) -> None:
    await bot.add_cog(TicketCog(bot))