from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

'''Right/Context Click'''
action_chain = ActionChains(driver)
element = driver.find_element(By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]')

action_chain.context_click(element).perform()


'''To get the list of options after right clicking'''
rightclickoptions_list = driver.find_elements(By.XPATH, '//li[contains(@class,"context-menu-item")]/span')
for ele in rightclickoptions_list:
    print(ele.text)
    if ele.text == 'Edit':
        ele.click()
        break;




driver.quit()




