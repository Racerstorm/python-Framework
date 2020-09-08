from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browseroptions = webdriver.ChromeOptions()
browseroptions.add_argument("--start-maximized")
browseroptions.add_argument(("--incognito"))
browseroptions.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=browseroptions)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.reddit.com/')
print(driver.title)
'''Screenshots'''
filepath = 'C:\\Users\\ust52622\\Pictures\\'
# driver.get_screenshot_as_file(filepath+'screenshotselenium.png')

'''To take screenshot of the entire page,the following code is used. Make sure browser runs in headless mode.'''

S= lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot(filepath+'fullpagescreenshot.png')
