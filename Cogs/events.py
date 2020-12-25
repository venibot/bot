import discord
from discord.ext import commands
import Database


class Events(commands.Cog):
    def __init__(self, client: commands.AutoShardedBot):
        self.client = client

    @commands.Cog.listener(name="Вход на сервер")
    async def on_guild_join(self, guild: discord.Guild):
        Database.add_guild(guild)


def setup(client: commands.AutoShardedBot):
    client.add_cog(Events(client))
