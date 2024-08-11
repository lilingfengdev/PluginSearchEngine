import typing

from core.engine.base import SearchResult
from core.engine.bing import Bing


class Tinksp:

    def search(self, keywords, translation, engine=Bing()) -> typing.List[SearchResult]:
        return engine.search(keywords, site="tinksp.com")[:5]
