from cn_bing_translator import Translator
from functools import lru_cache

EN = "en"
ZH_CN = "zh-Hans"


@lru_cache(maxsize=None)
def translate(text, to_lang=ZH_CN) -> str:
    translator = Translator()
    return translator.process(text, toLang=to_lang)


