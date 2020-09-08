import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expcon
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

'''Fixtures allow parameters to be passed as a dictionary'''


# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init_driver(request):
#     '''request var allows parameters to be accessed'''
#     if request.param == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--start-maximized")
#         driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
#
#     if request.param == 'firefox':
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#         driver.maximize_window()
#
#     '''Now,the driver should be made available at the class level'''
#     wait = WebDriverWait(driver, 10)
#     request.cls.driver = driver
#     request.cls.wait = wait
#
#
#     yield
#     driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

'''Class name should start with Caps'''
class Test_childclass(BaseTest):

    def test_google_title(self):
        self.driver.get('https://www.google.com/')
        print(self.driver.title)
        assert self.driver.title == 'Google'



    def test_ubisoft_site(self):
        def custom_select_action(dropdownlist, value):
            print('----------Inside custom select method----------')
            print(len(dropdownlist))

            for el in dropdownlist:
                print(el.text)
                if el.text == value:
                    el.click()
                    break

        def element_border(element):
            '''Create a border for an element using JS'''
            self.driver.execute_script("arguments[0].style.border = '3px solid red'", element)

        self.driver.get('https://www.ubisoft.com/en-us/')
        title = self.driver.execute_script("return document.title;")
        print(title)

        watchbutton = self.wait.until(expcon.presence_of_element_located((By.XPATH, '//span[text()="WATCH TRAILER"]')))
        element_border(watchbutton)
        # driver.execute_script("arguments[0].style.border = '3px solid red'", watchbutton)
        self.driver.execute_script("arguments[0].click();", watchbutton)

        monthdropdown = self.wait.until(
            expcon.presence_of_all_elements_located((By.XPATH, '//select[@name="selectedMonth"]/option')))
        # = driver.find_element(By.XPATH, '//select[@name="selectedMonth"]/option')
        daydropdown = self.driver.find_elements(By.XPATH, '//select[@name="selectedDay"]/option')
        yeardropdown = self.driver.find_elements(By.XPATH, '//select[@name="selectedYear"]/option')

        custom_select_action(monthdropdown, 'MARCH')
        custom_select_action(daydropdown, '6')
        custom_select_action(yeardropdown, '1994')

        submitbutton = self.driver.find_element(By.XPATH, '//span[text()="Submit"]')
        self.driver.execute_script("arguments[0].click();", submitbutton)
        self.driver.find_element(By.XPATH, '//button[@class="modal__header__closeBtn"]').click()

        '''JS SCROLL TO THE BOTTOM OF THE PAGE - 0 to scroll height. Scroll height to 0 for scrolling from bottom to top'''
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        '''JS SCROLL INTO VIEW SCRIPT'''
        element_to_be_scrolled_to = self.driver.find_element(By.XPATH, '//span[text()="Join Now"]/..')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_to_be_scrolled_to)

