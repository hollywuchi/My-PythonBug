import requests
import urllib

#——————————————————————————————————————————————————————————————————————————————
#request与Urllib非常相似
#——————————————————————————————————————————————————————————————————————————————

#request 的get请求

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
# }

# url = "https://www.baidu.com/s?"


# #与urllib相比，request不需要编码。因为request是唯一一个“非转基因”的Python库
# data ={
#     "wd":"我的世界"
# }
# # data = {
# #     "wd":"我的世界",
# #     "location":"中国",
# #     "type":"game"
# # }
# # new_data = urllib.parse.urlencode(data)

# response = requests.get(url = url,params = data,headers = headers)

# content = response.text

# with(content)


#——————————————————————————————————————————————————————————————————————————————

#总结：
#此刻，与urllib的区别就有一些了
#参数使用params传递
#不需要请求对象的定制
#请求资源路径中的？可以加也可以不加

#——————————————————————————————————————————————————————————————————————————————

#request的post请求

# url = "https://fanyi.baidu.com/sug"

# data ={
#     "kw":"apple"
# }

#首先复习以下之前的urllib post请求
#post请求必须要进行编码才可以实现中文的阅读，并且是进行两次编码才可以进行阅读
#data = urllib.parse.urlencode(data).encode("utf-8")

#但是request提供了一个全新的思路，他提供了一个post请求，不需要对data编码就可以运行

# response = requests.post(url = url,data = data ,headers = headers)

# content = response.text

# import json

# obj = json.loads(content.encode("utf-8"))

# with(obj)

#总结：
#相对于urllib的post，request的post是一个请求，可以直接调用，
#post的请求参数是data，get请求参数是params
#相同的，不需要请求对象的定制

#——————————————————————————————————————————————————————————————————————————————

#request的代理使用

# url = "https://www.baidu.com/s?"

# proxy = {
#     "113.124.86.186":"9999"
# }

# data ={
#     "wd":"ip"
# }

# respose = requests.get(url = url , params = data ,headers = headers,proxies = proxy)

# content = respose.text

# with open("daili.html","w",encoding = "utf-8") as f:
#     f.write(content)

#——————————————————————————————————————————————————————————————————————————————

# url = "https://u.y.qq.com/cgi-bin/musics.fcg?_=1700101610984&sign=zzbe73ca46cnoova1ahwzw7boi4mpxg227c8f27"

# middata = 'data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2462922659,"g_tk_new_20200303":1417578329,"g_tk":1417578329},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["2462922659"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["2462922659"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1808433485","songmid":["002b4LF810mHRC"],"songtype":[0],"uin":"2462922659","loginflag":1,"platform":"20"}},"req_5":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["002b4LF810mHRC"]}},"req_6":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"002b4LF810mHRC","songID":3596006}},"req_7":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"3596006","biz_sub_type":0}]}},"req_8":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003W5t102sjVNj"}},"req_9":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6608277428","songmid":["002b4LF810mHRC"],"songtype":[0],"uin":"2462922659","loginflag":1,"platform":"20"}}}: '

# middata = 'data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2462922659,"g_tk_new_20200303":1417578329,"g_tk":1417578329},"req_9":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6608277428","songmid":["002b4LF810mHRC"],"songtype":[0],"uin":"2462922659","loginflag":1,"platform":"20"}}}'

# middata = 'data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":386978147,"g_tk":386978147},"req_6":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"295571183","songmid":["004DXFlC0nsTCZ"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}}}:'

