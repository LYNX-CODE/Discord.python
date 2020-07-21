import discord
from discord.ext    import commands
from discord.ext.commands   import Bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Autoreact ready...')

@bot.event
async def on_message(message):
    if message.channel.id == 123456789: # Hier Channel ID einfügen
        await message.add_reaction("") # Hier Emoji einsetzen

bot.run("") # Hier Token einfügen

#                               Treffzentrum Discord: https://discord.gg/Na9fEdr
#
#
# To-Do
# 1. Channel ID einfügen (Zeile 13)
# 2. Emoji einfügen (zeile 14)
# 3. Bot Token einfügen (Zeile 16)
# 4. Bot starten und Spaß haben
# 5. Treffzentrum Server lieben und boosten! xD
#
#