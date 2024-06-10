import typing

from plugin.engine.base import SearchResult
from plugin.engine.bing import Bing


class Minebbs(Bing):

    def search(self, keywords) -> typing.List[SearchResult]:
        return super()._search(keywords, site="minebbs.com")[:4]  # 一般来将,前五个才有价值 # 四个吧
