import discord, os, logic as l
from dotenv import load_dotenv
from discord.ext import commands

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

bot.run(token)

