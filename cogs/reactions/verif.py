import discord
from discord import File
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

class verif(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verif", style=discord.ButtonStyle.success, custom_id='verif', emoji=discord.PartialEmoji.from_str("✅"))
    async def verif(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1106723502779809862)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Merci d'avoir accepté les règles du serveur !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Vous venez de perdre l'accès au serveur, veuillez accepter les règles pour le récuperer", ephemeral=True)
            await interaction.user.remove_roles(role)

class verification(commands.Cog):
    def __init__(self,bot):
        bot = bot
    """@commands.command()
    async def verif(self, ctx):
        view = verif()
        await ctx.send(```Bonjour et bienvenue sur le serveur Kinad's World, ce server ayant pour but de réunir les gens qui apprécie mon contenue et les différents jeu auxquels je joue, quelque règles sont évidement a respecté pour le bien d'autrui, les règles sont donc les suivantes :
1 - Soyez respectueux envers les autres membres du serveur.

2 - Pas de discours haineux, de harcèlement ou de discrimination peu importe sa forme.

3 - Pas de spam ou de publicité non sollicitée. La publicités non autorisée sera lourdement sanctionné. (allant de simple mute a ban si récidive)

4 - Utilisez les canaux appropriés pour les sujets de discussion. Ils ont été crée pour satisfaire tout en ne perdant aucune fonctionnalité, malgré ca si il vient a manquer de channels pour un sujet quelconque faites en part aux modérateurs ou a moi-même

5 - Suivez les directives de la communauté Discord et les conditions d’utilisation.

6 - Quelconque problèmes entre membres devront être réglé en privé ou bien une plainte devra être déposé aux modérateurs ou moi-même. Si une bagarre vient a éclater publiquement, les deux parties viendraient a être punies.

7 - Le Bot "KinadBot" étant propriétaire et fais a la main, il a ces failles bien évidement et si d'aventure un quelconque bug est découvert je vous prierai de vennir m'en parler directement et ne pas en abuse.

Merci a celles et ceux qui auront lus jusqu'ici, je vous prierai de bien vouloir validé la lecture et l'approbations de ces règles pour entrer sur le serveur et accéder a toutes les fonctionnalités de ce dernier en appuyant sur le bouton suivant : ```,view=view)"""
async def setup(bot):
    await bot.add_cog(verification(bot))