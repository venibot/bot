import peewee
import discord
from config import DB


database = peewee.MySQLDatabase(host=DB['host'], port=DB['port'], user=DB['user'], password=DB['password'], database=DB['database'])


def create_tables():
    with database:
        database.create_tables([Guild, Member, Bot])


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Guild(BaseModel):
    guild_id = peewee.BigIntegerField(unique=True)
    prefix = peewee.CharField(max_length=5, default='.')
    bonus = peewee.CharField(default="0")
    mute_role = peewee.BigIntegerField(default=0)
    log_channel = peewee.BigIntegerField(default=0)

    class Meta:
        db_table = "guilds"


class Member(BaseModel):
    guild_id = peewee.BigIntegerField()
    prefix = peewee.CharField(max_length=5, default='.')
    bonus = peewee.CharField(default="0")

    class Meta:
        db_table = "members"


class Bot(BaseModel):
    testers = peewee.TextField()
    staff = peewee.TextField()
    owners = peewee.TextField()

    class Meta:
        db_table = "bot"


def add_guild(guild: discord.Guild):
    try:
        Guild.select().where(Guild.guild_id == guild.id).get()
        to_add_guild = False
    except peewee.DoesNotExist:
        to_add_guild = True

    if to_add_guild:
        inserted = Guild(guild_id=guild.id)
        inserted.save()
        return True
    else:
        return False
