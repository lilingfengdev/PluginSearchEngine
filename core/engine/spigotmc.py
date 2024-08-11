import typing

from core.engine.base import SearchEngine, SearchResult
from core.utils.translate import translate, EN
import requests
import json


class SpigotResult(SearchResult):
    def __init__(self, url, title, summary, count):
        super().__init__(url, title, summary)
        self.count = count


class Spigot(SearchEngine):
    def search(self, keywords, translation=True) -> typing.List[SearchResult]:
        key = translate(keywords, EN)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/93.0.4577.63 Safari/537.36'}
        data = json.loads(requests.get(
            f"https://fof1092.de/Plugins/SSE/resourceSearchV2.php?SearchText={key}", headers=headers).content)
        result = []
        for plug in data:
            result.append(
                SpigotResult(url=plug["url"], title=plug["name"], summary=plug["tag"], count=plug["download"]["count"]))
        result.sort(key=lambda obj: obj.count, reverse=True)
        result = result[:10]
        if translation:
            for plug in result:
                plug.summary = translate(plug.summary)
                plug.title = translate(plug.title)
        return result
