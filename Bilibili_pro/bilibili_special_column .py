from lxml import etree
import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

# 请求对象的定制
def creat_request(url):
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    connect = response.read().decode("utf-8")
    tree = etree.HTML(connect)
    return tree

# 获取图片地址
def resolving_url(tree):
    print("开始解析")
    request_url = tree.xpath(
        "//div/div/div/div/div[@id='read-article-holder']/figure[@class='img-box']/img/@data-src")
    return request_url
def resolving_url_2(url):
    # driver = webdriver.Edge()
    driver = webdriver.Chrome()
    # 使用edge浏览器
    driver.minimize_window()
    driver.get(url)
    time.sleep(2)
    request_url_1 = driver.find_elements(By.XPATH,"//div[@class='ql-editor']/p[@class='normal-img']/img[@alt='read-normal-img']")
   
    for i in range(0,len(request_url_1)):
        request_url = request_url_1[i].get_attribute("src")[:-17]
        DownLoad(request_url,request_pid=None,model= True,model_num=2,name=i)
        time.sleep(2)
    print("下载结束,记得把图片转移位置哦")
    

# 获取图片下方简介
def resolving_pid(tree):
    request_pid = tree.xpath(
        "//div[@id='read-article-holder']/figure/figcaption/text()")
    return request_pid

# 判断要使用的下载方式
def DownLoad_Check(request_url,request_pid):
    print("解析结束")
           
    if len(request_pid) != len(request_url):
        print("检测到图片简介与图片数量不符，启用安全模式下载")
        model = True
    else:
        print("启用正常模式下载")
        model = False
    print("图片数量：" + str(len(request_url)))
    print("简介数量：" + str(len(request_pid)))
    return model
    
    
# 下载函数
def DownLoad(request_url,request_pid,model,model_num,name):
    if model_num == 1:
        print("开始下载")
        for i in range(len(request_url)):
            url = request_url[i]
            print("http:"+url)
            # 下载图片
            if model:
                urllib.request.urlretrieve(
                    url="http:" + url, filename="./BilibiliImg/" + str(i) + ".jpg")
                
            else:
                name = request_pid[i]
                print(name)
                urllib.request.urlretrieve(
                    url="http:" + url, filename="./BilibiliImg/" + name + ".jpg")
        print("下载成功")
        print("下载结束,记得把图片转移位置哦")
    
    if model_num == 2:
        print("开始下载" + request_url)
        urllib.request.urlretrieve(
            url = request_url,filename="./BilibiliImg/" + str(name) + ".jpg"
        )
        # ————————————————————————————————————————————————————————————
        # r = requests.get(request_url,stream=True)
        # with open(f"./BilibiliImg/" + str(name) + ".jpg",'wb') as f:
        #     for chuck in r.iter_content(chunk_size=1024):
        #         if chuck:
        #             f.write(chuck)
        #             f.flush()
        
        print("下载完成")
    

# 分析文件夹是否存在
def check_file():
    save_path = ".\BilibiliImg"
    if os.path.exists(save_path):
        print("下载路径正常")
    else:
        print("文件夹不存在，将进行创建" + save_path)
        os.mkdir(save_path)

# 主程序运行处
if __name__ == "__main__":
    # if ifnum == 0:
    #     start_page = int(input("请输入起始页码"))
    #     end_page = int(input("请输入结束页码"))
    #     for page in range(start_page, end_page+1):
    #         url = creat_URL(page)
    #         connect = creat_request(url)
    #         resolving(connect)

    # else:
    try:
        url_1 = str(input("请输入网址？(按下ctrl+v粘贴)"))
    except:
        print("出现意想不到的错误力")
    check_file()
    tree = creat_request(url_1)
    url = resolving_url(tree)
    pid = resolving_pid(tree)
    model = DownLoad_Check(url,pid)
    if len(url) == 0:
        print("未检测到图片")
        print("即将尝试其他方式")
        url = resolving_url_2(url_1)
        # DownLoad(url,pid,model = True)
        
    else:
        print("开始下载（方法1）")
        DownLoad(url,pid,model,1,name=None)

    
# 防闪现设置
input("按任意键退出")