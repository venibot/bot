import discord
from discord.ext import commands
import Database


class Administration(commands.Cog):
    def __init__(self, client: commands.AutoShardedBot):
        self.client = client

    @commands.group(
        name="тестеры",
        description="Управление тестерами бота",
        aliases=['testers'],
        usage="тестеры <тип действия> <пользователь> [причина]"
    )
    async def _testers(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.send(embed=discord.Embed(
                title="Укажите правильное действие",
                description="Доступные действия:\nДобавить\nУдалить",
                colour=self.client.colors['error']
            ))

    @_testers.command(
        name="добавить",
        description="Добавление тестера бота",
        aliases=['add'],
        usage="тестеры добавить <пользователь> [причина]"
    )
    async def _add_tester(self, ctx: commands.Context, user: discord.User, *, reason="не указана"):
        has_role = False
        user_in_support = self.client.support_server.get_member(user.id)
        if (user_in_support is not None) and (self.client.tester_role not in user_in_support.roles):
            await user_in_support.add_roles(self.client.tester_role)
            has_role = True
        if Database.add_tester(user.id, reason, has_role):
            await ctx.send(embed=discord.Embed(
                title="Успешное добавление тестера",
                description=f"Пользователь {user} теперь является тестером бота. Роль на сервере поддержки " + (
                    "не выдана" if not has_role else "выдана"),
                colour=self.client.colors['success']
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="Ошибка при добавлении тестера",
                description=f"Пользователь {user} уже является тестером бота",
                colour=self.client.colors['error']
            ))

    @_testers.command(
        name="удалить",
        description="Удаление тестера бота",
        aliases=['remove'],
        usage="тестеры удалить <пользователь>"
    )
    async def _remove_tester(self, ctx: commands.Context, user: discord.User):
        had_role = False
        user_in_support = self.client.support_server.get_member(user.id)
        if (user_in_support is not None) and (self.client.tester_role in user_in_support.roles):
            await user_in_support.remove_roles(self.client.tester_role)
            had_role = True
        if Database.remove_tester(user.id):
            await ctx.send(embed=discord.Embed(
                title="Успешное удаление тестера",
                description=f"Пользователь {user} теперь не является тестером бота. Роль на сервере поддержки " + (
                    "не была снята по причине её отсутствия" if not had_role else "была снята"),
                colour=self.client.colors['success']
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="Ошибка при удалении тестера",
                description=f"Пользователь {user} не является тестером бота",
                colour=self.client.colors['error']
            ))

    @_testers.command(
        name="список",
        description="Вывод всех тестеров бота",
        aliases=['лист', 'list'],
        usage="тестеры список"
    )
    async def _testers_list(self, ctx: commands.Context):
        testers = Database.get_testers()
        embed = discord.Embed(
            title="Все тестеры бота",
            colour=self.client.colors['base']
        )
        if testers is None:
            embed.description = "Тестеры отсутствуют"
        else:
            embed.description = f"Всего тестеров {len(testers)}"
            for tester in testers:
                embed.add_field(
                    name=f"{self.client.get_user(tester.member_id)}({tester.member_id})",
                    value=f"Причина добавления {tester.reason}. Роль на сервере поддержки " + (
                        "не выдана" if not tester.has_role else "выдана"),
                )
        await ctx.send(embed=embed)

    @commands.group(
        name="стафф",
        description="Управление стаффом бота",
        aliases=['staff'],
        usage="стафф <тип действия> <пользователь> [причина]"
    )
    async def _staff(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.send(embed=discord.Embed(
                title="Укажите правильное действие",
                description="Доступные действия:\nДобавить\nУдалить",
                colour=self.client.colors['error']
            ))

    @_staff.command(
        name="добавить",
        description="Добавление стаффа бота",
        aliases=['add'],
        usage="стафф добавить <пользователь> [причина]"
    )
    async def _add_staff(self, ctx: commands.Context, user: discord.User, *, reason="не указана"):
        has_role = False
        user_in_support = self.client.support_server.get_member(user.id)
        if (user_in_support is not None) and (self.client.staff_role not in user_in_support.roles):
            await user_in_support.add_roles(self.client.staff_role)
            has_role = True
        if Database.add_staff(user.id, reason, has_role):
            await ctx.send(embed=discord.Embed(
                title="Успешное добавление стаффа",
                description=f"Пользователь {user} теперь является стаффом бота. Роль на сервере поддержки " + (
                    "не выдана" if not has_role else "выдана"),
                colour=self.client.colors['success']
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="Ошибка при добавлении стаффа",
                description=f"Пользователь {user} уже является стаффом бота",
                colour=self.client.colors['error']
            ))

    @_staff.command(
        name="удалить",
        description="Удаление стаффа бота",
        aliases=['remove'],
        usage="стафф удалить <пользователь>"
    )
    async def _remove_staff(self, ctx: commands.Context, user: discord.User):
        had_role = False
        user_in_support = self.client.support_server.get_member(user.id)
        if (user_in_support is not None) and (self.client.staff_role in user_in_support.roles):
            await user_in_support.remove_roles(self.client.staff_role)
            had_role = True
        if Database.remove_staff(user.id):
            await ctx.send(embed=discord.Embed(
                title="Успешное удаление стаффа",
                description=f"Пользователь {user} теперь не является стаффом бота. Роль на сервере поддержки " + (
                    "не была снята по причине её отсутствия" if not had_role else "была снята"),
                colour=self.client.colors['success']
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="Ошибка при удалении стаффа",
                description=f"Пользователь {user} не является стаффом бота",
                colour=self.client.colors['error']
            ))

    @_staff.command(
        name="список",
        description="Вывод всех стаффов бота",
        aliases=['лист', 'list'],
        usage="стафф список"
    )
    async def _staff_list(self, ctx: commands.Context):
        staff = Database.get_staff()
        embed = discord.Embed(
            title="Все стаффы бота",
            colour=self.client.colors['base']
        )
        if staff is None:
            embed.description = "Стаффы отсутствуют"
        else:
            embed.description = f"Всего стаффов {len(staff)}"
            for staff_member in staff:
                embed.add_field(
                    name=f"{self.client.get_user(staff_member.member_id)}({staff_member.member_id})",
                    value=f"Причина добавления {staff_member.reason}. Роль на сервере поддержки " + (
                        "не выдана" if not staff_member.has_role else "выдана"),
                )
        await ctx.send(embed=embed)


def setup(client: commands.AutoShardedBot):
    client.add_cog(Administration(client))
