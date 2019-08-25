from selenium import webdriver

capability = {
    "browserName": "firefox",
    "marionette": True,
    "acceptInsecureCerts": True,
}
if __name__ == '__main__':
    driver = webdriver.Remote("http://192.168.1.103:7279/wd/hub", capability)
    driver.get("https://www.baidu.com")
    driver.quit()
