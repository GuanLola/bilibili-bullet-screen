
# coding=utf-8
from builtins import str
from bs4 import BeautifulSoup
import requests
from lxml import etree
import re
class BiliSpider:
    def __init__(self):
        # 构造要爬取的视频url地址
        self.BVurl = "https://api.bilibili.com/x/v1/dm/list.so?oid=263537370"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Mobile Safari/537.36"}
    # 弹幕都是在一个url请求中，该url请求在视频url的js脚本中构造
    def getXml_url(self):
        # 获取该视频网页的内容
        response = requests.get(self.BVurl, headers = self.headers)
        html_str = response.content.decode()
        print(html_str)
        # 使用正则找出该弹幕地址
        # 格式为：https://comment.bilibili.com/168087953.xml
        # 我们分隔出的是地址中的弹幕文件名，即 168087953
        getWord_url = re.findall(" '//comment.bilibili.com/'+ (.*) +'.xml',", html_str)
        getWord_url = getWord_url[0].replace("+","").replace(" ","")
        print(getWord_url);
        # 组装成要请求的xml地址
        xml_url = "https://comment.bilibili.com/{}.xml".format(getWord_url)
        return xml_url

    # Xpath不能解析指明编码格式的字符串，所以此处我们不解码，还是二进制文本
    def parse_url(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content

    # 弹幕包含在xml中的<d></d>中，取出即可
    def get_word_list(self,str):
        html = etree.HTML(str)
        d_list = html.xpath("//d")
        return d_list

    def run(self):
        # 1.根据BV号获取弹幕的地址
        # start_url = self.getXml_url()
        start_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=264223404'
        # 2.请求并解析数据
        xml_str = self.parse_url(start_url)
        list = self.get_word_list(xml_str)
        # 3.打印
        for inx, val in enumerate(list):
            # print(etree.tostring(val))
            soup = BeautifulSoup(etree.tostring(val), 'lxml')
            tag = soup.d
            p_progress = tag['p']
            # print(tag.string, p_progress.split(',')[0])
            # stringnum = str(inx) + '=' + val
            stringnum = str(inx) + '=' + "'" + tag.string + "'" + '&' + p_progress.split(',')[0]
            print(stringnum)

if __name__ == '__main__':
    spider = BiliSpider()
    spider.run()
