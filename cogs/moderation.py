import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from discord.ui import Button, View
import json

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

##Id discord Kinad
moi = 687334620974284904

 ##Bouton de création de ticket
class TicketsButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

   
    @discord.ui.button(label="Nouveau Ticket", style=discord.ButtonStyle.success, custom_id='Tickettes')
    async def Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        ##Variable de role/Catégories
        guild = interaction.guild
        cat =   discord.utils.get(guild.categories, name='Ticket')
        admin_role = guild.get_role(1106723214450770092)
        modo_role = guild.get_role(1106723883731648614)
        
        ##changement des perms du salon nouvellement trié
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True),
            admin_role: discord.PermissionOverwrite(view_channel=True),
            modo_role: discord.PermissionOverwrite(view_channel=True),
        }
        ##création du salon privé (vérification de la quantitées de salon crée)
        if len(cat.channels) <= 10:
            await interaction.response.send_message("Votre Ticket a été ouvert", ephemeral=True)
            await guild.create_text_channel(category=cat, name=f"Ticket #{(len(cat.channels)+1)}", overwrites=overwrites)
        else:
            await interaction.followup.send("Désolé il y a déja trop de requète en cours veuillez patientez", ephemeral=True)

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    ##commande pour ajouter une réaction a un message                
    @commands.command()
    async def reaction(self, ctx, msg: discord.Message, emote):
        if ctx.message.author.id == moi:
            await msg.add_reaction(emote)
            await asyncio.sleep(0.3)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
            await asyncio.sleep(1.5)
            await ctx.channel.purge(limit=2)
    
    ##commande pour retirer une reaction a un message (emote = Emoji), (msg = id du message), (id* = identifiant de l'utilisateur)
    @commands.command()
    async def reactionless(self, ctx, msg: discord.Message, emote = None, identifiant: discord.User = None):
        if ctx.message.author.id == moi:
            if identifiant == None:
                if emote == None:
                    await msg.clear_reactions()
                    await asyncio.sleep(0.3)
                    await ctx.channel.purge(limit=1)
                else:
                    await msg.clear_reaction(emote)
                    await asyncio.sleep(0.3)
                    await ctx.channel.purge(limit=1)
            else:
                await msg.remove_reaction(emote, identifiant)
                await asyncio.sleep(0.3)
                await ctx.channel.purge(limit=1)
        else:
            await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
            await asyncio.sleep(1.5)
            await ctx.channel.purge(limit=2)
    
    ##Commande pour retirer X nombre de message dans un channel écrit
    @commands.command()
    async def clear(self, ctx, quantités: int ):
        #if interaction.user.id == moi: 
        await ctx.channel.purge(limit = quantités)
        await ctx.send(f"vous avez purgé {quantités} messages.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(moderation(bot))