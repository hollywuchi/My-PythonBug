import scrapy
from lxml import etree
import urllib.request
import os
import re
     
def request_packge(url_article):
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
        }
        
    request = urllib.request.Request(url = url_article,headers = headers)

    response_chaper = urllib.request.urlopen(request)

    content_chaper = response_chaper.read().decode("utf-8")
    tree = etree.HTML(content_chaper)
    
    return tree



def resolving(response):
    try:
        print("开始解析……")
        auther = response.xpath("//ul[@class='clearfix']/li/a/@href")

        urls = []

        for i in range(len(auther)):
            if auther[i].extract()[0:4] != "/vip":
                url_article = "https://book.sfacg.com" + auther[i].extract()
                urls.append(url_article)
                
            else:
                return urls
            
        return urls
    except:
        print("你输入的网址出现了问题，请重试")
    

#检测特殊字符导致的下载失败
def has_special_chars(str):
    padttern = r"[/]"
    if re.search(padttern,str):
        return True
    else:
        return False

#寻找正文内容
def find_book_text(tree):
    book_text = tree.xpath("//div[@class='article-content font16']/p/text()")
    return book_text
#整本书的名字
def find_book_name(response):
    book_Name = response.xpath("//div[@class='story-head']/h1/text()")
    return book_Name.extract()
#章节标题
def find_chaper_Name(tree):
    Chaper_Name = tree.xpath("//div[@class='article-hd']/h1/text()")
    return Chaper_Name
#新建这本书的文件夹
def check_file(book_Name):
    print("解析完成")
    print("正在检查下载路径")
    save_path = f".\{book_Name}"
    if os.path.exists(save_path):
        print("下载路径正常")
    else:
        print("下载路径失效")
        print("开始创建新的下载路径" + save_path)
        os.mkdir(save_path)
        print("即将开始下载")
# 下载这本书
def download(book_name,chaper_name,book_text):

    print(f"开始下载{book_name}")
    try:

        if(has_special_chars(chaper_name[0])):
            chaper_name[0] = chaper_name[0][0-4]
        else:
            chaper_name[0] = chaper_name[0]
        with open(f"{book_name}/{chaper_name[0]}.txt","a",encoding = "utf-8") as f:
            f.write("----------------------------------------------------------\n")
            f.write(chaper_name[0] + "\n")
            f.write("----------------------------------------------------------\n")
            for line in range(len(book_text)):
                line_text = book_text[line]
                f.write(line_text + "\n")
        print(f"{chaper_name} 下载完成")
    except FileNotFoundError:
        print("下载失败")
class SfdSpider(scrapy.Spider):
    url_novel_input = input("请输入小说目录页面的链接(按下 Ctrl+V 粘贴)")
    name = "SFD"
    allowed_domains = ["book.sfacg.com"]
    start_urls = [url_novel_input]
    def parse(self, response):

        print("————————————————————————————————————————————————————————————————")

        urls = resolving(response)
        book_name = find_book_name(response)
        check_file(book_name)

        for i in range(len(urls)):
            tree = request_packge(url_article = urls[i])
            chaper_name = find_chaper_Name(tree)
            book_text = find_book_text(tree)
            download(book_name,chaper_name,book_text)

        print("呼，总算下载完了")
        input("按Enter键结束本程序")  
        

        print("————————————————————————————————————————————————————————————————")
                

