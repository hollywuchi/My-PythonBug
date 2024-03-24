
from lxml import etree
import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}
# url = "https://www.bilibili.com/read/cv3721263/?from=search&spm_id_from=333.337.0.0"
url = "https://www.bilibili.com/read/cv28123048/?spm_id_from=333.1007.0.0&jump_opus=1"
# url = "https://www.bilibili.com/v/popular/all/?spm_id_from=333.1007.0.0"
request = urllib.request.Request(url = url, headers = headers)
response = urllib.request.urlopen(request)
connect = response.read().decode("utf-8")

with open("b.html",'w',encoding="utf-8")as f:
    f.write(connect)

# tree = etree.HTML(connect)
# request_url = tree.xpath(
#         "//div[@id='app']//div[@class='rql-editor ql-container ql-bubble ql-disabled']/div[@class='ql-editor']/p[@class='normal-img']/img/@src"
#     )
# print(request_url)

path = "msedgedriver.exe"
# driver = webdriver.Edge()
driver = webdriver.Chrome()

driver.get(url)

# search = driver.find_elements(By.XPATH,"//div[@id='app']//div[@class='rql-editor ql-container ql-bubble ql-disabled']/div[@class='ql-editor']/p[@class='normal-img']/img/@src")

# search = driver.find_element("//div[@id='read-article-holder']/h1/text()")
# search = driver.find_elements(By.XPATH,"//p[@class='video-name']")
# time.sleep(5)
# print(len(search))
# for num in range(0,len(search)):
#     print(search[num].get_attribute("title"))
time.sleep(2)
search = driver.find_elements(By.XPATH,"//div[@class='ql-editor']/p[@class='normal-img']/img[@alt='read-normal-img']")
print(len(search))
print(search[0].get_attribute("src")[:-17])
# print(search)