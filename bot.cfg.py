1:  import discord
2:  import asyncio

3:  c = discord.Client()

4:  @c.event
5:  async def on_ready():
6:       print("Eingelogt als")
7:       print(c.user.name)
8:       print(c.user.id)
9:  @c.event
10: async def on_message(message):
11:     if message.content.startswith("?test"):
12:         await c.send_message(message.channel, "Test bestanden")

13: c.run("Hier Token einfügen.")