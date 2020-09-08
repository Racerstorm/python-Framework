from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expcon

browseroptions = webdriver.ChromeOptions()
browseroptions.add_argument("--start-maximized")
#browseroptions.add_argument(("--incognito"))
#browseroptions.headless=True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=browseroptions)
#driver.implicitly_wait(10)
# driver.maximize_window()

def element_border(element):
    '''Create a border for an element using JS'''
    driver.execute_script("arguments[0].style.border = '3px solid red'", element)

driver.get('https://app.hubspot.com/login')
wait = WebDriverWait(driver, 10)
wait.until(expcon.title_contains('HubSpot'))

print(driver.title)
# driver.find_element(By.ID, 'username').send_keys('userone@email.com')
email_field = wait.until(expcon.presence_of_element_located((By.ID, 'username')))
element_border(email_field)
email_field.send_keys("userone@email.com")
password_field = driver.find_element(By.ID, 'password')
element_border(password_field)
password_field.send_keys('userone@email.com')

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.find_element(By.NAME, 'proceed').click()
alerthandler = wait.until(expcon.alert_is_present())
print(alerthandler.text)
alerthandler.dismiss()

driver.get('https://developers.google.com/')
footerlinks = wait.until(expcon.presence_of_all_elements_located((By.XPATH, '//li[@class="devsite-footer-linkbox-item"]')))
print(len(footerlinks))

for footer in footerlinks:
    print(footer.text)