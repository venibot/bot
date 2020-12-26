import requests
from config import API
from Utils import Logger


def send_stat(servers: int, shards: int, users: int):
    sended = requests.get(
        url=f"https://boticord.top/api/stats?servers={servers}&shards={shards}&users={users}",
        headers={"Authorization": API['BotiCord']}
    )

    try:
        if sended.json()['ok']:
            Logger.Console.APIs.boticord_stat_sended(servers, shards, users)
        else:
            Logger.Console.APIs.boticord_stat_errored("Произошла непредвиденная ошибка", "500")
    except KeyError:
        error = sended.json()['error']
        Logger.Console.APIs.boticord_stat_errored(error['message'], error['code'])
