import discord
from discord.ext import commands
import os
from Utils import Logger


def load_cog(client: commands.AutoShardedBot, cog_name: str):
    try:
        client.load_extension(f"Cogs.{cog_name.replace('.py', '')}")
        Logger.Console.Cogs.cog_loaded(cog_name)
    except Exception as error:
        Logger.Console.Cogs.cog_errored(cog_name, error)


def load_cogs(client: commands.AutoShardedBot):
    for cog_name in os.listdir('./Cogs'):
        if cog_name.endswith('.py'):
            try:
                client.load_extension(f"Cogs.{cog_name.replace('.py', '')}")
                Logger.Console.Cogs.cog_loaded(cog_name)
            except Exception as error:
                Logger.Console.Cogs.cog_errored(cog_name, error)