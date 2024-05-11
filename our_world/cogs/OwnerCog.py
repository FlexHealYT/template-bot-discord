import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


class OwnerCog(commands.Cog, name="owner"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(
        name="sync",
        description="Synchronise les commandes slash.",
    )
    @app_commands.describe(scope="La portée de la synchronisation. Peut être `global` ou `guild`")
    @commands.is_owner()
    async def sync(self, context: Context, scope: str) -> None:
        """
        Synchronise les commandes slash.

        :param context: Le contexte de la commande.
        :param scope: La portée de la synchronisation. Peut être `global` ou `guild`.
        """

        if scope == "global":
            await context.bot.tree.sync()
            embed = discord.Embed(
                description="Les commandes slash ont été synchronisées globalement.",
                color=0xBEBEFE,
            )
            await context.send(embed=embed, ephemeral=True)
            return
        elif scope == "guild":
            context.bot.tree.copy_global_to(guild=context.guild)
            await context.bot.tree.sync(guild=context.guild)
            embed = discord.Embed(
                description="Les commandes slash ont été synchronisées dans cette guilde.",
                color=0xBEBEFE,
            )
            await context.send(embed=embed, ephemeral=True)
            return
        embed = discord.Embed(
            description="La portée doit être `global` ou `guild`.", color=0xE02B2B
        )
        await context.send(embed=embed, ephemeral=True)

    @commands.command(
        name="unsync",
        description="Désynchronise les commandes slash.",
    )
    @app_commands.describe(
        scope="La portée de la synchronisation. Peut être `global`, `current_guild` ou `guild`"
    )
    @commands.is_owner()
    async def unsync(self, context: Context, scope: str) -> None:
        """
        Désynchronise les commandes slash.
    @commands.command(
        name="
        :param context: Le contexte de la commande.
        :param scope: La portée de la synchronisation. Peut être `global`, `current_guild` ou `guild`.
        """

        if scope == "global":
            context.bot.tree.clear_commands(guild=None)
            await context.bot.tree.sync()
            embed = discord.Embed(
                description="Les commandes slash ont été désynchronisées globalement.",
                color=0xBEBEFE,
            )
            await context.send(embed=embed, ephemeral=True)
            return
        elif scope == "guild":
            context.bot.tree.clear_commands(guild=context.guild)
            await context.bot.tree.sync(guild=context.guild)
            embed = discord.Embed(
                description="Les commandes slash ont été désynchronisées dans cette guilde.",
                color=0xBEBEFE,
            )
            await context.send(embed=embed, ephemeral=True)
            return
        embed = discord.Embed(
            description="La portée doit être `global` ou `guild`.", color=0xE02B2B
        )
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="load",
        description="Charge un module.",
    )
    @app_commands.describe(cog="Le nom du module à charger")
    @commands.is_owner()
    async def load(self, context: Context, cog: str) -> None:
        """
        Le bot chargera le module donné.

        :param context: Le contexte de la commande hybride.
        :param cog: Le nom du module à charger.
        """
        try:
            await self.bot.load_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                description=f"Impossible de charger le module `{cog}`.", color=0xE02B2B
            )
            await context.send(embed=embed, ephemeral=True)
            return
        embed = discord.Embed(
            description=f"Le module `{cog}` a été chargé avec succès.", color=0xBEBEFE
        )
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="unload",
        description="Décharge un module.",
    )
    @app_commands.describe(cog="Le nom du module à décharger")
    @commands.is_owner()
    async def unload(self, context: Context, cog: str) -> None:
        """
        Le bot déchargera le module donné.

        :param context: Le contexte de la commande hybride.
        :param cog: Le nom du module à décharger.
        """
        try:
            await self.bot.unload_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                description=f"Impossible de décharger le module `{cog}`.", color=0xE02B2B
            )
            await context.send(embed=embed, ephemeral=True)
            return
        embed = discord.Embed(
            description=f"Le module `{cog}` a été déchargé avec succès.", color=0xBEBEFE
        )
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="reload",
        description="Recharge un module.",
    )
    @app_commands.describe(cog="Le nom du module à recharger")
    @commands.is_owner()
    async def reload(self, context: Context, cog: str) -> None:
        """
        Le bot rechargera le module donné.

        :param context: Le contexte de la commande hybride.
        :param cog: Le nom du module à recharger.
        """
        try:
            await self.bot.reload_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                description=f"Impossible de recharger le module `{cog}`.", color=0xE02B2B
            )
            await context.send(embed=embed, ephemeral=True)
            return
        embed = discord.Embed(
            description=f"Le module `{cog}` a été rechargé avec succès.", color=0xBEBEFE
        )
        await context.send(embed=embed, ephemeral=True)

    @commands.hybrid_command(
        name="shutdown",
        description="Éteint le bot.",
    )
    @commands.is_owner()
    async def shutdown(self, context: Context) -> None:
        """
        Éteint le bot.

        :param context: Le contexte de la commande hybride.
        """
        embed = discord.Embed(description="Extinction. Au revoir ! :wave:", color=0xBEBEFE)
        await context.send(embed=embed, ephemeral=True)
        await self.bot.close()

    @commands.hybrid_command(
        name="say",
        description="Le bot répétera ce que vous voulez.",
    )
    @app_commands.describe(message="Le message que le bot doit répéter")
    @commands.is_owner()
    async def say(self, context: Context, *, message: str) -> None:
        """
        Le bot répétera ce que vous voulez.

        :param context: Le contexte de la commande hybride.
        :param message: Le message que le bot doit répéter.
        """
        await context.send(message)

    @commands.hybrid_command(
        name="embed",
        description="Le bot répétera ce que vous voulez, mais dans des embeds.",
    )
    @app_commands.describe(message="Le message que le bot doit répéter")
    @commands.is_owner()
    async def embed(self, context: Context, *, message: str) -> None:
        """
        Le bot répétera ce que vous voulez, mais en utilisant des embeds.

        :param context: Le contexte de la commande hybride.
        :param message: Le message que le bot doit répéter.
        """
        embed = discord.Embed(description=message, color=0xBEBEFE)
        await context.send(embed=embed)

    @commands.hybrid_command(name="cours", description="Envoie le message des cours")
    @commands.is_owner()
    async def create_embed(self, ctx: Context):
        embed = discord.Embed(title="Roles", description="Réagissez avec les emojis correspondant aux languages que vous voulez apprendre", color=0x00ff00)
        roles_emojis = {
            '<:c_:1232075318345597020>': 1231952778553987215,
            '<:css:1232074095986872360>': 1231952923366264863,
            '<:python:1232075302398591046>': 1231952273492672593,
            '<:php:1232075285629763675>': 1232048720623702077,
            '<:html:1232069038386057338>': 1231952881100263434,
            '<:js:1232072012411961458>': 1231952694697267229
        }
        
        for emoji, role_id in roles_emojis.items():
            embed.add_field(name=emoji, value=f"<@&{role_id}>", inline=True)

        message = await ctx.send(embed=embed)

        for emoji in roles_emojis.keys():
            await message.add_reaction(emoji)


async def setup(bot) -> None:
    await bot.add_cog(OwnerCog(bot))
