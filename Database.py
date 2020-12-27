import peewee
import discord
from config import DB


database = peewee.MySQLDatabase(host=DB['host'], port=DB['port'], user=DB['user'], password=DB['password'], database=DB['database'])


def create_tables():
    with database:
        database.create_tables([Guild, Member, Tester, Staff])


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


class Tester(BaseModel):
    member_id = peewee.BigIntegerField(unique=True)
    reason = peewee.TextField()
    has_role = peewee.BooleanField()

    class Meta:
        db_table = "testers"


class Staff(BaseModel):
    member_id = peewee.BigIntegerField(unique=True)
    reason = peewee.TextField()
    has_role = peewee.BooleanField()

    class Meta:
        db_table = "staff"


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


def add_tester(tester_id: int, reason: str, has_role: bool):
    try:
        Tester.select().where(Tester.member_id == tester_id).get()
        to_add_tester = False
    except peewee.DoesNotExist:
        to_add_tester = True

    if to_add_tester:
        inserted = Tester(member_id=tester_id, reason=reason, has_role=has_role)
        inserted.save()
        return True
    else:
        return False


def remove_tester(tester_id: int):
    try:
        Tester.select().where(Tester.member_id == tester_id).get()
        to_remove_tester = True
    except peewee.DoesNotExist:
        to_remove_tester = False

    if to_remove_tester:
        to_delete = Tester.get(member_id=tester_id)
        to_delete.delete_instance()
        return True
    else:
        return False


def get_tester(tester_id):
    try:
        return Tester.select().where(Tester.member_id == tester_id).get()
    except peewee.DoesNotExist:
        return False


def get_testers():
    testers = [tester for tester in Tester.select()]
    return testers


def add_staff(staff_id: int, reason: str, has_role: bool):
    try:
        Staff.select().where(Staff.member_id == staff_id).get()
        to_add_staff = False
    except peewee.DoesNotExist:
        to_add_staff = True

    if to_add_staff:
        inserted = Staff(member_id=staff_id, reason=reason, has_role=has_role)
        inserted.save()
        return True
    else:
        return False


def remove_staff(staff_id: int):
    try:
        Staff.select().where(Staff.member_id == staff_id).get()
        to_remove_staff = True
    except peewee.DoesNotExist:
        to_remove_staff = False

    if to_remove_staff:
        to_delete = Staff.get(member_id=staff_id)
        to_delete.delete_instance()
        return True
    else:
        return False


def get_staff_member(staff_id: int):
    try:
        return Staff.select().where(Staff.member_id == staff_id).get()
    except peewee.DoesNotExist:
        return False


def get_staff():
    staff = [staff_member for staff_member in Staff.select()]
    return staff
