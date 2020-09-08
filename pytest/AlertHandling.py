from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

alert_reference = driver.switch_to.alert
print(alert_reference.text)

alert_reference.accept()
driver.switch_to.default_content()
driver.refresh()
'''The following line is used when the user is expected to enter something into the alert'''
# alert_reference.send_keys('Alert disappear')

'''Handling basic authentication popup'''

driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

# elem = driver.find_element(By.XPATH, '//input[@name="fldLoginUserId"]')
# elem.send_keys(Keys.RETURN)
# alert_reference=driver.switch_to.alert
# print(alert_reference.text)
# alert_reference.dismiss()
