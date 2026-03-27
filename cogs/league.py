import discord
from discord import File
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

class league(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    ##Commande pour obtenir les stats lolalytics d'un champion
    @app_commands.command(name="build", description="Trouve le build populaire du moment sur ton champion préferé !")
    async def build(self, interaction:discord.Interaction, champion:str):
        CommandChannel = self.bot.get_channel(1106664079503937566)
        champ = champion.replace("'", "").lower()
        if interaction.channel == CommandChannel:
            if champ == "mundo" or champ == "dr mundo":
                champ ="drmundo"
            if champ == "lee sin":
                champ = "leesin"
            if champ == "maitre yi" or champ == "maître yi" or champ == "master yi":
                champ = "masteryi"
            if champ == "tf" or champ == "twisted fate":
                champ = "twistedfate"
            await interaction.response.send_message(f"https://lolalytics.com/fr/lol/{champ}/build/", ephemeral=True)
        else:
            await interaction.response.send_message(f"Les commandes doivent être utilisées dans le salon {CommandChannel.mention}", ephemeral=True)
    
    ##Commande pour obtenir le build onetrickgg d'un champion
    @app_commands.command(name="otp", description="Trouve le build populaire des OTP sur ton champion préferé !")
    async def otp(self, interaction:discord.Interaction, champion:str):
        CommandChannel = self.bot.get_channel(1106664079503937566)
        champ = champion.replace("'", "").lower()
        if interaction.channel == CommandChannel:
            if champ == "mundo" or champ == "dr mundo":
                champ ="drmundo"
            if champ == "lee sin":
                champ = "leesin"
            if champ == "maitre yi" or champ == "maître yi" or champ == "master yi":
                champ = "masteryi"
            if champ == "tf" or champ == "twisted fate":
                champ = "twistedfate"
            await interaction.response.send_message(f"https://www.onetricks.gg/fr/champions/builds/{champ}", ephemeral=True)
        else:
            await interaction.response.send_message(f"Les commandes doivent être utilisées dans le salon {CommandChannel.mention}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(league(bot))