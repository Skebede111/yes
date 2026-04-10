import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'started session {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send('yes working !')

bot.run('')