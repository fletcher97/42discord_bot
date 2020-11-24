# What this modules does:
# - Add a command to clear messages

import discord
from discord.ext import commands

class Commands(commands.Cog):
	def __init__(self, client):
		self.client = client

	# Clears a given number of lines. 1 being the default if no number is given as parameter
	@commands.command()
	async def clear(self, ctx, amount=1):
		if('staff' in [x.name for x in ctx.author.roles]):
			await ctx.channel.purge(limit=amount + 1)

	# TODO: WIP
	@commands.command()
	async def stop(self, ctx):
		if('staff' in [x.name for x in ctx.author.roles]):
			await ctx.channel.send("Logging out!")
			await self.client.close()

def setup(client):
	client.add_cog(Commands(client))
