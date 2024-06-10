from plugin.engine.bing import Bing
from plugin.utils.translate import translate,EN

print("欢迎使用插件搜索工具")
keyword = input("请输入关键字:")

engine = Bing()

for result in engine.search(f"我的世界 {translate(keyword)} 插件"):
    print(result.title)
    print(result.summary)
    print(result.url)
    print("====================")
    print()

for result in engine.search(f"minecraft {translate(keyword,EN)} plugin"):
    print(translate(result.title))
    print(translate(result.summary))
    print(result.url)
    print("====================")
    print()
