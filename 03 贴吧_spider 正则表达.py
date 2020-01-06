import requests
import json
import re
import lxml
from lxml import etree
import html



class DoubanSpider:
    def __init__(self,tieba_name):
        self.start_url_temp="https://movie.douban.com/subject/{}/?tag=热门8&from=gaia_video"
        self.headers={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self,url): #发送请求获取相应
        response=requests.get(url,headers=self.headers)
        return response.content.decode(encoding='utf-8')

    def get_content_list(self,html_str): #提取数据
        html=etree.HTML(html_str)
        print(html)
        s1=etree.tostring(html).decode(encoding='utf-8')
        print(s1)
        #获取电视剧名称
        print("++++++++++++++++++++++++++++")
        ret1=html.xpath("//link/@href")
        print(ret1)


        # content_list=re.findall(r"",html_str)
        # print(content_list)
        # return content_list

    def save_content_list(self,content_list): # 保存数据
        with open("douban1.txt","a") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n") # 写入换行符进行换行
        print("保存成功")


    def run(self): #实现主要逻辑

        ID=25853071
        #hile ID==30327842:
        #1.获取starturl
        url=self.start_url_temp.format(ID)
        print(url)
        #2.发送请求获取相应
        html_str=self.parse_url(url)
        #3.提取数据，提取下一页URL地址
        content_list=self.get_content_list(html_str)
        #4.保存数据
        # self.save_content_list(content_list)
        #5.请求下一页url地址，循环2-5


if __name__=='__main__':
    douban_spider=DoubanSpider()
    douban_spider.run()








