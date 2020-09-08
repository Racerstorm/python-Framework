from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browsername = 'Chrome'

if browsername == 'Chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browsername == 'Firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

elif browsername == 'Edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

else:
    print(browsername+' is not a valid browser. Please enter a valid browser name.')
    raise Exception('Driver is not found')

#driver = webdriver.Chrome(executable_path='C:\\Automation\\Webdrivers\\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')

def select_action(element, option, value):
    print('----------Inside default select method----------')
    select = Select(element)

    if option =='text':
        select.select_by_visible_text(value)

    elif option == 'index':
        select.select_by_index(value)

    elif option == 'value':
        select.select_by_value(value)

    else:
        print(option+ ' is not a valid value. Please enter a valid select option.')
        raise Exception('Option is not present')

def custom_select_action(dropdownlist, value):
    print('----------Inside custom select method----------')
    print(len(dropdownlist))

    for el in dropdownlist:
        if el.text == value:
            el.click()
            break

dropdown = driver.find_element(By.NAME, 'Industry')
select_action(dropdown,'index','7')

countrydropdown = driver.find_elements(By.XPATH, '//select[@name="Country"]/option')
custom_select_action(countrydropdown,'India')

select = Select(dropdown)
selectList = select.options

for opt in selectList:
    print(opt.text)
    break

#print(len(countrydropdown))
# for country in countrydropdown:
#     print(country.text)
#     if country.text == 'India':
#         country.click()
#         break

#select = Select(dropdown)
#select.select_by_visible_text('Automotive')
#select.select_by_index(7)
