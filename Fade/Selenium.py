import time
#——————————————————————————————————————————————————————————————————————————————————

#在使用xPath来爬部分网站的时候总会遇到各式各样的反爬手段：
#比如说：B站的热门不会被轻易的爬下来（那个难忘的上午）

#selenium 可以用引擎来模拟一个真实的浏览器，并且模拟一个真实的用户来实现访问：
#从而减少服务器的访问限制

#——————————————————————————————————————————————————————————————————————————————————

#注意：使用最新版的selenium打开chrome浏览器时，Chrome浏览器的驱动会在执行完脚本对应的操作之后关闭浏览器
#产生类似"闪退"的假象。实际上对于代码的执行都是没有影响的
#换掉其他的浏览器，例如火狐，就不会闪退

#——————————————————————————————————————————————————————————————————————————————————
#尝试使用selenium打开一个网页

#（1）导入selenium
#     因为尚硅谷的教程版本太旧了，所以要学习新的，就要多导入一个
from selenium import webdriver
from selenium.webdriver.common.by import By

#（2）创建浏览器操作对象（因为没有配置环境变量）
# path = "chromedriver.exe" 

# brower = webdriver.Chrome()
# (3)访问网站

# url = "http://www.bilibili.com"
# url = "https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0"

# brower.get(url)

# #page_source获取网页源码
# # print(content)

#新版的selenium在打开谷歌浏览器执行完对应的任务之后会自动关闭浏览器从而回收资源
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver.get("http://www.bilibili.com")
# driver.get("https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0")
# driver.get("http://www.baidu.com")

# import time
# time.sleep(3)

# print(driver.title)

# content = driver.page_source
# with open("BiliBili.html","w",encoding = "utf-8") as f:
#     f.write(content)

#——————————————————————————————————————————————————————————————————————————————————

#尝试在打开的网页中自动化进行一些操作

#因为已经配置了环境变量，所以不用再写路径让代码去找驱动引擎了
# driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")

#找到搜索框然后将要搜索的词条发送过去，点击搜索按钮

# button = driver.find_element(By.ID,"kw").send_keys("我的世界")
# driver.find_element(By.ID,"su").click()

#——————————————————————————————————————————————————————————————————————————————————

#控制浏览器的一些很有意思的小指令

# time.sleep(3)
# driver.back() #暂停三秒之后点击返回按钮
# time.sleep(3)
# driver.forward() #前进按钮
# time.sleep(3)
# driver.refresh() #刷新按钮
# time.sleep(3)
# driver.minimize_window() #最小化窗口
# time.sleep(2)
# driver.maximize_window() #最大化窗口
# time.sleep(1)
# driver.fullscreen_window() #全屏
# time.sleep(1)
# driver.set_window_size(1280,720) #调节浏览器窗口大小
# time.sleep(3)
# driver.quit() #等待3秒退出浏览器

#——————————————————————————————————————————————————————————————————————————————————

#更加详细的元素定位与简易交互:

# driver = webdriver.Firefox()
# driver = webdriver.Edge()
# driver.get("http://baidu.com")
# driver.get("https://bilibili.com")
# driver.get("https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0")
# driver.get("https://y.qq.com")

# search = driver.find_element(By.XPATH,"//input[@id='kw']")
# search.send_keys("我的世界")
# button = driver.find_element(By.XPATH,"//input[@id='su']")
# button.click()

#百度翻译，获取翻译结果
# search = driver.find_element(By.XPATH,"//textarea[@id='baidu_translate_input']")
# search.send_keys("selenium")


# search = driver.find_element(By.XPATH,"//input[@class='nav-search-input']")
# search.send_keys("电摇")
# driver.find_element(By.XPATH,"//div[@class='nav-search-btn']").click()
# search.clear()
# search.send_keys("Python")
# search.submit()

#get_attribute 获取标签的属性值
# search = driver.find_elements(By.XPATH,"//p[@class='video-name']")
# print(len(search))
# for num in range(0,len(search)):
#     print(search[num].get_attribute("title"))

#By.LINK_TEXT是指获取链接的按钮
# search = driver.find_element(By.LINK_TEXT,"新闻")
# print(search.text)
# search.click()

#鼠标滚轮向下滚动多少像素值
# for num in range(0,4):
#     js = f"window.scrollTo(0,{500*num});"
#     driver.execute_script(js)
#     time.sleep(1)


# driver.find_element(By.XPATH,"//a[@class='top_login__link']").click

# time.sleep(10)

# button = driver.find_element(By.XPATH,"//span[@class='img_out_focus']").click

# time.sleep(5)

# time.sleep(5)
# driver.quit()

#——————————————————————————————————————————————————————————————————————————————————

#Chrome-headless:对比浏览器的图形化操作界面,headless的无图形操作效率要更高

#以下为固定的格式

# from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")

#结论:过时教程,之后在学
#——————————————————————————————————————————————————————————————————————————————————

