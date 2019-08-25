from appium import webdriver
import time

desired_caps = {
  "platformName": "Android",
  "platformVersion": "9",
  # "deviceName": "a9870a1e",
  "deviceName": "192.168.56.105:5555",
  "automationName": "UiAutomator1",
  # "appPackage": "com.easygroup.ngaripatient",
  # "appActivity": "",
  "app": "/home/ooka/Downloads/com.easygroup.ngaripatient.apk",
  "noReset": "true"
}


if __name__ == '__main__':
  driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
  driver.implicitly_wait(30)
  time.sleep(3)
  driver.background_app(1)
  driver.find_element_by_id("com.easygroup.ngaripatient:id/textView_appoint").click()
  # driver.switch_to('com.easygroup.ngaripatient.webview.H5WebActivity')
  # driver.context('com.easygroup.ngaripatient.webview.H5WebActivity')
  time.sleep(3)
  print(driver.contexts)
  driver.switch_to.context('WEBVIEW_com.easygroup.ngaripatient')
  driver.refresh()
  # driver.find_element_by_class_name("my-appoint").click()
  time.sleep(2)
  print(driver.title)
  driver.find_element_by_class_name('my-appoint').click()
  driver.switch_to.context('NATIVE_APP')
  driver.background_app(1)
  driver.find_element_by_id("com.easygroup.ngaripatient:id/actionbar_navigation").click()
  driver.find_element_by_id("com.easygroup.ngaripatient:id/textView_appoint").click()

