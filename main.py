from config import TOKEN
import discord
from discord.ext import commands
from Utils import CogsLoader
import Database

client = commands.AutoShardedBot('.', intents=discord.Intents.all())


@client.event
async def on_ready():
    CogsLoader.load_cogs(client)
    Database.create_tables()
    for guild in client.guilds:
        Database.add_guild(guild)

client.run(TOKEN)
