import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

'''Fixtures allow parameters to be passed as a dictionary'''

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    '''request var allows parameters to be accessed'''
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    if request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()

    '''Now,the driver should be made available at the class level'''
    wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.close()