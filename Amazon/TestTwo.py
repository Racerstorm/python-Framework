import unittest
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

class AmazonSearch(unittest.TestCase):
    base_url="https://www.amazon.in"
    search_term="Boat Headphones"

    def setUp(testobject):
        #Declare and initialize web driver
        testobject.driver=webdriver.Chrome(executable_path="C:\Automation\Webdrivers\chromedriver.exe")
        testobject.driver.maximize_window()
        testobject.driver.implicitly_wait(10)

    def testhomepage(testobject):
        testobject.driver.get(testobject.base_url)
        testobject.assertIn("Amazon",testobject.driver.title)
        searchboxtext=testobject.driver.find_element_by_id("twotabsearchtextbox")
        searchboxtext.clear()
        searchboxtext.send_keys(testobject.search_term)
        searchboxtext.send_keys(Keys.RETURN)
        testobject.assertIn(testobject.search_term,testobject.driver.title)
        testobject.assertNotIn("No results found.",testobject.driver.page_source)

    def tearDown(testobject):
        testobject.driver.close()

if __name__ == "__main__":
    unittest.main()


