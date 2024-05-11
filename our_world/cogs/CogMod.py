import os
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


class CogMod(commands.Cog, name="modération"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="kick",
        description="Expulse l'utilisateur du serveur.",
    )
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @app_commands.describe(
        utilisateur="L'utilisateur que vous voulez expulser.",
        reason="La raison de l'expulsion.",
    )
    async def expulser(
        self, context: Context, utilisateur: discord.User, *, reason: str = "Non précisé"
    ) -> None:
        """
        Expulse un utilisateur du serveur.

        :param context: Le contexte de la commande hybride.
        :param utilisateur: L'utilisateur qui devrait être expulsé du serveur.
        :param reason: La reason de l'expulsion. Par défaut, "Non précisé".
        """
        membre = context.guild.get_member(utilisateur.id) or await context.guild.fetch_member(
            utilisateur.id
        )
        if membre.guild_permissions.administrator:
            embed = discord.Embed(
                description="L'utilisateur a les permissions d'administrateur.", color=0xE02B2B
            )
            await context.send(embed=embed, ephemeral=True)
        else:
            try:
                embed = discord.Embed(
                    description=f"**{membre}** a été expulsé par **{context.author}**!",
                    color=0xBEBEFE,
                )
                embed.add_field(name="reason :", value=reason)
                await context.send(embed=embed, ephemeral=True)
                await self.bot.get_channel(1232061261898846328).send(embed=embed)
                try:
                    await membre.send(
                        f"Vous avez été expulsé par **{context.author}** de **{context.guild.name}**!\nreason : {reason}"
                    )
                except:
                    # Impossible d'envoyer un message dans les messages privés de l'utilisateur
                    pass
                await membre.kick(reason=reason)
            except:
                embed = discord.Embed(
                    description="Une erreur s'est produite lors de la tentative d'expulsion de l'utilisateur. Assurez-vous que mon rôle est supérieur à celui de l'utilisateur que vous souhaitez exclure..",
                    color=0xE02B2B,
                )
                await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="nick",
        description="Modifier le surnom d'un utilisateur sur un serveur.",
    )
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    @app_commands.describe(
        utilisateur="L'utilisateur qui doit avoir un nouveau surnom.",
        surnom="Le nouveau pseudo qui doit être défini.",
    )
    async def surnom(
        self, context: Context, utilisateur: discord.User, *, surnom: str = None
    ) -> None:
        """
        Change le surnom d'un utilisateur sur un serveur.

        :param context: Le contexte de la commande hybride.
        :param utilisateur: L'utilisateur dont le surnom doit être changé.
        :param surnom: Le nouveau surnom de l'utilisateur. Par défaut, None, ce qui réinitialisera le surnom.
        """
        membre = context.guild.get_member(utilisateur.id) or await context.guild.fetch_member(
            utilisateur.id
        )
        try:
            await membre.edit(nick=surnom)
            embed = discord.Embed(
                description=f"Le nouveau surnom de **{membre}** est **{surnom}** !",
                color=0xBEBEFE,
            )
            await context.send(embed=embed, ephemeral=True)
        except:
            embed = discord.Embed(
                description="Une erreur s'est produite lors de la modification du pseudonyme de l'utilisateur. Assurez-vous que mon rôle est supérieur à celui de l'utilisateur dont vous souhaitez modifier le pseudonyme.",
                color=0xE02B2B,
            )
            await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="ban",
        description="Bannis l'utilisateur de ce serveur.",
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @app_commands.describe(
        user="L'utilisateur qui devrait être banni.",
        reason="La raison pour laquelle l'utilisateur doit être banni.",
    )
    async def bannir(
        self, context: Context, user: discord.User, *, reason: str = "Non précisée"
    ) -> None:
        """
        Bannis un utilisateur du serveur.

        :param context: Le contexte de la commande hybride.
        :param utilisateur: L'utilisateur qui devrait être banni du serveur.
        :param reason: La reason du bannissement. Par défaut, "Non précisée".
        """
        membre = context.guild.get_member(user.id) or await context.guild.fetch_member(
            user.id
        )
        try:
            if membre.guild_permissions.administrator:
                embed = discord.Embed(
                    description="L'utilisateur a des droits d'administrateur.", color=0xE02B2B
                )
                await context.send(embed=embed, ephemeral=True)
            else:
                embed = discord.Embed(
                    description=f"**{membre}** a été banni par **{context.author}**!",
                    color=0xBEBEFE,
                )
                embed.add_field(name="reason:", value=reason)
                print(f"Utilisateur banni - {user.id}  /  {user.name} à été banni de {context.guild.name} par {context.user} pour la raison suivante : {reason}")
                await context.send(embed=embed, ephemeral=True)
                await self.bot.get_channel(1232061261898846328).send(embed=embed)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                try:
                    await membre.send(
                        f"Tu as été banni par **{context.author}** de **{context.guild.name}**!\nreason: {reason}"
                    )
                except:
                    # Impossible d'envoyer un message dans les messages privés de l'utilisateur
                    pass
                await membre.ban(reason=reason)
        except:
            embed = discord.Embed(
                title="Erreur!",
                description="Une erreur s'est produite lors de la tentative de bannissement de l'utilisateur. Assurez-vous que mon rôle est supérieur à celui de l'utilisateur que vous souhaitez bannir.",
                color=0xE02B2B,
            )
            await context.send(embed=embed, ephemeral=True)


    @commands.hybrid_group(
        name="warn",
        description="Gérer les avertissements d'un utilisateur sur un serveur.",
    )
    @commands.has_permissions(manage_messages=True)
    async def avertissement(self, context: Context) -> None:
        """
        Gérer les avertissements d'un utilisateur sur un serveur.

        :param context: Le contexte de la commande hybride.
        """
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                description="Veuillez spécifier une sous-commande.\n\n**Sous-commandes:**\n`ajouter` - Ajouter un avertissement à un utilisateur.\n`supprimer` - Supprimer un avertissement d'un utilisateur.\n`liste` - Lister tous les avertissements d'un utilisateur.",
                color=0xE02B2B,
            )
            await context.send(embed=embed, ephemeral=True)

    @avertissement.command(
        name="add",
        description="Ajoute un avertissement à un utilisateur sur le serveur.",
    )
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        utilisateur="L'utilisateur qui devrait être averti.",
        reason="La raison pour laquelle l'utilisateur devrait être averti.",
    )
    async def avertissement_ajouter(
        self, context: Context, utilisateur: discord.User, *, reason: str = "Non précisée"
    ) -> None:
        """
        Avertissement d'un utilisateur dans ses messages privés.

        :param context: Le contexte de la commande hybride.
        :param utilisateur: L'utilisateur qui devrait être averti.
        :param reason: La reason de l'avertissement. Par défaut, "Non précisée".
        """
        membre = context.guild.get_member(utilisateur.id) or await context.guild.fetch_member(
            utilisateur.id
        )
        total = await self.bot.database.add_warn(
            utilisateur.id, context.guild.id, context.author.id, reason
        )
        embed = discord.Embed(
            description=f"**{membre}** a été averti par **{context.author}**!\nTotal des avertissements pour cet utilisateur : {total}",
            color=0xBEBEFE,
        )
        embed.add_field(name="reason:", value=reason)
        await context.send(embed=embed, ephemeral=True)
        await self.bot.get_channel(1232061261898846328).send(embed=embed)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        try:
            await membre.send(
                f"Vous avez été averti par **{context.author}** dans **{context.guild.name}**!\nreason: {reason}"
            )
        except:
            # Impossible d'envoyer un message dans les messages privés de l'utilisateur
            await context.send(
                f"{membre.mention}, vous avez été averti par **{context.author}**!\nreason: {reason}"
            )


    @avertissement.command(
        name="delete",
        description="Supprime un avertissement d'un utilisateur sur le serveur.",
    )
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        utilisateur="L'utilisateur dont l'avertissement doit être supprimé.",
        id_avertissement="L'ID de l'avertissement qui doit être supprimé.",
    )
    async def avertissement_supprimer(
        self, context: Context, utilisateur: discord.User, id_avertissement: int
    ) -> None:
        """
        Avertissement d'un utilisateur dans ses messages privés.

        :param context: Le contexte de la commande hybride.
        :param utilisateur: L'utilisateur dont l'avertissement doit être supprimé.
        :param id_avertissement: L'ID de l'avertissement qui doit être supprimé.
        """
        membre = context.guild.get_member(utilisateur.id) or await context.guild.fetch_member(
            utilisateur.id
        )
        total = await self.bot.database.remove_warn(id_avertissement, utilisateur.id, context.guild.id)
        embed = discord.Embed(
            description=f"J'ai supprimé l'avertissement **#{id_avertissement}** de **{membre}**!\nTotal des avertissements pour cet utilisateur : {total}",
            color=0xBEBEFE,
        )
        await context.send(embed=embed, ephemeral=True)
        await self.bot.get_channel(1232061261898846328).send(embed=embed)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    @avertissement.command(
        name="list",
        description="Affiche les avertissements d'un utilisateur sur le serveur.",
    )
    @commands.has_guild_permissions(manage_messages=True)
    @app_commands.describe(utilisateur="L'utilisateur dont vous voulez obtenir les avertissements.")
    async def avertissement_liste(self, context: Context, utilisateur: discord.User) -> None:
        """
        Affiche les avertissements d'un utilisateur sur le serveur.

        :param context: Le contexte de la commande hybride.
        :param utilisateur: L'utilisateur dont vous voulez obtenir les avertissements.
        """
        liste_avertissements = await self.bot.database.get_warnings(utilisateur.id, context.guild.id)
        embed = discord.Embed(title=f"Avertissements de {utilisateur}", color=0xBEBEFE)
        description = ""
        if len(liste_avertissements) == 0:
            description = "Cet utilisateur n'a aucun avertissement."
        else:
            for avertissement in liste_avertissements:
                description += f"• Averti par <@{avertissement[2]}>: **{avertissement[3]}** (<t:{avertissement[4]}>>) - ID de l'avertissement #{avertissement[5]}\n"
        embed.description = description
        await context.send(embed=embed, ephemeral=True)


    @commands.hybrid_command(
        name="supprimer-message",
        description="Supprime un nombre de messages.",
    )
    @commands.has_guild_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @app_commands.describe(montant="Le nombre de messages qui doivent être supprimés.")
    async def purge(self, context: Context, montant: int) -> None:
        """
        Supprime un nombre de messages.

        :param context: Le contexte de la commande hybride.
        :param amount: Le nombre de messages qui doivent être supprimés.
        """
        messages_purgés = await context.channel.purge(limit=montant)
        embed = discord.Embed(
            description=f"**{context.author}** a effacé **{len(messages_purgés)}** messages!",
            color=0xBEBEFE,
        )
        await context.send(embed=embed, ephemeral=True)


    @commands.hybrid_command(
        name="ban-hors-serv",
        description="Bannis un utilisateur sans que l'utilisateur ne soit dans le serveur.",
    )
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @app_commands.describe(
        user_id="L'ID de l'utilisateur qui devrait être banni.",
        reason="La raison pour laquelle l'utilisateur devrait être banni.",
    )
    async def bannir_hack(
        self, context: Context, user_id: str, *, reason: str = "Non spécifiée"
    ) -> None:
        """
        Bannis un utilisateur sans que l'utilisateur ne soit dans le serveur.

        :param context: Le contexte de la commande hybride.
        :param user_id: L'ID de l'utilisateur qui devrait être banni.
        :param reason: La reason du bannissement. Par défaut, "Non spécifiée".
        """
        try:
            await self.bot.http.ban(user_id, context.guild.id, reason=reason)
            utilisateur = self.bot.get_user(int(user_id)) or await self.bot.fetch_user(
                int(user_id)
            )
            embed = discord.Embed(
                description=f"**{utilisateur}** (ID: {user_id}) a été banni par **{context.author}**!",
                color=0xBEBEFE,
            )
            embed.add_field(name="reason:", value=reason)
            await context.send(embed=embed, ephemeral=True)
        except Exception:
            embed = discord.Embed(
                description="Une erreur s'est produite lors de la tentative de bannissement de l'utilisateur. Assurez-vous que l'ID existe et appartient à un utilisateur.",
                color=0xE02B2B,
            )
            await context.send(embed=embed, ephemeral=True)
            await self.bot.get_channel(1232061261898846328).send(embed=embed)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    @commands.hybrid_command(
        name="archive",
        description="Archive dans un fichier texte les derniers messages avec une limite choisie de messages.",
    )
    @commands.has_permissions(manage_messages=True)
    @app_commands.describe(
        limite="La limite de messages qui doivent être archivés.",
    )
    async def archive(self, context: Context, limite: int = 10) -> None:
        """
        Archive dans un fichier texte les derniers messages avec une limite choisie de messages. Cette commande nécessite l'intent MESSAGE_CONTENT pour fonctionner correctement.

        :param limite: La limite de messages qui doivent être archivés. Par défaut, 10.
        """
        fichier_journal = f"{context.channel.id}.log"
        with open(fichier_journal, "w", encoding="UTF-8") as f:
            f.write(
                f'Messages archivés depuis : #{context.channel} ({context.channel.id}) dans la guilde "{context.guild}" ({context.guild.id}) à {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n'
            )
            async for message in context.channel.history(
                limit=limite, before=context.message
            ):
                pièces_jointes = []
                for pièce_jointe in message.attachments:
                    pièces_jointes.append(pièce_jointe.url)
                texte_pièces_jointes = (
                    f"[Fichier{'s' if len(pièces_jointes) >= 2 else ''} joint{'s' if len(pièces_jointes) >= 2 else ''}: {', '.join(pièces_jointes)}]"
                    if len(pièces_jointes) >= 1
                    else ""
                )
                f.write(
                    f"{message.created_at.strftime('%d.%m.%Y %H:%M:%S')} {message.author} {message.id}: {message.clean_content} {texte_pièces_jointes}\n"
                )
        f = discord.File(fichier_journal)
        await context.send(file=f)
        os.remove(fichier_journal)


async def setup(bot) -> None:
    await bot.add_cog(CogMod(bot))
