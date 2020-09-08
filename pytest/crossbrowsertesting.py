from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time

browsername = 'Firefox'

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
driver.get("https://www.amazon.in/")
#driver.find_element(By.NAME, 'q').send_keys("Adobe")
#optionsList = driver.find_elements(By.XPATH, '//ul[@class="erkvQe"]/li/div/div[2]/div/span')
linkslist = driver.find_elements(By.TAG_NAME, 'a')
print(len(linkslist))
#print(len(optionsList))

for ele in linkslist:
    print(ele.text)
    print(ele.get_attribute('href'))
    if ele.text == 'Mobiles':
      ele.click()
      break

imagelist = driver.find_elements(By.TAG_NAME, 'img')
print(len(imagelist))

for ele in imagelist:
    print(ele.get_attribute('src'))

time.sleep(10)
driver.quit()



