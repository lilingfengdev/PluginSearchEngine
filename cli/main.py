from core.search import search
import random
import colorama

colorama.init(autoreset=True)


def print_result(result):
    print("\033[1;33m====================\033[0m")
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

    results = search(keyword)
    random.shuffle(results)
    for result in results:
        print_result(result)
