import unittest
import HtmlTestRunner
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ViewProductDetails(unittest.TestCase):
    # Declare variable to store URL
    base_url = "https://www.amazon.in"
    # Declare variable to store search keyword
    search_term = "Boat Headphones"
    page_title_tc01 = "Your Account"

    def setUp(testobject):
        # Declare and initialize webdriver
        testobject.driver=webdriver.Chrome(executable_path="C:\Automation\Webdrivers\chromedriver.exe")
        testobject.driver.maximize_window()
        testobject.driver.implicitly_wait(10)

    def test_Amazon_TC_001_NavigatetoAccountPage(testobject):
        """Navigate to My Accounts page"""
        testobject.driver.get(testobject.base_url)
        testobject.driver.find_element_by_id("nav-hamburger-menu").click()
        testobject.driver.find_element_by_xpath("//a[@class='hmenu-item'][text()='Your Account']").click()
        testobject.assertIn(testobject.page_title_tc01,testobject.driver.title)
        

    def test_Amazon_TC_003_Additemtocart(testobject):
        """Search for a product from the search bar and add it to the cart"""
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
        testobject.driver.find_element_by_id("hlb-ptc-btn-native").click()
        testobject.assertTrue(testobject.driver.title.startswith("Amazon Sign In"))
        testobject.assertTrue(testobject.driver.find_element_by_id('ap_email').is_displayed())   

    def test_Amazon_TC_002_DeleteItemfromCart(testobject):
        """Delete item(s) from cart"""
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
        testobject.driver.find_element_by_xpath("//a[@class='nav-logo-link']").click()

        cartcount=int(testobject.driver.find_element_by_id("nav-cart-count").text)
        if(cartcount<1):
            print("Cart is empty. Exiting the test")
            exit()

        testobject.driver.find_element_by_id("nav-cart").click()
        if(testobject.driver.title.startswith("Amazon.in Shopping Cart")):
            testobject.driver.find_element_by_xpath("//span[@class='a-size-small sc-action-delete']/span/input").click()
            time.sleep(2)
        testobject.assertTrue(int(testobject.driver.find_element_by_id("nav-cart-count").text) < cartcount)



    # --- post - condition ---
    def tearDown(testobject):
        testobject.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Automation\pythonFramework\Reports'))


    