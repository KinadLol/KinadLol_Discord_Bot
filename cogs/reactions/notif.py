import discord
from discord import File
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

moi = 687334620974284904


class notifview(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def addrole(role, test:discord.Interaction):
        print(test)
        if role not in test.user.roles:
            await test.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await test.user.add_roles(role)
        else:
            await test.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await test.user.remove_roles(role)

    ##Notif Twitch
    @discord.ui.button(label="Twitch", style=discord.ButtonStyle.success, custom_id='twitch', emoji=discord.PartialEmoji.from_str("Twitch:1376770829198688328"))
    async def twitch(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1106723385687416932)
        await self.addrole(role, interaction)

    ##Notif Youtube
    @discord.ui.button(label="Youtube", style=discord.ButtonStyle.success, custom_id='youtube', emoji=discord.PartialEmoji.from_str("Youtube:1376771003216167084"))
    async def youtube(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1106723417358602321)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    ##Notif Twitter
    @discord.ui.button(label="Twitter", style=discord.ButtonStyle.success, custom_id='twitter', emoji=discord.PartialEmoji.from_str("Twitter:1376770903936864307"))
    async def twitter(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1110162296656891914)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

    ##Notif Instagram
    @discord.ui.button(label="Instagram", style=discord.ButtonStyle.success, custom_id='insta', emoji=discord.PartialEmoji.from_str("Insta:1376770852674342912"))
    async def insta(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        role = guild.get_role(1110162258098663565)
        if role not in interaction.user.roles:
            await interaction.response.send_message("Votre role a bien été ajoutez !", ephemeral=True)
            await interaction.user.add_roles(role)
        else:
            await interaction.response.send_message("Votre role a bien été supprimé", ephemeral=True)
            await interaction.user.remove_roles(role)

class notifcommand(commands.Cog):
    def __init__(self,bot):
        bot = bot
    
    ##Commande pour forcer le bot a renvoyé le message de rôle(obsolète après mise en place)
    @commands.command()
    async def notif(self, ctx):
        if ctx.message.author.id == moi:
            view = notifview()
            Embednotif = discord.Embed(title="Role", color=0xa678de)
            Embednotif.add_field(name = "", value="Merci pour ceux qui prendront la peine de sélectionner leur rôles, ces derniers ne sont pas dénués d'intérêt puisqu'il serve a définir les notifications que vous souhaitez recevoir sur mes plateformes :")
            await ctx.send(embed=Embednotif,view=view)
            
async def setup(bot):
    await bot.add_cog(notifcommand(bot))