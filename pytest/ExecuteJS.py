from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcon
import time

browseroptions = webdriver.ChromeOptions()
browseroptions.add_argument("--start-maximized")
#browseroptions.add_argument(("--incognito"))
driver = webdriver.Chrome(ChromeDriverManager().install(), options=browseroptions)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
'''Method Dropdown Handling'''
def custom_select_action(dropdownlist, value):
    print('----------Inside custom select method----------')
    print(len(dropdownlist))

    for el in dropdownlist:
        print(el.text)
        if el.text == value:
            el.click()
            break

'''Method - Border color for element'''
def element_border(element):
    '''Create a border for an element using JS'''
    driver.execute_script("arguments[0].style.border = '3px solid red'", element)


driver.get('https://www.ubisoft.com/en-us/')
title = driver.execute_script("return document.title;")
print(title)

watchbutton = wait.until(expcon.presence_of_element_located((By.XPATH, '//span[text()="WATCH TRAILER"]')))
element_border(watchbutton)
# driver.execute_script("arguments[0].style.border = '3px solid red'", watchbutton)
driver.execute_script("arguments[0].click();", watchbutton)

monthdropdown = wait.until(expcon.presence_of_all_elements_located((By.XPATH, '//select[@name="selectedMonth"]/option')))
# = driver.find_element(By.XPATH, '//select[@name="selectedMonth"]/option')
daydropdown = driver.find_elements(By.XPATH, '//select[@name="selectedDay"]/option')
yeardropdown = driver.find_elements(By.XPATH, '//select[@name="selectedYear"]/option')

custom_select_action(monthdropdown, 'MARCH')
custom_select_action(daydropdown, '6')
custom_select_action(yeardropdown, '1994')

submitbutton = driver.find_element(By.XPATH, '//span[text()="Submit"]')
driver.execute_script("arguments[0].click();", submitbutton)
driver.find_element(By.XPATH, '//button[@class="modal__header__closeBtn"]').click()

'''JS SCROLL TO THE BOTTOM OF THE PAGE - 0 to scroll height. Scroll height to 0 for scrolling from bottom to top'''
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

'''JS SCROLL INTO VIEW SCRIPT'''
element_to_be_scrolled_to = driver.find_element(By.XPATH, '//span[text()="Join Now"]/..')
driver.execute_script("arguments[0].scrollIntoView(true);", element_to_be_scrolled_to)











'''Checking the same scroll functionality on a different site'''
driver.get('https://www.amazon.in/')
scrolltillthiselement = driver.find_element(By.XPATH, '//span[contains(text(),"Deals")]')
driver.execute_script("arguments[0].scrollIntoView(true);", scrolltillthiselement)
print(driver.execute_script("return navigator.userAgent;"))

