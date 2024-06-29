import typing

from core.engine.base import SearchResult
import re
import requests
from lxml.html import etree

class Bing:

    def get_bing_url(self, keywords):
        keywords = keywords.strip('\n')
        bing_url = re.sub(r'^', 'https://www.bing.com/search?q=', keywords)
        bing_url = re.sub(r'\s', '+', bing_url)
        return bing_url

    def search(self, keywords, site) -> typing.List[SearchResult]:
        keywords = f'"{keywords}" 插件 site:{site}'
        url = self.get_bing_url(keywords)
        result: typing.List[SearchResult] = []
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                   'Accept-Encoding': 'gzip, deflate',
                   'cookie': 'DUP=Q=sBQdXP4Rfrv4P4CTmxe4lQ2&T=415111783&A=2&IG=31B594EB8C9D4B1DB9BDA58C6CFD6F39; '
                             'MUID=196418ED32D66077102115A736D66479; SRCHD=AF=NOFORM; '
                             'SRCHUID=V=2&GUID=DDFFA87D3A894019942913899F5EC316&dmnchg=1; ENSEARCH=BENVER=1; '
                             '_HPVN=CS'
                             '=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMC0wMy0xNlQwMDowMDowMFoiLCJJb3RkIjowLCJEZnQiOm51bGwsIk12cyI6MCwiRmx0IjowLCJJbXAiOjd9; ABDEF=V=13&ABDV=11&MRNB=1614238717214&MRB=0; _RwBf=mtu=0&g=0&cid=&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2021-02-25T07:47:40.5285039+00:00&e=; MUIDB=196418ED32D66077102115A736D66479; SerpPWA=reg=1; SRCHUSR=DOB=20190509&T=1614253842000&TPC=1614238646000; _SS=SID=375CD2D8DA85697D0DA0DD31DBAB689D; _EDGE_S=SID=375CD2D8DA85697D0DA0DD31DBAB689D&mkt=zh-cn; _FP=hta=on; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; dsc=order=ShopOrderDefault; ipv6=hit=1614260171835&t=4; SRCHHPGUSR=CW=993&CH=919&DPR=1&UTC=480&WTS=63749850642&HV=1614256571&BRW=HTP&BRH=M&DM=0'
                   }
        content = requests.get(url=url, timeout=5, headers=headers)
        tree = etree.HTML(content.text)
        li_list = tree.xpath('//ol[@id="b_results"]//li[@class="b_algo"]')
        for li in li_list:
            try:
                h3 = li.xpath('./h2/a')[0]
                p = li.xpath('.//p')[0].xpath('string(.)')
                try:
                    url = li.xpath('./div[1]/a/div[2]/div[2]/div/cite')[0].xpath('string(.)')
                except IndexError:
                    url = h3.get('href')
                h3 = h3.xpath('string(.)')
                result.append(SearchResult(url=url, title=h3, summary=p))
            except IndexError:
                pass

        return result
