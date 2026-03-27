import discord
import requests
from PIL import Image, ImageDraw
from discord import File
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

class bienvenue(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    ##Commande test bannière custom
    @commands.command()
    async def deco(self,ctx, id):
        ##variable : membre, salon(Bienvenue + regles), pp, deco pp
        member = await self.bot.fetch_user(id)
        channel = self.bot.get_channel(1107721632295956570)
        rules = self.bot.get_channel(1107995328285790258)
        avatar = member.avatar
        decoration = member.avatar_decoration
        background = Image.open("/home/container/Images/bienvenue.png")
        pfp = Image.open(requests.get(str(avatar), stream=True).raw)

        ##variable de taille de pp
        w, h = pfp.size

        ##Création bordure pp
        mask = Image.new('L', (w, h), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, w, h), fill = 255)

        ##Création nouvelle image + collé pp modifié + changement taille PP
        result = Image.new("RGBA",(w, h))
        result.paste(pfp, (0,0), mask = mask)
        profile = result.resize((197, 197))

        ##Ajout pp a image de fonds 
        background = background.paste(profile, (792, 142), mask= profile)

        ##Vérification Déco de PP
        if decoration != None:
            ##collé déco pp si existante
            deco = Image.open(requests.get(str(decoration), stream=True).raw).convert("RGBA")
            final = deco.resize((236, 236))
            background.paste(final, (772, 122), mask = final)
            background.save(fp = "/home/container/Images/BackgroundRécent.png")
        else:
            background.save(fp = "/home/container/Images/BackgroundRécent.png")
        ##Sauvegarde de la bannière avant envois
        with open("/home/container/Images/BackgroundRécent.png", 'rb') as image:
            picture = discord.File(image)
            await channel.send(f"Soit le Bienvenue {member.mention} je te prierai d'allez voir les {rules.mention} avant d'accéder pleinement a ce serveur.", file=picture)
        
    ##Bannière custom a l'arrivé d'un nouveau membre
    @commands.Cog.listener()
    async def on_member_join(self, member):
        ##variable : membre, salon(Bienvenue + regles), pp, deco pp
        guild = self.bot.get_guild(1106564303630373005)
        roleMembre = guild.get_role(1106723351298310155)
        channel = self.bot.get_channel(1107721632295956570)
        rules = self.bot.get_channel(1107995328285790258)
        avatar = member.avatar
        decoration = member.avatar_decoration
        background = Image.open("/home/container/Images/bienvenue.png")
        pfp = Image.open(requests.get(str(avatar), stream=True).raw)

        ##variable de taille de pp
        w, h = pfp.size
        ##Ajour role au nouveau membre
        await member.add_roles(roleMembre)

        
        ##Création bordure pp
        mask = Image.new('L', (w, h), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, w, h), fill = 255)

        ##Création nouvelle image + collé pp modifié + changement taille PP
        result = Image.new("RGBA",(w, h))
        result.paste(pfp, (0,0), mask = mask)
        profile = result.resize((197, 197))

        ##Ajout pp a image de fonds 
        background.paste(profile, (792, 142), mask= profile)

        ##Vérification Déco de PP
        if decoration != None:
            ##collé déco pp si existante
            deco = Image.open(requests.get(str(decoration), stream=True).raw).convert("RGBA")
            final = deco.resize((236, 236))
            background.paste(final, (772, 122), mask = final)
            background.save(fp = "/home/container/Images/BackgroundRécent.png")
        else:
            background.save(fp = "/home/container/Images/BackgroundRécent.png")
        ##Sauvegarde de la bannière avant envois
        with open("/home/container/Images/BackgroundRécent.png", 'rb') as image:
            picture = discord.File(image)
            await channel.send(f"Soit le Bienvenu(e) {member.mention} je te prierai d'allez voir les {rules.mention} avant d'accéder pleinement au serveur.", file=picture)

async def setup(bot):
    await bot.add_cog(bienvenue(bot))