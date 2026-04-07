import discord
import time
import os
from dotenv import load_dotenv
from discord.ext import commands

## Importation de toute les cogs
from cogs.moderation import moderation
from cogs.league import league
from cogs.bienvenue import bienvenue
from cogs.moderation import TicketsButton
from cogs.reactions.jeux import jeuxview
from cogs.reactions.notif import notifview
from cogs.reactions.verif import verif

#Id des messages intéractif a conserver en mémoire
TicketID = 1376778910259351634
notifID = 1376776665559994468
JeuxID = 1376777173079166996
VerifID = 1376960271729295452

##Chargement/recherche du Token de connections
load_dotenv("/home/container/Token.env")
Token = os.getenv('DISCORD_TOKEN')

##paramètres du bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)

bot.remove_command("help")
cogs = ["league", "moderation", "bienvenue", "reactions.jeux", "reactions.notif", "reactions.verif"]

##Commande de chargement des command slash
@bot.command(name="sync") 
async def sync(ctx):
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")

##chargements des cogs du bot
@bot.event
async def on_ready():
    for cog in cogs:
        await bot.load_extension("cogs."+cog)

    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")

async def setup_hook():
    ##Chargement des View(Boutons sans limites de temps)
    bot.add_view(TicketsButton(), message_id=TicketID)
    bot.add_view(jeuxview(), message_id=JeuxID)
    bot.add_view(notifview(), message_id=notifID)
    bot.add_view(verif(), message_id=VerifID)

bot.setup_hook = setup_hook
time.sleep(10)
bot.run(Token)