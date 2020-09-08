import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddItemtoCart(unittest.TestCase):
    base_url = "https://www.amazon.in"
    search_term = "Boat Headphones"

    def setUp(testobject):
        testobject.driver=webdriver.Chrome(executable_path="C:\Automation\Webdrivers\chromedriver.exe")
        testobject.driver.maximize_window()
        testobject.driver.implicitly_wait(10)

    def test_additemtocart(testobject):
        testobject.driver.get(testobject.base_url)
        searchtextbox=testobject.driver.find_element_by_id("twotabsearchtextbox")
        searchtextbox.clear()
        searchtextbox.send_keys(testobject.search_term)
        searchtextbox.send_keys(Keys.RETURN)
        testobject.driver.find_element_by_xpath("//span[@data-component-type='s-product-image']/a/div/img").click()
        testobject.driver.switch_to.window(testobject.driver.window_handles[1])
        testobject.driver.find_element_by_xpath("//input[@title='Add to Shopping Cart']").click()
        # to verify that sub cart page has loaded
        testobject.assertTrue(testobject.driver.find_element_by_id("hlb-subcart").is_enabled())
        testobject.assertTrue(testobject.driver.find_element_by_id("hlb-ptc-btn-native").is_displayed())

    # --- post - condition ---
    def tearDown(testobject):
        testobject.driver.quit()

if __name__ == "__main__":
    unittest.main()


    