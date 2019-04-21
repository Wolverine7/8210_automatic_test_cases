import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time



'''Written by Bobo Isamov'''
class AddServiceTest(unittest.TestCase):

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
        service_link = driver.find_element_by_link_text("Services").click()
        add_service_button = driver.find_element_by_link_text("Add Service").click()
        customer_select = Select(driver.find_element_by_id('id_cust_name'))
        customer_select.select_by_index(2)
        service_category = driver.find_element_by_name("service_category")
        service_category.clear()
        service_category.send_keys("Food Prep/Delivery")
        description = driver.find_element_by_name('description')
        description.clear()
        description.send_keys("A customer ordered a delivery order to be served for her")
        location = driver.find_element_by_name("location")
        location.clear()
        location.send_keys("Omaha NE")
        service_charge = driver.find_element_by_name("service_charge")
        service_charge.clear()
        service_charge.send_keys("150")
        save_buttom = driver.find_element_by_css_selector('.save.btn.btn-default').click()
        assert "No results found." not in driver.page_source


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()