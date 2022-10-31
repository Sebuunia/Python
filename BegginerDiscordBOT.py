import discord
from discord.ext import commands

TOKEN = ''
CHANNEL_ID = 

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Study bot is ready')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello!')

@bot.command()
async def ping(resp):
    await resp.send('pong')

@bot.command()
async def add(resp, x, y):
    wynik = float(x) + float(y)
    await resp.send(f'{x} + {y} = {wynik}')

@bot.command()
async def subt(resp, x, y):
    wynik = float(x) - float(y)
    await resp.send(f'{x} - {y} = {wynik}')

@bot.command()
async def mult(resp, x, y):
    wynik = float(x) * float(y)
    await resp.send(f'{x} * {y} = {wynik}')

@bot.command()
async def exch(resp, x, y):
    wynik = float(x) / float(y)
    await resp.send(f'{x} / {y} = {wynik}')

bot.run(TOKEN)
