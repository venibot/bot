import requests
from config import API
from Utils import Logger


def send_stat(servers: int, shards: int):
    sended = requests.post(
        url="https://api.server-discord.com/v2/bots/728030884179083354/stats",
        headers={"Authorization": API['SDC']},
        data={"servers": servers, "shards": shards}
    )

    try:
        if sended.json()['status']:
            Logger.Console.APIs.sdc_stat_sended(servers, shards)
        else:
            Logger.Console.APIs.sdc_stat_errored("Произошла непредвиденная ошибка", 500)
    except KeyError:
        error = sended.json()['error']
        Logger.Console.APIs.sdc_stat_errored(error['message'], error['code'])
