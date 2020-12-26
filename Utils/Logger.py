import colorama
from colorama import Fore, Style
import datetime

colorama.init()


class Console:
    class Cogs:
        @staticmethod
        def cog_loaded(cog_name: str):
            now = datetime.datetime.now()
            print(
                f"{Fore.GREEN}[Success]{Style.RESET_ALL}{Fore.CYAN}[{now.hour}:{now.minute}:{now.second} {now.day}.{now.month}.{now.year}][CogsLoader]{Style.RESET_ALL} Успешно загружен ког {cog_name.replace('.py', '').capitalize()}")

        @staticmethod
        def cog_errored(cog_name: str, error: Exception):
            now = datetime.datetime.now()
            print(
                f"{Fore.RED}[Error]{Style.RESET_ALL}{Fore.CYAN}[{now.hour}:{now.minute}:{now.second} {now.day}.{now.month}.{now.year}][CogsLoader]{Style.RESET_ALL} Ошибка при загрузке кога {cog_name.replace('.py', '').capitalize()} - {error}")


    class APIs:
        @staticmethod
        def sdc_stat_sended(servers: int, shards: int):
            now = datetime.datetime.now()
            print(
                f"{Fore.GREEN}[Success]{Style.RESET_ALL}{Fore.CYAN}[{now.hour}:{now.minute}:{now.second} {now.day}.{now.month}.{now.year}][SDC]{Style.RESET_ALL} Информация о боте успешно отправлена на SD.C. Отправленная информация - {servers} серверов и {shards} шардов")

        @staticmethod
        def sdc_stat_errored(error: str, code: int):
            now = datetime.datetime.now()
            print(
                f"{Fore.RED}[Error]{Style.RESET_ALL}{Fore.CYAN}[{now.hour}:{now.minute}:{now.second} {now.day}.{now.month}.{now.year}][SDC]{Style.RESET_ALL} Ошибка при отправке информации о боте на SD.C. {error}. Код ошибки - {code}")

        @staticmethod
        def boticord_stat_sended(servers: int, shards: int, users: int):
            now = datetime.datetime.now()
            print(
                f"{Fore.GREEN}[Success]{Style.RESET_ALL}{Fore.CYAN}[{now.hour}:{now.minute}:{now.second} {now.day}.{now.month}.{now.year}][BotiCord]{Style.RESET_ALL} Информация о боте успешно отправлена на BotiCord. Отправленная информация - {servers} серверов, {shards} шардов и {users} пользователей")

        @staticmethod
        def boticord_stat_errored(error: str, code: str):
            now = datetime.datetime.now()
            print(
                f"{Fore.RED}[Error]{Style.RESET_ALL}{Fore.CYAN}[{now.hour}:{now.minute}:{now.second} {now.day}.{now.month}.{now.year}][BotiCord]{Style.RESET_ALL} Ошибка при отправке информации о боте на BotiCord. {error} Код ошибки - {code}")
