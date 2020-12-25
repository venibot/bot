from config import TOKEN
from discord.ext import commands
from Utils import CogsLoader
import Database

client = commands.AutoShardedBot('.')


@client.event
async def on_ready():
    CogsLoader.load_cogs(client)
    Database.create_tables()

client.run(TOKEN)
