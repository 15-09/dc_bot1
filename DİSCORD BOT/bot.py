import discord
import time
import random
import os
import requests
from discord.ext import commands
from bot_mantik import createpassword
from bot_datatime import ts

intents = discord.Intents.default()

intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Basari ile {bot.user} baglanildi!')

@bot.command()
async def sa(ctx):
    await ctx.send(f"ve Aleykümeselam Hoşgeldiniz {bot.user}")

@bot.command()
async def heh(ctx,heh=5):
    await ctx.send("he"*heh)

@bot.command()
async def mem(ctx):
    with open('C:/Users/kadir/OneDrive/Masaüstü/DİSCORD BOT/img/1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def rmem(ctx):
    rmemm = random.choice(os.listdir("C:/Users/kadir/OneDrive/Masaüstü/DİSCORD BOT/img"))
    with open(f'C:/Users/kadir/OneDrive/Masaüstü/DİSCORD BOT/img/{rmemm}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def rcmem(ctx):
    olasılıklar = [0.5 , 0.25 , 0.25]
    rmemm = random.choices(os.listdir("C:/Users/kadir/OneDrive/Masaüstü/DİSCORD BOT/img"),weights=olasılıklar)[0]
    with open(f'C:/Users/kadir/OneDrive/Masaüstü/DİSCORD BOT/img/{rmemm}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def pwd(ctx,lengtha=8):
    embed = discord.Embed(title="Your Password" , color=0x0000FF)
    pwdd = createpassword(lengtha)
    embed.add_field(name="Şifreniz", value=pwdd)
    await ctx.send(embed = embed)


bot.run("MTE1OTkyMjQxNzM5NzkyNzk2Ng.GJahkP.9RNjBW7qXze-Z8h-3hFhGrcdHMrOIyU6etLhJ4")