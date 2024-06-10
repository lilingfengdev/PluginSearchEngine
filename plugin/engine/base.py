from abc import ABC, abstractmethod
import typing


class SearchResult:

    def __init__(self, url, title, summary):
        self.url = url
        self.title = title
        self.summary = summary


class SearchEngine(ABC):

    @abstractmethod
    def search(self, keywords) -> typing.List[SearchResult]:
        pass
