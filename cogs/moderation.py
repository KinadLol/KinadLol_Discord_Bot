import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from discord.ui import Button, View
import json

with open('cogs/banword.json', 'r') as file:
    banword = json.load(file)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
moi = 687334620974284904

class TicketsButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Nouveau Ticket", style=discord.ButtonStyle.success, custom_id='Tickettes')
    async def Button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Votre Ticket a été ouvert", ephemeral=True)
        guild = interaction.guild
        cat =   discord.utils.get(guild.categories, name='Ticket')
        admin_role = guild.get_role(1106723214450770092)
        modo_role = guild.get_role(1106723883731648614)
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True),
            admin_role: discord.PermissionOverwrite(view_channel=True),
            modo_role: discord.PermissionOverwrite(view_channel=True),
        }
        if len(cat.channels) <= 10:
            await guild.create_text_channel(category=cat, name=f"Ticket #{(len(cat.channels)+1)}", overwrites=overwrites)
        else:
            await interaction.followup.send("Désolé il y a déja trop de requète en cours veuillez patientez", ephemeral=True)

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.guild:
            channel = message.channel
            User = message.author
            for Banned in banword:
                if Banned in message.content.lower():
                    await channel.purge(limit = 1)
                    await User.send(f"Sache que ton message a été supprimés car il contient un ou des mots ({Banned}) sur le serveur.")
                    
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
        
    @commands.command()
    async def clear(self, ctx, quantités: int ):
        #if interaction.user.id == moi: 
        await ctx.channel.purge(limit = quantités)
        await ctx.send(f"vous avez purgé {quantités} messages.", ephemeral=True)

#Commande de Ticket
    """commands.command()
    async def ticket(self, ctx):
        view = TicketsButton()
        Icon = discord.File("Images/Tickets.png", filename="tickets.png")
        emb = discord.Embed(title="Tickets", color=0xa678de)
        emb.set_thumbnail(url="attachment://tickets.png")
        emb.add_field(name="", value="Les Tickets sont un outil permettant la création de salons temporaires "
        "permettant de discuter avec les Modérateurs ou Administrateurs du serveur. "
        "ils peuvent servir a réglé des conflits ou proposer des améliorations pour le serveur", inline=True)
        emb.add_field(name="Cloture", value="Une fois votre Ticket ouvert vous aurez 48 heures pour décrire votre problème, passez ce délai le ticket se fermera", inline=False)
        await ctx.send(file=Icon, embed=emb,view=view)"""

async def setup(bot):
    await bot.add_cog(moderation(bot))