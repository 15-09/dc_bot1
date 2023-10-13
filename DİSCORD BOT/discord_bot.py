import discord

from bot_mantik import createpassword
from bot_datatime import ts

intents = discord.Intents.default()

intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Basari ile {client.user} baglanildi!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('sa'):
        await message.channel.send("Aleykümeselam Hoşgeldin")
    elif message.content.startswith('baybay'):
        await message.channel.send("görüşürüz baybay")
    elif message.content.startswith('.pwd'):
        await message.channel.send(createpassword(8))
    elif message.content.startswith(".ts"):
        tarih_saat = ts()
        await message.channel.send(tarih_saat)


client.run("MTE1OTkyMjQxNzM5NzkyNzk2Ng.GIy_Aq.9BiRiVuKHeEb1Fjf0YVvIwiKuA9Apc3qlPMR_M")