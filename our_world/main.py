import discord
import asyncio
from discord.ext import commands
import json
from dotenv import load_dotenv
import os
from typing import List
from rich.console import Console
from rich.table import Table
from rich.text import Text
import logging
import json
import logging
import os
import platform
import random
import sys
import datetime
from datetime import datetime, timedelta
import pytz
import aiosqlite
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from dotenv import load_dotenv

from database import DatabaseManager

excluded_cogs_list = ["b_Setup_bot.py"]

def get_json(fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        return json.load(f) 

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

class LoggingFormatter(logging.Formatter):
    # Colors
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    # Styles
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red,
        logging.CRITICAL: red + bold,
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.bold)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)


logger = logging.getLogger("discord_bot")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(LoggingFormatter())
# File handler
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
)
file_handler.setFormatter(file_handler_formatter)

# Add the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or(config["prefix"]),
            intents=discord.Intents.all(),
            help_command=None,
        )
        """
        This creates custom bot variables so that we can access these variables in cogs more easily.

        For example, The config is available using the following code:
        - self.config # In this class
        - bot.config # In this file
        - self.bot.config # In cogs
        """
        self.logger = logger
        self.config = config
        self.database = None
        self.added_roles = []
        self.removed_roles = []

    
    async def TicketMsg(self):
        TicketChannel = self.get_channel(1196557781214449738)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        
        # Récupérer les messages dans le canal
        async for message in TicketChannel.history(limit=None):
            if message.author == self.user and message.embeds:
                embed = message.embeds[0]
                if embed.title == "Ticket":
                    await message.delete()  # Supprimer le message existant avec le titre "Ticket"
        
        # Envoyer le nouveau message
        embed = discord.Embed(
            title="Ticket",
            description="Besoin d'aide ? Ouvrez un ticket !\n🗒️ Recrutements --> Ouvre un ticket pour être recruté !\n🤝 Partenariats --> Ouvre un ticket pour faire une collaboration !\n❓ Support --> Pose une question !", 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            color=discord.Color.blue())
        await TicketChannel.send(embed=embed, view=TC.TicketView(self, interaction=None))


    async def on_ready(self):
        # await bot.change_presence(activity=discord.Game(name="!help"))
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/help_bot"))
        table = Table()
        
        table.add_column(f"Bot {bot.user} fonctionne parfaitement", justify="center", style="cyan", no_wrap=True)
        
        # ligne1 = Text(f"ID: {bot.user.id}", justify="center", style="bold red")
        ligne1 = Text(justify="center")
        ligne1.append("ID: ", style="bold red")
        ligne1.append(f"{bot.user.id}", style="bold Magenta")
        
        # ligne2 = Text(f"Version de Discord: {discord.__version__}", justify="center", style="bold red")
        ligne2 = Text(justify="center")
        ligne2.append("Version de Discord: ", style="bold red")
        ligne2.append(f"{discord.__version__}", style="bold Magenta")
        
        # ligne3 = Text(f"Connecté en tant que {bot.user.name} avec {len(bot.shards)} shards.", justify="center", style="bold red")
        ligne3 = Text(justify="center")
        ligne3.append("Connecté en tant que ", style="bold red")
        ligne3.append(f"{bot.user.name}", style="bold Magenta")
        ligne3.append(" avec ", style="bold red")
        # ligne3.append(f"{len(bot.shards)}", style="bold Magenta")
        # ligne3.append(" shards.", style="bold red")
        
        table.add_row(ligne1)
        table.add_row(ligne2)
        table.add_row(ligne3,end_section=True)
        # ajout d'une ligne de séparation --------------------

        # ligne4 = Text(f"Actuellement sur {len(bot.guilds)} serveurs:", justify="left", style="bold blue")
        ligne4 = Text(justify="left")
        ligne4.append("Actuellement sur ", style="bold blue")
        ligne4.append(f"{len(bot.guilds)}", style="bold cyan")
        ligne4.append(" serveurs:", style="bold blue")
        table.add_row(ligne4)

        for server in bot.guilds:
            # ligne5 = Text(f" - {server.name} (ID: {server.id})", justify="left", style="bold blue")
            ligne5 = Text(justify="left")
            ligne5.append(" - ", style="bold blue")
            ligne5.append(server.name, style="bold cyan")
            ligne5.append(f" (ID: ", style="bold blue")
            ligne5.append(f"{server.id}", style="bold cyan")
            ligne5.append(")", style="bold blue")
            table.add_row(ligne5)
        table.add_row(end_section=True)
        # for server in bot.guilds:
        #     table.add_row(f" - {server.name} (ID: {server.id})",end_section=True)
        await self.load_cogs(self, table, excluded_cogs_list)
        
        
        ligne10 = Text(f"Syncing slash commands:", justify="left", style="bold dark_yellow")
        try:
            synced = await bot.tree.sync()
            # Liste all slash commands
            table.add_row(ligne10)  # Ajouter l'en-tête une fois avant la boucle

            for command in synced:
                ligne11 = Text(justify="left")
                ligne11.append(" - ", style="bold dark_yellow")
                ligne11.append(command.name, style="bold bright_yellow")
                ligne11.append(" (ID: ", style="bold dark_yellow")
                ligne11.append(f"{command.id}", style="bold bright_yellow")
                ligne11.append(")", style="bold dark_yellow")
                
                table.add_row(ligne11)  # Ajouter chaque commande dans la boucle

            table.add_row(end_section=True)  # Fin de section après la boucle
        except Exception as e:
            print(e)
            
        await self.start_task_after_table_display(bot)
        await self.TicketMsg()
        console = Console()
        console.print(table)



    async def start_task_after_table_display(self, bot: commands.AutoShardedBot):
        my_cog_instance = bot.get_cog('tasks')
        if my_cog_instance:
            my_cog_instance.message_send_task.start()  # Démarrage de la tâche après l'affichage du tableau


    async def init_db(self) -> None:
        async with aiosqlite.connect(
            f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
        ) as db:
            with open(
                f"{os.path.realpath(os.path.dirname(__file__))}/database/schema.sql"
            ) as file:
                await db.executescript(file.read())
            await db.commit()

    async def load_cogs(self, bot, table, excluded_cogs):
        ligne6 = Text(f"Chargement des cogs:", justify="left", style="bold green")
        table.add_row(ligne6)
        for filename in os.listdir('./cogs'):
            if (filename in excluded_cogs):
                continue
            if (filename.endswith('.py') and not filename.startswith('__') and 
                not any(excluded_string in filename for excluded_string in excluded_cogs)):
                cog_name = filename[:-3]  # Retirer .py
                try:
                    # Importer le module du cog
                    cog_module = __import__(f"cogs.{cog_name}", fromlist=[cog_name])
                    
                    # Obtenir la classe du cog
                    cog_class = getattr(cog_module, cog_name, None)
                    
                    # Vérifier si la classe du cog existe et l'ajouter au bot
                    if callable(cog_class):
                        await bot.add_cog(cog_class(bot))
                        ligne6 = Text(justify="left")
                        ligne6.append(" - ", style="bold green")
                        ligne6.append(f"{cog_name}", style="bold green3s")
                        ligne6.append(" chargé avec succès", style="bold green")
                    else:
                        raise Exception(f"Le cog {cog_name} n'a pas de classe correspondante.")
                    
                    table.add_row(ligne6)
                except Exception as e:
                    ligne7 = Text(justify="left")
                    ligne7.append(" - ", style="bold red")
                    ligne7.append(f"{cog_name}", style="bold bright_red")
                    ligne7.append(" n'a pas pu être chargé: ", style="bold red")
                    ligne7.append(str(e), style="bold bright_red")
                    table.add_row(ligne7)
                    print(e)


    @tasks.loop(minutes=1.0)
    async def status_task(self) -> None:
        """
        Setup the game status task of the bot.
        """
        statuses = ["/help"]
        await self.change_presence(activity=discord.Game(random.choice(statuses)))

    @status_task.before_loop
    async def before_status_task(self) -> None:
        """
        Before starting the status changing task, we make sure the bot is ready
        """
        await self.wait_until_ready()

    async def setup_hook(self) -> None:
        """
        This will just be executed when the bot starts the first time.
        """
        self.logger.info(f"Logged in as {self.user.name}")
        self.logger.info(f"discord.py API version: {discord.__version__}")
        self.logger.info(f"Python version: {platform.python_version()}")
        self.logger.info(
            f"Running on: {platform.system()} {platform.release()} ({os.name})"
        )
        self.logger.info("-------------------")
        await self.init_db()
        self.status_task.start()
        self.database = DatabaseManager(
            connection=await aiosqlite.connect(
                f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
            )
        )

    async def on_message(self, message: discord.Message) -> None:
        """
        The code in this event is executed every time someone sends a message, with or without the prefix

        :param message: The message that was sent.
        """
        if message.author == self.user:
            return

        if message.content.startswith("!"):
            await message.delete()

        if message.channel == bot.get_channel(1229912237091852339):
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            await message.channel.send("<@&1229528607786008626>")
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        if message.author.id == 302050872383242240:  # ID de Disboard
 # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
           if message.channel == bot.get_channel(1229180297346809967): # salon de bump
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                current_time = datetime.now(pytz.utc) + timedelta(seconds=7200)
                timestamp = int(current_time.timestamp())
                await message.channel.send(f"Il sera temps de bumper dans <t:{timestamp}:R>")
                print("Le serveur vient d'être bumpé")
                await asyncio.sleep(7200)  # Attendre 2 heures (7200 secondes)
                await message.channel.send(f"<@1124611079855673355>, <@694873777942691920>, il est temps de bumper à nouveau !")
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        await self.process_commands(message)
        
    async def on_command_completion(self, context: Context) -> None:
        """
        The code in this event is executed every time a normal command has been *successfully* executed.

        :param context: The context of the command that has been executed.
        """
        full_command_name = context.command.qualified_name
        split = full_command_name.split(" ")
        executed_command = str(split[0])
        if context.guild is not None:
            self.logger.info(
                f"Executed {executed_command} command in {context.guild.name} (ID: {context.guild.id}) by {context.author} (ID: {context.author.id})"
            )
        else:
            self.logger.info(
                f"Executed {executed_command} command by {context.author} (ID: {context.author.id}) in DMs"
            )

    async def on_command_error(self, context: Context, error) -> None:
        """
        The code in this event is executed every time a normal valid command catches an error.

        :param context: The context of the normal command that failed executing.
        :param error: The error that has been faced.
        """
        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(error.retry_after, 60)
            hours, minutes = divmod(minutes, 60)
            hours = hours % 24
            embed = discord.Embed(
                description=f"**Please slow down** - You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                description="You are not the owner of the bot!", color=0xE02B2B
            )
            await context.send(embed=embed)
            if context.guild:
                self.logger.warning(
                    f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the guild {context.guild.name} (ID: {context.guild.id}), but the user is not an owner of the bot."
                )
            else:
                self.logger.warning(
                    f"{context.author} (ID: {context.author.id}) tried to execute an owner only command in the bot's DMs, but the user is not an owner of the bot."
                )
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description="You are missing the permission(s) `"
                + ", ".join(error.missing_permissions)
                + "` to execute this command!",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                description="I am missing the permission(s) `"
                + ", ".join(error.missing_permissions)
                + "` to fully perform this command!",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Error!",
                # We need to capitalize because the command arguments have no capital letter in the code and they are the first word in the error message.
                description=str(error).capitalize(),
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        else:
            raise error

    async def on_message_delete(self, message: discord.Message):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est supprimé.

        :param message: Le message qui a été supprimé.
        """
        author_id = message.author.id
        author_mention = message.author.mention
        content = message.content
        channel_name = message.channel.name
        channel_mention = message.channel.mention
        print(f"Message supprimé - Contenu: {content}, Auteur ID: {author_id}  /  {message.author.name}, Salon: {channel_name}")
        embed = discord.Embed(
            title="Message supprimé !",
            description=f"Contenu : {content}\nAuteur : {author_id}  /  {author_mention}\nSalon : {channel_mention}",
            color=0xff0000
            )
        if not content.startswith("!") or not message.channel.id in [1231276908759613521, 1232049659757727896]:
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            await self.get_channel(1231276908759613521).send(embed=embed)

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est modifié.

        :param before: Le message avant la modification.
        :param after: Le message après la modification.
        """
        # Vérifie si l'auteur du message avant la modification est un bot
        if before.author.bot:
            return
        
        author_id = before.author.id
        author_mention = before.author.mention
        content_before = before.content
        content_after = after.content
        channel_name = before.channel.name
        channel_mention = before.channel.mention
        print(f"Message modifié - Contenu avant: {content_before}, Contenu après: {content_after}, Auteur ID: {author_id}  /  {before.author.name}, Salon: {channel_name}")
        embed = discord.Embed(
            title="Message modifié !",
            description=f"Contenu avant : {content_before}\nContenu après : {content_after}\nAuteur : {author_id}  /  {author_mention}\nSalon : {channel_mention}",
            color=0xff0000
            )
        await self.get_channel(1231276908759613521).send(embed=embed)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est modifié.

        :param before: Le message avant la modification.
        :param after: Le message après la modification.
        """

        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            if entry.target == user:
                print(f"Utilisateur banni - {user.id}  /  {user.name} à été banni de {guild.name} par {entry.user}")
                embed = discord.Embed(
                    title="Utilisateur banni !",
                    description=f"{user.id}  /  {user.mention} à été banni de {guild.name} par {entry.user}",
                    color=0xff0000
                    )
                await self.get_channel(1231276908759613521).send(embed=embed)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        """
        Le code de cet événement est exécuté chaque fois qu'un message est modifié.

        :param before: Le message avant la modification.
        :param after: Le message après la modification.
        """
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.unban):
            if entry.target == user:
                print(f"Utilisateur débanni - {user.id}  /  {user.name} à été débanni de {guild.name} par {entry.user}")
                embed = discord.Embed(
                    title="Utilisateur débanni !",
                    description=f"{user.id}  /  {user.mention} à été débanni de {guild.name} par {entry.user}",
                    color=0xff0000
                    )
                await self.get_channel(1231276908759613521).send(embed=embed)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 1232081955605184616:  # ID du message embed
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            emoji = str(payload.emoji)

            roles_emojis = {
                '<:c_:1232075318345597020>': 1231952778553987215,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:css:1232074095986872360>': 1231952923366264863,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:python:1232075302398591046>': 1231952273492672593,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:php:1232075285629763675>': 1232048720623702077,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:html:1232069038386057338>': 1231952881100263434,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:js:1232072012411961458>': 1231952694697267229
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            }

            role_id = roles_emojis.get(emoji)
            if role_id:
                role = guild.get_role(role_id)
                await member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 1232081955605184616:  # ID du message embed
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            emoji = str(payload.emoji)

            roles_emojis = {
                '<:c_:1232075318345597020>': 1231952778553987215,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:css:1232074095986872360>': 1231952923366264863,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:python:1232075302398591046>': 1231952273492672593,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:php:1232075285629763675>': 1232048720623702077,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:html:1232069038386057338>': 1231952881100263434,
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                '<:js:1232072012411961458>': 1231952694697267229
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            }

            role_id = roles_emojis.get(emoji)
            if role_id:
                role = guild.get_role(role_id)
                await member.remove_roles(role)

load_dotenv()

bot = DiscordBot()
bot.run("MTIyODM5ODMyODY1NjU2NDM3NQ.GFBbua.YRDqM-CjgHNIAOVqLoCQBnN8PBTh99OHauhppU")
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
