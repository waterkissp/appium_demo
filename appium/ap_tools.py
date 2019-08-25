# coding=utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from openpyxl import load_workbook
import os
import time
import re


#获取设备系统版本
def platformVersion():
    platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
    platformVersion = platformVersion.replace('\r', '').replace('\n', '').replace('\t', '')  # 清除空白字符
    return (platformVersion)

#获取设备系统名称
def deviceID():
    deviceID = os.popen('adb devices').read()
    deviceID = deviceID.replace('\r', '').replace('\n', '').replace('\t', '')  # 清除空白字符
    return (deviceID.split("List of devices attached")[1].split("device")[0])

#appum初始化设置
def desired_caps(auto2):
    if auto2 =='true':
        desired_caps = {
            'platformName': 'Android',
            'deviceName': deviceID(),
            'platformVersion': platformVersion(),
            'appPackage': 'com.bianla.tangba',
            'appActivity': 'com.bianla.tangba.activity.StartActivity',
            'automationName':'uiautomator2'
        }
    else:
        desired_caps = {
            'platformName': 'Android',
            'deviceName': deviceID(),
            'platformVersion': platformVersion(),
            'appPackage': 'com.bianla.tangba',
            'appActivity': 'com.bianla.tangba.activity.StartActivity'
        }
    return desired_caps
#appum初始化设置

#捕获toast
def find_toast(driver, toast):
    try:
        ele = WebDriverWait(driver, 4).until(expected_conditions.presence_of_element_located((By.XPATH, './/*[contains(@text,'+'\''+toast+'\''+')]')))
        return True
    except:
        return False


#判断界面元素是否存在
def isElement(driver,identifyBy,c):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    time.sleep(1)
    flag=None
    try:
        if identifyBy == "id":
            #self.driver.implicitly_wait(60)
            driver.find_element_by_id(c)
        elif identifyBy == "xpath":
            #self.driver.implicitly_wait(60)
            driver.find_element_by_xpath(c)
        elif identifyBy == "class":
            driver.find_element_by_class_name(c)
        elif identifyBy == "link text":
            driver.find_element_by_link_text(c)
        elif identifyBy == "partial link text":
            driver.find_element_by_partial_link_text(c)
        elif identifyBy == "name":
            driver.find_element_by_name(c)
        elif identifyBy == "tag name":
            driver.find_element_by_tag_name(c)
        elif identifyBy == "css selector":
            driver.find_element_by_css_selector(c)
        flag = True
    except Exception:
        flag = False
    finally:
        return flag

#等待元素出现并返回该元素
def visible_ele(driver, identifyBy, c):
    try:
        if(identifyBy == "id"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, c)))
        elif(identifyBy == "xpath"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,c)))
        elif(identifyBy == "class_name"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,c)))
        elif(identifyBy == "tag_name"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.TAG_NAME,c)))
        elif(identifyBy == "css_selector"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,c)))
        elif(identifyBy == "link_text"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,c)))
        elif(identifyBy == "name"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME,c)))
        elif(identifyBy == "partial_link_text"):
            element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT,c)))

    except UnboundLocalError as e:
        print(e)
    return element

#判断手机号是否合法
def phonelist(a):
    n = a
    if re.match(r'1[3,4,5,7,8]\d{9}', n):
        return 'true'
    else:
        return 'false'

#实例化appium
def appiumDriver(auto2='true'):
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps(auto2))
    return driver

# 获取屏幕高宽
def getSize(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
# 屏幕向左滑动
def swipLeft(driver,t):  #左滑方法，调用此方法传入t参数即可
    l = getSize(driver)
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    driver.swipe(x1, y1, x2, y1, t)

#登录
def login(dr, phone, psw):
    time.sleep(1.5)
    swipLeft(dr, 1000)
    swipLeft(dr, 1000)
    swipLeft(dr, 1000)
    if(isElement(dr, "id", "com.bianla.tangba:id/btn_skip")):
        visible_ele(dr, "id", "com.bianla.tangba:id/btn_skip").click()  # 点击导航页“立即体验”按钮
    visible_ele(dr, "id", "com.bianla.tangba:id/btnEnter").click()  # 点击“注册登陆”按钮
    visible_ele(dr, "id", "com.bianla.tangba:id/etPhone").set_value(phone)  # 输入账号
    visible_ele(dr, "id", "com.bianla.tangba:id/btnNext").click()  # 点击“下一步”
    visible_ele(dr, "id", "com.bianla.tangba:id/etPassword").set_value(psw) # 输入密码
    visible_ele(dr, "id", "com.bianla.tangba:id/btnEnter").click()  # 点击登陆
