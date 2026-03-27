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

    @commands.command()
    async def deco(self,ctx, id):
        member = await self.bot.fetch_user(id)
        channel = self.bot.get_channel(1107721632295956570)
        rules = self.bot.get_channel(1107995328285790258)
        avatar = member.avatar
        decoration = member.avatar_decoration
        background = Image.open("Images/bienvenue.png")
        pfp = Image.open(requests.get(str(avatar), stream=True).raw)

        w, h = pfp.size

        mask = Image.new('L', (w, h), 0)

        draw = ImageDraw.Draw(mask)

        draw.ellipse((0, 0, w, h), fill = 255)

        result = Image.new("RGBA",(w, h))

        result.paste(pfp, (0,0), mask = mask)

        profile = result.resize((197, 197))
        bannière = background.paste(profile, (792, 142), mask= profile)
        if decoration != None:
            deco = Image.open(requests.get(str(decoration), stream=True).raw).convert("RGBA")
            final = deco.resize((236, 236))
            background.paste(final, (772, 122), mask = final)
            background.save(fp = "images/BackgroundRécent.png")
        else:
            background.save(fp = "images/BackgroundRécent.png")
        with open("images/BackgroundRécent.png", 'rb') as image:
            picture = discord.File(image)
            await channel.send(f"Soit le Bienvenue {member.mention} je te prierai d'allez voir les {rules.mention} avant d'accéder pleinement a ce serveur.", file=picture)
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(1106564303630373005)
        roleMembre = guild.get_role(1106723351298310155)
        channel = self.bot.get_channel(1107721632295956570)
        rules = self.bot.get_channel(1107995328285790258)
        await member.add_roles(roleMembre)
        avatar = member.avatar
        decoration = member.avatar_decoration
        background = Image.open("Images/bienvenue.png")
        pfp = Image.open(requests.get(str(avatar), stream=True).raw)

        w, h = pfp.size

        mask = Image.new('L', (w, h), 0)

        draw = ImageDraw.Draw(mask)

        draw.ellipse((0, 0, w, h), fill = 255)

        result = Image.new("RGBA",(w, h))

        result.paste(pfp, (0,0), mask = mask)

        profile = result.resize((197, 197))
        background.paste(profile, (792, 142), mask= profile)
        if decoration != None:
            deco = Image.open(requests.get(str(decoration), stream=True).raw).convert("RGBA")
            final = deco.resize((236, 236))
            background.paste(final, (772, 122), mask = final)
            background.save(fp = "images/BackgroundRécent.png")
        else:
            background.save(fp = "images/BackgroundRécent.png")
        with open("images/BackgroundRécent.png", 'rb') as image:
            picture = discord.File(image)
            await channel.send(f"Soit le Bienvenu(e) {member.mention} je te prierai d'allez voir les {rules.mention} avant d'accéder pleinement au serveur.", file=picture)

async def setup(bot):
    await bot.add_cog(bienvenue(bot))