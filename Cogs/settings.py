import discord
from discord.ext import commands
import Database
import typing


class Settings(commands.Cog):
    def __init__(self, client: commands.AutoShardedBot):
        self.client = client


    async def check_prefix(self, ctx: commands.Context, prefix: str):
        if prefix is None:
            return await ctx.send(embed=discord.Embed(
                title="Ошибка при смене префикса",
                description="Укажите новый префикс",
                colour=self.client.colors['error']
            ))
        if ' ' in prefix:
            return await ctx.send(embed=discord.Embed(
                title="Ошибка при смене префикса",
                description="Префикс не должен содержать пробелы",
                colour=self.client.colors['error']
            ))
        elif len(prefix) > 5:
            return await ctx.send(embed=discord.Embed(
                title="Ошибка при смене префикса",
                description="Префикс не должен быть длиннее 5 символов",
                colour=self.client.colors['error']
            ))
        else:
            return True


    @commands.command(
        name="селфпрефикс",
        description="Настройка префикса",
        aliases=['селф_префикс', 'selfprefix', 'self_prefix'],
        usage="префикс <Тип(здесь или везде)> <Новый префикс>"
    )
    async def _self_prefix(self, ctx: commands.Context, prefix_type: str = None, new_prefix: str = None):
        if (prefix_type is None) and (new_prefix is None):
            current_prefix = Database.get_prefix(None, ctx.message)
            await ctx.send(embed=discord.Embed(
                title="Смена префикса",
                description=f"Текущий префикс, который вы можете использовать - `{current_prefix}`. Для установки "
                            f"нового префикса для себя, воспользуйтесь командой `селфпрефикс`, для установки префикса "
                            f"сервера - `префикс`",
                colour=self.client.colors['base']
            ))
        else:
            if prefix_type is not None:
                if prefix_type == "здесь":
                    if ctx.guild is None:
                        return await ctx.send(embed=discord.Embed(
                            title="Ошибка при смене префикса",
                            description="Пока что нельзя сменить префикс только для личных сообщений",
                            colour=self.client.colors['error']
                        ))
                    else:
                        checked = await self.check_prefix(ctx, new_prefix)
                        if checked and Database.set_prefix("member", ctx.author.id, new_prefix, ctx.guild.id):
                            return await ctx.send(embed=discord.Embed(
                                title="Префикс успешно сменён",
                                description=f"Ваш личный префикс для этого сервера успешно сменён на {new_prefix}",
                                colour=self.client.colors['success']
                            ))
                        else:
                            return await ctx.send(embed=discord.Embed(
                                title="Ошибка при смене префикса",
                                description="Произошла непредвиденная ошибка при смене префикса. Повторите попытку "
                                            "позже",
                                colour=self.client.colors['error']
                            ))
                elif prefix_type == "везде":
                    checked = await self.check_prefix(ctx, new_prefix)
                    if checked and Database.set_prefix("user", ctx.author.id, new_prefix):
                        return await ctx.send(embed=discord.Embed(
                            title="Префикс успешно сменён",
                            description=f"Ваш личный префикс успешно сменён на {new_prefix}",
                            colour=self.client.colors['success']
                        ))
                    else:
                        return await ctx.send(embed=discord.Embed(
                            title="Ошибка при смене префикса",
                            description="Произошла непредвиденная ошибка при смене префикса. Повторите попытку "
                                        "позже",
                            colour=self.client.colors['error']
                        ))
                else:
                    return await ctx.send(embed=discord.Embed(
                        title="Ошибка при смене префикса",
                        description="Выберите одну из доступных категорий смены префикса(здесь или везде)",
                        colour=self.client.colors['error']
                    ))


def setup(client: commands.AutoShardedBot):
    client.add_cog(Settings(client))
