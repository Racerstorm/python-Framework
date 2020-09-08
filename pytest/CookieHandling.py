from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.reddit.com/')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//a[text()="View all"]').click()
time.sleep(2)
print(driver.title)

driver.back()
print(driver.title)
time.sleep(2)
driver.forward()
print(driver.title)

# cookies = driver.get_cookies()
#
# for cookie in cookies:
#     print(cookie)

driver.add_cookie({"name":"SeleniumAutomation", "value":"Python"})

print(driver.get_cookies())