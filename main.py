from config import TOKEN
from discord.ext import commands
from Utils import CogsLoader

client = commands.AutoShardedBot('.')


@client.event
async def on_ready():
    CogsLoader.load_cogs(client)

client.run(TOKEN)
