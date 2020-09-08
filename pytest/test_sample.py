from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


driver = None
def test_setup():
    global driver
    #   driver = webdriver.Chrome(executable_path="C:\Automation\Webdrivers\chromedriver.exe")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_run():
    driver = webdriver.Chrome(executable_path="C:\Automation\Webdrivers\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.google.com")
    assert driver.title=="Google"

    
def test_run2():
    
    #driver = webdriver.Chrome(executable_path="C:\Automation\Webdrivers\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.adobe.com")
    assert driver.title=="Adobe: Creative, marketing and document management solutions"

    
