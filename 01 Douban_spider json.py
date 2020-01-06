import requests
import json
import lxml
# from lxml import etree


class DoubanSpider:
    def __init__(self,type_name,tag_name):
        self.start_url_temp="https://movie.douban.com/j/search_subjects?type="+type_name+"&tag="+tag_name+"&page_limit=20&page_start={}"
        self.headers={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self,url): #发送请求获取相应
        response=requests.get(url,headers=self.headers)
        return response.content.decode(encoding="utf-8")

    def get_content_list(self,json_str): #提取数据
        dict_ret=json.loads(json_str)
        content_list=dict_ret["subjects"] #如果在字典的二级KEY里面格式如下：dict_rect["一级KEY"]["二级KEY"]
        title=[i["title"] for i in content_list] # 提取作品的名称
        id_list=[i["id"] for i in content_list] # 提取作品的ID
        return content_list,title,id_list




    def save_content_list(self,content_list): # 保存数据
        with open("douban1.txt","a") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n") # 写入换行符进行换行
        print("保存成功")

    def save_ID_list(self, ID_list):  # 保存数据
        with open("doubanid_list.txt", "a") as f:
            for ID in ID_list:
                f.write(json.dumps(ID, ensure_ascii=False))
                f.write("\n")  # 写入换行符进行换行
        print("保存成功")


    def run(self): #实现主要逻辑
        num=0
        while num<1000:
            #1.获取starturl
            url=self.start_url_temp.format(num)
            print(url)
            #2.发送请求获取相应
            json_str=self.parse_url(url)
            #3.提取数据，提取下一页URL地址
            content_list,title,id_list=self.get_content_list(json_str)
            print(title)
            print(id_list)

            #4.保存数据
            self.save_content_list(content_list)
            self.save_ID_list(id_list)

            #5.请求下一页url地址，循环2-5
            num+=20


if __name__=='__main__':
    douban_spider=DoubanSpider("tv","热门")
    douban_spider.run()








