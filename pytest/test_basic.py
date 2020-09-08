from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from lib2to3.pgen2 import driver
import time

@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\Automation\Webdrivers\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
   
def test_execute(test_setup):
    driver.get("https://www.google.com")
    searchkey=driver.find_element_by_name("q")
    searchkey.send_keys("Adobe" + Keys.RETURN)
    homepagelink = driver.find_element_by_xpath("//div[@class='rc']//a[contains(@href,'adobe.com/in')]")
    homepagelink.click()
    
    adobepagesearch = driver.find_element_by_xpath("//a[@class='feds-search-trigger']")
    adobepagesearch.click()

    searchkey=driver.find_element_by_name("q")
    searchkey.send_keys("Photoshop" + Keys.RETURN)
    
    adobepagesearch = driver.find_element_by_xpath("//a[text()='Adobe Photoshop']")
    adobepagesearch.click()
    
    adobepagesearch = driver.find_element_by_xpath("//span[text()='Free trial']")
    adobepagesearch.click()
    
    downloadlink = driver.find_element_by_xpath("//a[@title='Download']")
    downloadlink.click()
    time.sleep(5)


      

