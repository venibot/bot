from discord.ext import commands
import Database


def is_tester():
    def predicate(ctx: commands.Context):
        if Database.get_tester(ctx.author.id):
            return True
        else:
            return False
    return commands.check(predicate)


def is_staff():
    def predicate(ctx: commands.Context):
        if Database.get_staff_member(ctx.author.id):
            return True
        else:
            return False
    return commands.check(predicate)

