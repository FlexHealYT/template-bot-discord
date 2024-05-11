import platform
import random
import asyncio
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

import cours.PythonCog as PyC
import cours.JSCog as JSC
import cours.PHPCog as PHPC
import cours.HTMLCog as HTMLC
import cours.C_Cog as CC
import cours.CSSCog as CSSC


class GeneralCog(commands.Cog, name="general"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.context_menu_user = app_commands.ContextMenu(
            name="Obtenir l'ID", callback=self.grab_id
        )
        self.bot.tree.add_command(self.context_menu_user)
        self.context_menu_message = app_commands.ContextMenu(
            name="Supprimer les spoilers", callback=self.remove_spoilers
        )
        self.bot.tree.add_command(self.context_menu_message)
        
    @commands.hybrid_command(
        name="help", description="Liste toutes les commandes du bot."
    )
    async def help(self, context: Context) -> None:
        prefix = self.bot.config["prefix"]
        embed = discord.Embed(
            title="Aide", description="Liste des commandes disponibles :", color=0xBEBEFE
        )
        for cog_name in self.bot.cogs:
            if cog_name == "owner" and not await self.bot.is_owner(context.author):
                continue
            cog = self.bot.get_cog(cog_name.lower())
            if cog is not None:
                commands = cog.get_commands()
                if commands:
                    data = []
                    for command in commands:
                        description = command.description.partition("\n")[0]
                        data.append(f"/{command.name} - {description}")
                    help_text = "\n".join(data)
                    embed.add_field(
                        name=cog_name.capitalize(), value=f"```{help_text}```", inline=False
                    )
        await context.send(embed=embed, ephemeral=True)



    # Message context menu command
    async def remove_spoilers(
        self, interaction: discord.Interaction, message: discord.Message
    ) -> None:
        """
        Supprime les spoilers du message. Cette commande nécessite l'intention MESSAGE_CONTENT pour fonctionner correctement.

        :param interaction: L'interaction de la commande d'application.
        :param message: Le message avec lequel l'interaction a lieu.
        """
        spoiler_attachment = None
        for attachment in message.attachments:
            if attachment.is_spoiler():
                spoiler_attachment = attachment
                break
        embed = discord.Embed(
            title="Message sans spoilers",
            description=message.content.replace("||", ""),
            color=0xBEBEFE,
        )
        if spoiler_attachment is not None:
            embed.set_image(url=attachment.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    # User context menu command
    async def grab_id(
        self, interaction: discord.Interaction, user: discord.User
    ) -> None:
        """
        Récupère l'ID de l'utilisateur.

        :param interaction: L'interaction de la commande d'application.
        :param user: L'utilisateur avec lequel l'interaction a lieu.
        """
        embed = discord.Embed(
            description=f"L'ID de {user.mention} est `{user.id}`.",
            color=0xBEBEFE,
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="infobot",
        description="Obtenez des informations utiles (ou non) sur le bot.",
    )
    async def botinfo(self, context: Context) -> None:
        """
        Obtenez des informations utiles (ou non) sur le bot.

        :param context: Le contexte de la commande hybride.
        """
        embed = discord.Embed(
            description="Utilisé le modèle de [Krypton](https://krypton.ninja)",
            color=0xBEBEFE,
        )
        embed.set_author(name="Informations sur le bot")
        embed.add_field(name="Propriétaire :", value="flexheal_ytb#0606", inline=True)
        embed.add_field(
            name="Version Python :", value=f"{platform.python_version()}", inline=True
        )
        embed.add_field(
            name="Préfixe:",
            value=f"/ (Commandes Slash) ou {self.bot.config['prefix']} pour les commandes normales",
            inline=False,
        )
        embed.set_footer(text=f"Demandé par {context.author}")
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="infoserv",
        description="Obtenez des informations utiles (ou non) sur le serveur.",
    )
    async def serverinfo(self, context: Context) -> None:
        """
        Obtenez des informations utiles (ou non) sur le serveur.

        :param context: Le contexte de la commande hybride.
        """
        roles = [role.name for role in context.guild.roles]
        num_roles = len(roles)
        if num_roles > 50:
            roles = roles[:50]
            roles.append(f">>>> Affichage [50/{num_roles}] Rôles")
        roles = ", ".join(roles)

        embed = discord.Embed(
            title="**Nom du Serveur :**", description=f"{context.guild}", color=0xBEBEFE
        )
        if context.guild.icon is not None:
            embed.set_thumbnail(url=context.guild.icon.url)
        embed.add_field(name="ID du Serveur", value=context.guild.id)
        embed.add_field(name="Nombre de Membres", value=context.guild.member_count)
        embed.add_field(
            name="Salons Textuels/Vocaux", value=f"{len(context.guild.channels)}"
        )
        embed.add_field(name=f"Rôles ({len(context.guild.roles)})", value=roles)
        embed.set_footer(text=f"Créé le : {context.guild.created_at}")
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="ping",
        description="Vérifiez si le bot est en ligne.",
    )
    async def ping(self, context: Context) -> None:
        """
        Vérifiez si le bot est en ligne.

        :param context: Le contexte de la commande hybride.
        """
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"La latence du bot est {round(self.bot.latency * 1000)}ms.",
            color=0xBEBEFE,
        )
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="8ball",
        description="Posez n'importe quelle question au bot.",
    )
    @app_commands.describe(question="La question que vous voulez poser.")
    async def eight_ball(self, context: Context, *, question: str) -> None:
        """
        Posez n'importe quelle question au bot.

        :param context: Le contexte de la commande hybride.
        :param question: La question que l'utilisateur devrait poser.
        """
        answers = [
            "C'est certain.",
            "Il en est décidément ainsi.",
            "Vous pouvez compter dessus.",
            "Sans aucun doute.",
            "Oui - absolument.",
            "Comme je le vois, oui.",
            "Très probablement.",
            "Les perspectives sont bonnes.",
            "Oui.",
            "Les signes indiquent oui.",
            "Réessayez plus tard.",
            "Demandez à nouveau plus tard.",
            "Mieux vaut ne pas vous le dire maintenant.",
            "Impossible de prédire maintenant.",
            "Concentrez-vous et demandez à nouveau plus tard.",
            "Ne comptez pas dessus.",
            "Ma réponse est non.",
            "Mes sources disent non.",
            "Les perspectives ne semblent pas bonnes.",
            "Très douteux.",
        ]
        embed = discord.Embed(
            title="**Ma réponse :**",
            description=f"{random.choice(answers)}",
            color=0xBEBEFE,
        )
        embed.set_footer(text=f"La question était : {question}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="bitcoin",
        description="Obtenez le prix actuel du bitcoin.",
    )
    async def bitcoin(self, context: Context) -> None:
        """
        Obtenez le prix actuel du bitcoin.

        :param context: Le contexte de la commande hybride.
        """
        # Cela empêchera votre bot de tout arrêter lors de la réalisation d'une requête Web - voir: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            ) as request:
                if request.status == 200:
                    data = await request.json()  # Pour une raison quelconque, le contenu retourné est de type JavaScript
                    embed = discord.Embed(
                        title="Prix du Bitcoin",
                        description=f"Le prix actuel est de {data['bpi']['USD']['rate_float']}$ !",
                        color=0xBEBEFE,
                    )
                else:
                    embed = discord.Embed(
                        title="Erreur!",
                        description="Quelque chose ne va pas avec l'API, veuillez réessayer plus tard",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)

async def setup(bot) -> None:
    await bot.add_cog(GeneralCog(bot))
