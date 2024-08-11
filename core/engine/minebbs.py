import typing

from core.engine.base import SearchResult
from core.engine.bing import Bing


class Minebbs():

    def search(self, keywords, translation=True, engine=Bing()) -> typing.List[SearchResult]:
        return engine.search(keywords, site="minebbs.com")[:4]  # 一般来将,前五个才有价值 # 四个吧
