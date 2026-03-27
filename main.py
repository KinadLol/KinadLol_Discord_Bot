import discord
import time
import os

from dotenv import load_dotenv
from discord.ext import commands
from cogs.moderation import moderation
from cogs.league import league
from cogs.bienvenue import bienvenue
from cogs.moderation import TicketsButton
from cogs.reactions.jeux import jeuxview
from cogs.reactions.notif import notifview
from cogs.reactions.verif import verif


TicketID = 1376778910259351634
notifID = 1376776665559994468
JeuxID = 1376777173079166996
VerifID = 1376960271729295452
load_dotenv("/home/container/Token.env")
Token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)

bot.remove_command("help")

@bot.command(name="sync") 
async def sync(ctx):
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")

@bot.event ## : cogs
async def on_ready():
    await bot.load_extension("cogs.moderation")
    await bot.load_extension("cogs.league")
    await bot.load_extension("cogs.bienvenue")
    await bot.load_extension("cogs.reactions.jeux")
    await bot.load_extension("cogs.reactions.notif")
    await bot.load_extension("cogs.reactions.verif")
    
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")

async def setup_hook():
    bot.add_view(TicketsButton(), message_id=TicketID)
    bot.add_view(jeuxview(), message_id=JeuxID)
    bot.add_view(notifview(), message_id=notifID)
    bot.add_view(verif(), message_id=VerifID)

bot.setup_hook = setup_hook
time.sleep(10)
bot.run(Token)