from appium import webdriver
import time

desired_caps = {
  "platformName": "Android",
  "platformVersion": "8.1",
  "deviceName": "a9870a1e",
  "automationName": "UiAutomator2",
  "appPackage": "com.easygroup.ngaripatient.tianjinertong",
  "appActivity": "com.easygroup.ngaripatient.welcome.WelcomeGuideActivity",
  # "app": "/home/ooka/eclipse-workspace/tianjiner.apk",
  "noReset": "true"
}

if __name__ == '__main__':
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(30)
    # driver.find_element_by_id('com.easygroup.ngaripatient.tianjinertong:id/username').send_keys("13281549858")
    driver.background_app(1)
    driver.find_element_by_id("com.easygroup.ngaripatient.tianjinertong:id/icon_main").click()
    print(driver.contexts)
    driver.switch_to.context('WEBVIEW_com.easygroup.ngaripatient.tianjin')
    print(driver.current_url)
