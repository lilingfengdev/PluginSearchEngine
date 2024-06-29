import typing

from core.engine.base import SearchResult
from core.engine.bing import Bing


class Klpbbs:

    def search(self, keywords, translation=True, engine=Bing()) -> typing.List[SearchResult]:
        return engine.search(keywords, site="klpbbs.com")[:3]  # 一般来将,前五个才有价值 # 更加fw,3个