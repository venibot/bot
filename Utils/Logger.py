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
