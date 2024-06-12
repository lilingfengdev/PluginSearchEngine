from plugin.engine.minebbs import Minebbs
from plugin.engine.klpbbs import Klpbbs
from plugin.engine.spigotmc import Spigot
from plugin.engine.tinksp import Tinksp
from concurrent.futures import ThreadPoolExecutor, wait


def print_result(result):
    print(result.title)
    print(result.summary)
    print(result.url)
    print("====================")
    print()


print("欢迎使用插件搜索工具")
while True:
    keyword = input("请输入关键字(exit退出):")
    if keyword == "exit":
        break

    engine = [Spigot, Tinksp, Minebbs, Klpbbs, ]
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_list = []
        for e in engine:
            future = executor.submit(e().search, keyword)
            future_list.append(future)
        wait(future_list)
        for future in future_list:
            for result in future.result():
                print_result(result)
