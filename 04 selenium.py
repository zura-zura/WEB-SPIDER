





from selenium import webdriver
import time


#实例化一个浏览器
chrome_driver=r"C:\Users\xmp\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\chrome" \
              r"\chromedriver.exe " # 制定驱器位置，如果selenium没有驱动器，网络下载对应版本的chromdriver


driver=webdriver.Chrome(executable_path=chrome_driver)

#driver=webdriver.PhantomJS(executable_path=r'C:\Users\xmp\Downloads\phantomjs-2.5.0-beta2-windows\phantomjs-2.5.0-beta2-windows\bin')



#设置窗口大小
driver.set_window_size(1920,1080)

#最大化窗口
driver.maximize_window()


#发送请求
driver.get("http://www.baidu.com")

#页面截屏
driver.save_screenshot("./baidu.png")



#元素定位的方法
# selenium包是在element（不是internet）中定位可，所以写标签查看网页的element中去看就可以了
driver.find_element_by_id("kw").send_keys("python") #搜索框中输入python
driver.find_element_by_id("su").click()  #点击搜索





'''
#其他定位方法 
driver.find_element_by_link_text("下一页").get_attribute("href")  #定位“下一页”按钮的链接
driver.find_element_by_partial_link_text("下一页").get_attribute("href") #点位含有“下一页”三个字的内容的按钮的链接

find.element 返回一个元素，没有的话会报错
find.elements 返回一个列表，没有的话会返回空列表
'''

time.sleep(3)  #对于有时候需要等下一页加载的时候需要等它加载，不然没地方点，程序会报错。等加载完再进行下一页操作。


# driver获取html字符串

#print(driver.page_source) #浏览器中element的内容，可以以此为基础写x-path



#driver 获取cookie列表
cookies=driver.get_cookies()
print(cookies)
print("+"*100)
    #用字典推导式将列表转化为字典
cookies={i["name"]:i["value"] for i in cookies}
print(cookies)
#退出浏览器
#driver.close()
#driver.quit()
