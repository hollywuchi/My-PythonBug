from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request

url = "http://192.168.83.4:8085/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

requests = urllib.request.Request(url = url ,headers=headers)
response = urllib.request.urlopen(requests)
content = response.read().decode("utf-8")

print(content)