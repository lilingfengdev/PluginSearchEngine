from plugin.engine.bing import Bing
from plugin.utils.translate import translate, EN


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

    engine = Bing()

    for result in engine.search(keyword):
        print_result(result)
