from appium import webdriver
import time


desired_caps = {
  "platformName": "Android",
  "platformVersion": "8.1",
  "deviceName": "a9870a1e",
  "browserName": "Chrome"
}

if __name__ == '__main__':
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.get("https://m.so.com")
    print(driver.w3c)
    # driver.send_sms("13281549858", "hello")
    driver.implicitly_wait(100)
    driver.execute_script()
    time.sleep(3)
    # driver.switch_to.alert.accept()
    # driver.find_element_by_id("index-kw").click()
    # driver.find_element_by_id("index-kw").send_keys(213)
    # driver.find_element_by_class_name("se-input").send_keys(1)

    # driver.find_element_by_id("index-bn").click()
    driver.find_element_by_id("q").send_keys("ret")
    driver.find_element_by_class_name("search-btn").click()
