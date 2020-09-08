from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expcon
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import time

driver = None


@pytest.fixture(scope='module')
def setup_module():
    global driver
    print("-------------------Setup module-------------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    browseroptions = webdriver.ChromeOptions()
    browseroptions.add_argument("--start-maximized")
    wait = WebDriverWait(driver, 10)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=browseroptions)

    print("-------------------Teardown module-------------------")
    yield
    # driver.close()

# @pytest.mark.usefixtures("setup_module") or use inside the method call
def test_aexecute(setup_module):
    print("-------------------Main module-------------------")
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    searchkey = driver.find_element_by_name("q")
    searchkey.send_keys("Adobe" + Keys.RETURN)
    homepagelink = driver.find_element_by_xpath("//div[@class='rc']//a[contains(@href,'adobe.com/in')]")
    homepagelink.click()

def test_bexecute2(setup_module):
    driver.get('https://app.hubspot.com/login')
    wait = WebDriverWait(driver, 10)
    wait.until(expcon.title_contains('HubSpot'))
    print(driver.title)

def test_cexecute3(setup_module):
    driver.get('https://fineuploader.com/demos.html')
    driver.find_element(By.NAME, 'qqfile').send_keys('C:\\Users\\ust52622\\Pictures\\sampleimage.png')
    time.sleep(2)

 