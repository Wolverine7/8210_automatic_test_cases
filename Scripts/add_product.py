import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time



'''Written by Bobo Isamov'''
class AddProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def test_admin_export(self):
        driver = self.driver
        driver.get("https://bobo-food-service.herokuapp.com/")
        login_link = driver.find_element_by_link_text("Login").click()
        username = driver.find_element_by_name("username")
        username.clear()
        username.send_keys("bobo")
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys("Simcards1.")
        submit_buttom = driver.find_element_by_xpath("//input[@type='submit']").click()
        product_link = driver.find_element_by_link_text("Products").click()
        add_product_button = driver.find_element_by_link_text("Add Product").click()
        customer_select = Select(driver.find_element_by_id('id_cust_name'))
        customer_select.select_by_index(2)
        product_category = driver.find_element_by_name("product")
        product_category.clear()
        product_category.send_keys("Steak")
        description = driver.find_element_by_name('p_description')
        description.clear()
        description.send_keys("Medium Fried")
        quantity = driver.find_element_by_name("quantity")
        quantity.clear()
        quantity.send_keys("2")
        product_charge = driver.find_element_by_name("charge")
        product_charge.clear()
        product_charge.send_keys("150")
        #submit_buttom = driver.find_element_by_css_selector("button")
        product_charge.send_keys(Keys.RETURN)

        assert "No results found." not in driver.page_source


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()