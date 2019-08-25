from selenium import webdriver


options = webdriver.ChromeOptions()
# options.add_experimental_option('androidPackage', 'com.android.chrome')
# options.add_experimental_option('androidPackage', 'com.easygroup.ngaripatient')
# options.add_experimental_option('androidActivity', 'com.easygroup.ngaripatient.webview.H5WebActivity')
# options.add_experimental_option('androidUseRunningApp', True)
# options.add_experimental_option('androidDeviceSerial', '192.168.56.104:5555')

options.add_argument('start-fullscreen')

driver = webdriver.Chrome('chromedriver', options=options)
driver = webdriver.Chrome(options=options)
driver.get('https://www.baidu.com')
print(driver.session_id)
print(driver.capabilities)
# driver.find_element_by_id("index-kw").send_keys("213")
# driver.find_element_by_id("index-bn").click()
# driver.quit()

# app = self._d.current_app()
#         print(app)
#         capabilities = {
#             'chromeOptions': {
#                 'androidDeviceSerial': self._d.serial,
#                 'androidPackage': package or app["package"],
#                 'androidUseRunningApp': attach,
#                 'androidProcess': process or app["package"],
#                 'androidActivity': activity or app["activity"],
#             }
#         }
#
# dr = webdriver.Remote('http://localhost:%d' % self._port, capabilities)