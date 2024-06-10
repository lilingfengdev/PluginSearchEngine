import typing

from plugin.engine.base import SearchResult
from plugin.engine.bing import Bing


class Klpbbs(Bing):

    def search(self, keywords) -> typing.List[SearchResult]:
        return super()._search(keywords, site="klpbbs.com")[:3]  # 一般来将,前五个才有价值 # 更加fw,3个