import typing

from plugin.engine.base import SearchResult
from plugin.engine.bing import Bing


class Klpbbs:

    def search(self, keywords,engine=Bing()) -> typing.List[SearchResult]:
        return engine.search(keywords, site="klpbbs.com")[:3]  # 一般来将,前五个才有价值 # 更加fw,3个