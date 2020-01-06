import requests
import json
import re
import lxml
from lxml import etree
import html
import os

class DoubanSpider:
    def __init__(self):
        self.start_url_temp="https://movie.douban.com/subject/{}/?tag=热门8&from=gaia_video"
        self.headers={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}


    def parse_url(self,url): #发送请求获取相应
        response=requests.get(url,headers=self.headers)
        return response.content.decode(encoding='utf-8')

    def get_content_list(self,html_str): #提取数据
        html_s1=etree.HTML(html_str)  #将字符串转换为html格式，并作为写X-path的基础。
        #print(html_s1)
        s1=etree.tostring(html_s1).decode(encoding='utf-8') #将html-S1可视化，打印出来，用于查看怎么写x-path
        s1 = html.unescape(s1)     # 调用html的unescape方法解决乱码问题
        #print(s1)
        #获取电视剧名称
        #print("++++++++++++++++++++++++++++")
        content_list=[] #定义列表，用于存放字典
        item={} #定义字典，接收信息。
        item["TV_name"]=html_s1.xpath("/html//div/div[@class='sub-title']/text()") #获取电视剧的名称并存到字典的“TV-name”key中。
        item["Introduction"]=html_s1.xpath("/html//div[@class='bd']/p/text()")
        item["Introduction"]=item["Introduction"][0].replace("\n","") # 去除换行符
        item["Introduction"]=item["Introduction"].replace(" ","") #去除空格
        item["Poster"]=html_s1.xpath("/html//div[@id='subject-header-container']/div/a/img/@src") #获取海报图片链接
        item["Poster"]= item["Poster"][0] if len(item["Poster"])>0 else None # 如果没有海报链接则返回None

        print(item)
        content_list.append(item)
        return content_list


    def save_content_list(self,content_list): # 保存数据
        with open("douban2.txt","a") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n") # 写入换行符进行换行
        print("保存成功")



    def run(self): #实现主要逻辑

        with open('doubanid_list.txt', 'r') as f:
            ID_list = f.readlines()  # 从IDtxt文件中获取ID列表。
        for ID in ID_list:
            ID=eval(ID)  # 去掉txt文件中ID两边的双引号
            #hile ID==30327842:
            #1.获取starturl
            url=self.start_url_temp.format(ID)
            print(url)
            #2.发送请求获取相应
            html_str=self.parse_url(url)
            #3.提取数据，提取下一页URL地址
            content_list=self.get_content_list(html_str)
            #4.保存数据
            self.save_content_list(content_list)
            #5.请求下一页url地址，循环2-5

if __name__=='__main__':
    douban_spider=DoubanSpider()
    douban_spider.run()








