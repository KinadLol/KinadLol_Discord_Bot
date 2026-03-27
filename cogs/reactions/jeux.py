import discord
from discord import File
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

class jeuxview(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Lol", style=discord.ButtonStyle.success, custom_id='lol', emoji=discord.PartialEmoji.from_str("Lol:1376770929060876288"))
    async def lol(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1109855795048353864)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    @discord.ui.button(label="Rocket League", style=discord.ButtonStyle.success, custom_id='rl', emoji=discord.PartialEmoji.from_str("RL:1376770749934866472"))
    async def rl(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1109855875734192200)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    @discord.ui.button(label="Valorant", style=discord.ButtonStyle.success, custom_id='valorant', emoji=discord.PartialEmoji.from_str("Valorant:1376770879358505053"))
    async def valo(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1109855845195460678)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    @discord.ui.button(label="Brawlhalla", style=discord.ButtonStyle.success, custom_id='bh', emoji=discord.PartialEmoji.from_str("BH:1376770781882749031"))
    async def Bh(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1110573952025239652)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

class jeuxcommand(commands.Cog):
    def __init__(self,bot):
        bot = bot
        
    @commands.command()
    async def jeux(self, ctx):
        view = jeuxview()
        Embedjeux = discord.Embed(title="Role", color=0xa678de)
        Embedjeux.add_field(name = "", value="Pour compléter vos rôles vous pouvez sélectionnez les jeux auxquels vous jouez :")
        await ctx.send(embed=Embedjeux,view=view)
        
async def setup(bot):
    await bot.add_cog(jeuxcommand(bot))