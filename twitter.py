#coding=utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import random
from twitter_scraper import get_tweets
import time
from selenium.webdriver.chrome.options import Options
# coding: utf-8
import sys
driver_path = "/Users/renasami/Desktop/twitter/static/chromedriver"
# options = Options()
# options.add_argument("--headless")
print("1 = aa\n2 = bb \n 3 = cc \nその他 = 打ち込んで♡")
oppai = str(input())
if oppai == "1":
    name = "aa"
    pas = "aaaaa"
elif oppai == "2":
    name = "bb"
    pas = "bbbb"
elif oppai == "3":
    name = "cc"
    pas = "cccc"
else:
    #ユーザー名を入力
    print("@ユーザー名")
    #パスワードを入力
    name = input()
    print("パスワード")
    pas = input()
    #キーワード指定
print("検索したいハッシュタグをキーボードで入力してください")
print("1=#progate\n2=#プログラミング初心者\n3=#駆け出しエンジニアと繋がりたい\nその他は任意で入力")
value = str(input())
if value == "1":
    keyWord = "#dd"
elif value == "2":
    keyWord = "#dd"
elif value == "3":
    keyWord = "#cc"
elif value == "4":
    keyWord = "#bb"
elif value == "5":
    keyWord = "#aa"
else:
    print("設定されてないキーです。")
    print('入力してください')
    keyWord = "#" + input()

driver = webdriver.Chrome(executable_path=driver_path, options=options)
url = "https://twitter.com/login"
driver.get(url)
time.sleep(2)
username = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input')
password = driver.find_element_by_name ('session[password]')
logIn = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
username.send_keys('@' + name)
password.send_keys(pas)
logIn.click()
time.sleep(3)
userID = []
for n in range(3):
    for tweet in get_tweets(str(keyWord) ,1):
        print('--------------------------------------------------------------------------------')
        print(tweet['text'])
        nameofuser = tweet['username']
        print('<<ユーザーネーム:' + nameofuser + '>>')
        if nameofuser in userID:
            print("かぶってる")
        else:
            userID.append(nameofuser)
            print('--------------------------------------------------------------------------------')
            url2 = "https://twitter.com/" + nameofuser
            driver.get(url2)
            time.sleep(3)
            follow = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div > div > div > div > div > div > div:nth-child(1) > div > div.css-1dbjc4n.r-obd0qt.r-18u37iz.r-1w6e6rj.r-1wtj0ep > div > div > div > div')
            follow.click()
print('☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆')  
print(userID)
print('上記' + str(len(userID)) + '人をフォローしました！')
print('☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆')  
driver.quit()
