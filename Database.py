import peewee
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
    mute_role = peewee.BigIntegerField()
    log_channel = peewee.BigIntegerField()


class Member(BaseModel):
    guild_id = peewee.BigIntegerField()
    prefix = peewee.CharField(max_length=5, default='.')
    bonus = peewee.CharField(default="0")


class Bot(BaseModel):
    testers = peewee.TextField()
    staff = peewee.TextField()
    owners = peewee.TextField()
