from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.spicejet.com/default.aspx')
time.sleep(5)
headerone = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
action_chains = ActionChains(driver)
action_chains.move_to_element(headerone).perform()
driver.implicitly_wait(10)
headertwo = driver.find_element(By.XPATH, '//a[text()="SpiceClub Members"]')
action_chains.move_to_element(headertwo).perform()
driver.implicitly_wait(10)
linktoclick = driver.find_element(By.LINK_TEXT, 'Member Login')
linktoclick.click()
time.sleep(5)

'''Send keys and Click using Action Chain'''
driver.get('https://www.adobe.com/in/')
action_chain = ActionChains(driver)
searchbtn = driver.find_element(By.CLASS_NAME, 'feds-search-trigger')
action_chain.click(searchbtn).perform()
#emailfield = driver.find_element(By.XPATH, '//input[@type="email"]')
action_chain.send_keys_to_element(searchbtn, 'user@email.com').perform()

driver.quit()