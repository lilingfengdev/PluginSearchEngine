from cn_bing_translator import Translator

EN = "en"
ZH_CN = "zh-Hans"


def translate(text, to_lang=ZH_CN) -> str:
    translator = Translator()
    return translator.process(text, toLang=to_lang)


