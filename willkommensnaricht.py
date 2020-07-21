import discord
from discord.ext import commands
import asyncio

TOKEN = '' # Hier Token einfügen

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('welcome is ready')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="channel-name") # Hier Channel Name einfügen (Achrung - Channelname nicht ändern, sonst funktioniert der Bot nicht mehr!)
    await channel.send(f"**{member.mention}** Begrüßungstext\n User: {len(list(member.guild.members))}") # Hier fügst du deinen Text ein ( \n = Leerzeile )

bot.run(TOKEN) # Oben einfügen oder Klammer mit "Token" ersetzen

#                               Treffzentrum Discord: https://discord.gg/Na9fEdr
#
#
# To-Do
# Zeile 5 Token einfügen
# Zeile 15 Channel-Namen einfügen
# Zeile 16 Text ersetzen
# Treffzentrum Server lieben und Boosten! ❤️
#
#
#