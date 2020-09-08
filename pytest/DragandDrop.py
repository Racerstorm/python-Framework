from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')

sourceobj = driver.find_element(By.ID, 'draggable')
destobj = driver.find_element(By.ID, 'droppable')

draganddrop = ActionChains(driver)
'''One way of using the drag and drop'''
# draganddrop.drag_and_drop(sourceobj, destobj).perform()

'''Chaining multiple actions to drag and drop'''
draganddrop.click_and_hold(sourceobj)\
    .move_to_element(destobj)\
    .release()\
    .perform()

'''Or write it in a single line like this'''
# draganddrop.click_and_hold(sourceobj).move_to_element(destobj).release().perform()

'''Send keys and Click using Action Chain'''
driver.get('https://www.adobe.com/in/')
action_chain = ActionChains(driver)
searchbtn = driver.find_element(By.CLASS_NAME, 'feds-search-trigger')
action_chain.click(searchbtn).perform()
#emailfield = driver.find_element(By.XPATH, '//input[@type="email"]')
action_chain.send_keys_to_element(searchbtn, 'user@email.com').perform()



