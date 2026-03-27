import discord
from discord import File
from discord.ext import commands
from discord import app_commands
import discord.gateway
from discord.ui import Button, View


##séléction poste league of legends
class roleview(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Top", style=discord.ButtonStyle.success, custom_id='top', emoji=discord.PartialEmoji.from_str("top:1357373482408874134"))
    async def top(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1352138787089682484)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    @discord.ui.button(label="Jungle", style=discord.ButtonStyle.success, custom_id='jungle', emoji=discord.PartialEmoji.from_str("jungle:1358899231217418340"))
    async def jungle(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1352138818400288778)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    @discord.ui.button(label="Mid", style=discord.ButtonStyle.success, custom_id='mid', emoji=discord.PartialEmoji.from_str("mid:1358899254852321321"))
    async def mid(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1352138840755798077)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    @discord.ui.button(label="Adc", style=discord.ButtonStyle.success, custom_id='adc', emoji=discord.PartialEmoji.from_str("adc:1358899266491256993"))
    async def adc(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1352138860921880606)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    @discord.ui.button(label="Support", style=discord.ButtonStyle.success, custom_id='supp', emoji=discord.PartialEmoji.from_str("supp:1358899277761478900"))
    async def support(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1352138874238799914)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

class rolecommand(commands.Cog):
    def __init__(self,bot):
        bot = bot
        
    @commands.command()
    async def role(self, ctx):
        view = roleview()
        EmbedRole = discord.Embed(title="Role", color=0xa678de)
        EmbedRole.add_field(name = "", value="Met en avant ta lande de coeur en sélectionnant le rôle adapté, tu pourras t'en servir pour trouver un/des duos :")
        await ctx.send(embed=EmbedRole,view=view)
        
async def setup(bot):
    await bot.add_cog(rolecommand(bot))