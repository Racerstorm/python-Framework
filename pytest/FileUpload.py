from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://fineuploader.com/demos.html')
driver.find_element(By.NAME, 'qqfile').send_keys('C:\\Users\\ust52622\\Pictures\\sampleimage.png')

driver.get('https://tus.io/demo.html')
driver.find_element(By.ID, 'js-file-input').send_keys('C:\\Users\\ust52622\\Pictures\\sampleimage.png')
