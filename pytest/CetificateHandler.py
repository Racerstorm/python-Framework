from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as expcon
import time

browseroptions = webdriver.ChromeOptions()
browseroptions.add_argument("--start-maximized")
#browseroptions.add_argument(("--incognito"))
'''Method 1'''
#browseroptions.add_argument(("--allow-running-insecure-content"))
#browseroptions.add_argument(("--ignore-certificate-errors"))

'''Method 2'''
# DesiredCaps = DesiredCapabilities().CHROME.copy()
# DesiredCaps['acceptInsecureCerts'] = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=DesiredCaps)

'''Method 3'''
browseroptions = Options()
browseroptions.set_capability("acceptInsecureCerts", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=browseroptions)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get('https://expired.badssl.com/')
print(driver.find_element(By.TAG_NAME, 'h1').text)
