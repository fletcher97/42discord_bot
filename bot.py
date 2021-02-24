# What this modules does:
# - Cycles through all the cogs and runs them
# - Gives the users 3 commands (load, unload, reload) to work with the cogs

# Each cog has the same structure:
# class cog_name(commands.Cog):
# 	def __init__(self, client):
# 		self.client = client

# Whatever you want him to do

# def setup(client):
# 	client.add_cog(cog_name(client))

# There are two main types of events:
# - @commands.command(): response to a command following the pattern defined in bot.py (i.e. .<command name>)
# - @commands.Cog.listener(): basically every other event like a message is sent or the bot starts

from dotenv import load_dotenv
import discord
import os
from discord.ext import commands

# Switch between prod and dev branches
branches = ["prod", "dev"]
switch = branches[1]

# Gives the bots additionnal permissions
# Defines the prefix for commands
intents = discord.Intents().all()
client = commands.Bot(command_prefix = '.', intents=intents)

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	if('staff' in [x.name for x in ctx.author.roles]):
		client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

load_dotenv()
if switch == branches[0]:
	token = os.environ.get("TOKEN_PROD")
else:
	token = os.environ.get("TOKEN_DEV")
client.run(token)
