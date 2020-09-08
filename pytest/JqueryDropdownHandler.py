from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('http://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')


def jquery_dropdown_action(dropdownvalues, listofvalues):
    if not listofvalues[0] == 'all':
        # This traverses the elements in the dropdown
        for element in dropdownvalues:
            print(element.text)
            # Now the second loop is required to traverse the list provided as the second parameter
            for indexvar in range(len(listofvalues)):
                # If the value.text from the dropdown equals value[index] provided as the second parameter(list)
                if element.text == listofvalues[indexvar]:
                    element.click()
                    break

    else:
        try:
            for element in dropdownvalues:
                element.click()
        except Exception as e:
            print(e)




dropdown = driver.find_element(By.ID, 'justAnInputBox')
dropdown.click()
valuesindropdown = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
# valuestobechecked = ['choice 1', 'choice 3', 'choice 6 2 1', 'choice 6 2 2', 'choice 6 2 3']
valuestobechecked = ['all']
jquery_dropdown_action(valuesindropdown, valuestobechecked)

time.sleep(5)

driver.quit()
