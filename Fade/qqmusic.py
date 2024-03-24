#无限期搁置……
#直到找到新的BUG
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup


def download(url,user_agent="wswp",num_retries=2):
    if url is None:
        return None 
    print("Downloading:",url)
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    request = urllib.request.Request(url = url, headers = headers)
    #设置用户代理wswp

    try:
        html = urllib.request.urlopen(request).read().decode("utf-8")
    except urllib.error.URLError as e:
        print("Downloading Error:",e.reason)
        html = None
    if num_retries > 0:
        if hasattr(e,"code") and 500 < e.code < 600:
            return download(url,num_retries-1)
        return html

def music_scrpter(html,page_num = 0):
    try:
        soup = BeautifulSoup(html,"html.parser")
        mod_songlist_div = soup.find_all("div",class_ = "mod_songlist")
        songlist_ul = mod_songlist_div[1].find("ul",class_ = "songlist_list")
        print("开始解析歌曲信息")
        print(songlist_ul)
        # lis = songlist_ul.find()
    except:
        print("Error")


# if __name__ == "__main__":