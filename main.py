from config import TOKEN
import discord
from discord.ext import commands
from Utils import CogsLoader
from Utils.APIs import SDC, BotiCord
import Database

client = commands.AutoShardedBot(Database.get_prefix, intents=discord.Intents.all())


@client.event
async def on_ready():
    client.support_server = client.get_guild(759796323569500160)
    client.tester_role = client.support_server.get_role(759796893621551184)
    client.staff_role = client.support_server.get_role(759797091198435338)
    client.owner_role = client.support_server.get_role(759806670540111893)
    client.colors = {"base": 0x000000, "success": 0x000000, "error": 0x000000}
    CogsLoader.load_cogs(client)
    Database.create_tables()
    for guild in client.guilds:
        Database.add_guild(guild)
    # SDC.send_stat(len(client.guilds), len(client.shards))
    # BotiCord.send_stat(len(client.guilds), len(client.shards), len(client.users))


client.run(TOKEN)
