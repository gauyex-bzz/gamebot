import discord
from discord.ext import commands
from pets import *

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

token = 'TOKEN'
