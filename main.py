from plugin.engine.minebbs import Minebbs
from plugin.engine.klpbbs import Klpbbs
from plugin.engine.spigotmc import Spigot
from plugin.engine.tinksp import Tinksp
from concurrent.futures import ThreadPoolExecutor, wait


def print_result(result):
    print(f"\033[1;32m标题: \033[0m{result.title}")
    print(f"\033[1;34m简介: \033[0m{result.summary}")
    print(f"\033[1;36mURL: \033[0m{result.url}")
    print("\033[1;33m====================\033[0m")
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
