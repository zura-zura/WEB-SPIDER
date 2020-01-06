import selenium
from selenium import webdriver
import time
import json




class DouyuSpider:
    def __init__(self):
        pass
        self.start_url="https://www.douyu.com/directory/all"
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\xmp\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\chrome" \
              r"\chromedriver.exe ")

    def get_content_list(self):
        li_list=self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        print(li_list)
        print("+++++++++++++++++++")
        content_list=[]
        for li in li_list:
            item={}
            item["room_img"]=li.find_element_by_xpath(".//img").get_attribute("src") #获取图片
            item["room_title"]=li.find_element_by_xpath(".//div//h3").get_attribute("title") #获取标题
            print(item)
            content_list.append(item)
            #time.sleep(3)
            #获取下一页元素
        next_url=self.driver.find_elements_by_xpath("//span[@class='dy-Pagination-item-custom']")
        next_url=next_url[0] if len(next_url)>0 else None
        print(next_url)
        return content_list,next_url

    def save_content_list(self,content_list):
        pass
        with open("douyu.txt","a",encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")



    def run(self): #实现主要逻辑
        #1. start-url

        #2.发送请求，获取相应
        self.driver.get(self.start_url)
        time.sleep(20) #发送请求后一定要让程序等一下，等页面加载完成，不然找不到要素提取，会出错，也有可能图片没加载完，提取处理啊的图片都是一样的
        #3.提取数据，提取下一页按钮
        content_list,next_url=self.get_content_list()
        #4.保存数据
        self.save_content_list(content_list)
        #5.请求下一页，循环2-5步骤
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list,next_url=self.get_content_list()
            self.save_content_list(content_list)



if __name__=='__main__':
    Spider=DouyuSpider()
    Spider.run()
