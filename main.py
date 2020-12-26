from config import TOKEN
import discord
from discord.ext import commands
from Utils import CogsLoader
from Utils.APIs import SDC, BotiCord
import Database

client = commands.AutoShardedBot('.', intents=discord.Intents.all())


@client.event
async def on_ready():
    CogsLoader.load_cogs(client)
    Database.create_tables()
    for guild in client.guilds:
        Database.add_guild(guild)
    SDC.send_stat(len(client.guilds), len(client.shards))
    BotiCord.send_stat(len(client.guilds), len(client.shards), len(client.users))

client.run(TOKEN)
