import discord
from discord import File
from discord.ext import commands
from discord import app_commands
import discord.gateway
from discord.ui import Button, View

class eloview(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Iron", style=discord.ButtonStyle.success, custom_id='iron', emoji=discord.PartialEmoji.from_str("iron:1358739878325784606"))
    async def iron(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352138940131446806)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Bronze", style=discord.ButtonStyle.success, custom_id='bronze', emoji=discord.PartialEmoji.from_str("bronze:1357375139733569556"))
    async def bronze(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352138910393962516)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Silver", style=discord.ButtonStyle.success, custom_id='silver', emoji=discord.PartialEmoji.from_str("silver:1357375177067073596"))
    async def silver(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352138925929660477)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Gold", style=discord.ButtonStyle.success, custom_id='gold', emoji=discord.PartialEmoji.from_str("gold:1357375156556927189"))
    async def gold(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352139004186988584)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Platine", style=discord.ButtonStyle.success, custom_id='platine', emoji=discord.PartialEmoji.from_str("platine:1358748627635408946"))
    async def platine(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352139029419917365)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Émeraude", style=discord.ButtonStyle.success, custom_id='émeraude', emoji=discord.PartialEmoji.from_str("emeraude:1357375111597916332"))
    async def emeraude(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352139059891273788)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Diamant", style=discord.ButtonStyle.success, custom_id='diamant', emoji=discord.PartialEmoji.from_str("diamant:1357375148038295563"))
    async def diamant(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352139114522349588)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Master", style=discord.ButtonStyle.success, custom_id='master', emoji=discord.PartialEmoji.from_str("master:1357375132372308231"))
    async def master(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352139262690070568)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Grandmaster", style=discord.ButtonStyle.success, custom_id='gm', emoji=discord.PartialEmoji.from_str("gm:1357375167906578463"))
    async def gm(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352139274463481878)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

    @discord.ui.button(label="Challenger", style=discord.ButtonStyle.success, custom_id='challenger', emoji=discord.PartialEmoji.from_str("challenger:1357375125342650488"))
    async def challenger(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        roles = [guild.get_role(1352138940131446806),#iron
            guild.get_role(1352138910393962516),#bronze
            guild.get_role(1352138925929660477),#silver
            guild.get_role(1352139004186988584),#gold
            guild.get_role(1352139029419917365),#platine
            guild.get_role(1352139059891273788),#emeraude
            guild.get_role(1352139114522349588),#diamant
            guild.get_role(1352139262690070568),#master
            guild.get_role(1352139274463481878),#grandmaster
            guild.get_role(1352139312690495593)]#Challenger
        
        role = guild.get_role(1352139312690495593)
        userRoles = interaction.user.roles
        Corresponding = list(set(roles).intersection(userRoles))
        if len(Corresponding) >0:
            for roles in Corresponding:
                if role in userRoles:
                    await interaction.response.send_message("il semblerait que vous possediez deja ce role, il vous sera donc retiré", ephemeral=True)
                    await interaction.user.remove_roles(role)
                else:
                    await interaction.response.send_message("Votre role a bien été changez !", ephemeral=True)
                    await interaction.user.add_roles(role)
                    await interaction.user.remove_roles(Corresponding[0])
        else:
            await interaction.response.send_message("Votre role a bien été ajouté !",ephemeral=True)
            await interaction.user.add_roles(role)

class elo(commands.Cog):
    def __init__(self,bot):
        bot = bot
        
    @commands.command()
    async def elo(self, ctx):
        view = eloview()
        EmbedRole = discord.Embed(title="Elo", color=0xa678de)
        EmbedRole.add_field(name = "", value="Met en avant ton Elo en sélectionnant le rôle adapté, tu pourras t'en servir pour trouver un/des duos :")
        await ctx.send(embed=EmbedRole,view=view)
        
async def setup(bot):
    await bot.add_cog(elo(bot))