from typing import List

from core.engine.minebbs import Minebbs
from core.engine.klpbbs import Klpbbs
from core.engine.spigotmc import Spigot
from core.engine.tinksp import Tinksp
from core.engine.base import SearchResult
from concurrent.futures import ThreadPoolExecutor, wait


def search(keyword: str, translation=True) -> List[SearchResult]:
    engine = [Spigot, Tinksp, Minebbs, Klpbbs]
    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_list = []
        for e in engine:
            future = executor.submit(e().search, keyword, translation)
            future_list.append(future)
        wait(future_list)
        for future in future_list:
            for result in future.result():
                results.append(result)
    return results
