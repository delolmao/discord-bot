import discord, os, logic as l
from dotenv import load_dotenv
from discord.ext import commands
import commandapi as c
load_dotenv()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name= "psw")
async def contra(ctx,length = 25):
    x = l.password(length)
    await ctx.send(f"su contraseña es:{x}")

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def roll(ctx, dice: str):
    dado = l.roll(dice)
    await ctx.send(f'Resultado--> {dado}')

@bot.command(name='meme')
async def img_meme(ctx):
    x = l.meme()
    await ctx.send(file = x)

@bot.command(name='memes')
async def img_memes(ctx):
    x = l.memes()
    await ctx.send(file = x)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = c.duck_img()
    await ctx.send(image_url)

bot.run(token)