# middata = 'data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":386978147,"g_tk":386978147},"req_1":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"236139870","songmid":["004DXFlC0nsTCZ"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
#     # "Referer":"https://y.qq.com/",
#     # "Origin":"https://y.qq.com",
#     # "Cookie":"pgv_pvid=2513688940; fqm_pvqid=e17d28c3-1f8b-48bc-8635-36b41c4b3f0d; fqm_sessionid=79e62aaa-d788-4a87-83fd-c6e2b4407d80; pgv_info=ssid=s9834334425; ts_last=y.qq.com/; ts_uid=5356938120; _qpsvr_localtk=0.7486418602696889; RK=Ed3AyNvMsn; ptcz=4508d92e355779e45540ba467302d9a92a0542fbda5c486b3051398f10e4eb3a; login_type=1; psrf_qqrefresh_token=F82255524A559A965E00C2D96D7BB7A4; euin=owvsowEAowCkNv**; tmeLoginType=2; music_ignore_pskey=202306271436Hn@vBj; uin=2462922659; wxrefresh_token=; psrf_access_token_expiresAt=1707810892; psrf_musickey_createtime=1700034892; psrf_qqopenid=31B489F266AF418EC3A3A3D187C1049F; wxopenid=; psrf_qqaccess_token=EF81B9BB498B8B27EEE4D52267914E03; wxunionid=; psrf_qqunionid=42B0FC260E748B2250F955716893E53E; qm_keyst=Q_H_L_5bzjVc5l_qc621mhfQymk6ovEKWU-Tiwq_C1QKL1z5NtnoNwEotqKoA; qqmusic_key=Q_H_L_5bzjVc5l_qc621mhfQymk6ovEKWU-Tiwq_C1QKL1z5NtnoNwEotqKoA"
# }

# data = {
#     "w":"Jar Of Love"
# }

# response = requests.post(url,data = middata,headers = headers)

# response = requests.get(url = url+middata,headers = headers)

# response.encoding = "utf-8"

# content = response.text

# with(content)

# with(content)
# # with open("qq.html","w",encoding="utf-8") as f:
# #     f.write(content)

# from lxml import etree

# # request = etree.

#—————————————————————————————————————————————————————————————————————————————————————————————————————————


# import requests
# import json
# from bs4 import BeautifulSoup
# import urllib.request

#解析并使用request登录古诗文网

#解析：想要登录，要看古诗文网登录需要什么值，
    #共需要三个值：__VIEWSTATE  __VIEWSTATEGENERATOR    验证码
    #获取前两个值比较简单，因为只需要进行bs或其他的解析就可以直接提取
    #剩下的验证码是比较难的


url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
}

response = requests.get(url = url ,headers = headers)

content = response.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(content,"lxml")

#获取__VIEWSTATE
#复习bs的select：
#这是一个收集所有关于“id=”#后值的方法
#返回的是一个列表，所以要用列表的方式来调用里面的方法
viewstate = soup.select("#__VIEWSTATE")[0].attrs.get("value")

#复习找到id之后来获取其中之一的属性值：
#使用attrs.get("class")获取其中的class属性的值
#使用attrs.get("value")获取其中的value属性的值

viewstategenerator = soup.select("#__VIEWSTATEGENERATOR")[0].attrs.get("value")

# with(viewstategenerator)

#获取验证码图片

#PS:
# 在chrome浏览器中有这样一个选项：Preserve log
# 表示保存上一个网站的动态活动，不至于在下一个网站加载的时候将其删掉
# 一个例子：在登录界面登录成功之后，下一个界面加载出来之后上一个登录的界面的数据不会消失

Y_img = soup.select("#imgCode")[0].attrs.get("src")
code_url = "https://so.gushiwen.cn" + Y_img

#下一步是保存这个图片（可以用）urllib.request

#注意！！！！！
#这里的下载的验证码与下面需要的验证码并不是一个
# import urllib.request
# urllib.request.urlretrieve(code_url,"code.jpg")

#我们需要使用request中的一个方法：session来统一
#使用sessoin来干预，将其包装成一个“对象”
session = requests.session()
#验证码url的内容
response_code = session.get(code_url)
#这里打印出来是二进制的内容
content_code = response_code.content
#要使用‘wb’来转换
with open('code.jpg','wb') as f:
    f.write(content_code)

code = input("请输入验证码")

#登陆的网址
url_post = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"

data_post = {
    "__VIEWSTATE": viewstate,
    "__VIEWSTATEGENERATOR": viewstategenerator,
    "from": "http://so.gushiwen.cn/user/collect.aspx",
    "email": "15725095527",
    "pwd": "7418695230.q",
    "code": code,
    "denglu": "登录",
}

response_post = session.post(url = url_post,headers = headers,data = data_post)

content_post = response_post.text

with open("gushiwen.html","w",encoding = "utf-8") as f:
    f.write(content_post)

#成功：
#   要注意的点：
#   1.隐藏_viewstate的查找
#   2.request.session()封装为一个对象，实现验证码统一

#——————————————————————————————————————————————————————————————————————————————————————————————————————————

