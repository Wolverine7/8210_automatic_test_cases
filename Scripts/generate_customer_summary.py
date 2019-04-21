import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


'''Written by Bobo Isamov'''
class CustomerSummaryTest(unittest.TestCase):

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
        customer_link = driver.find_element_by_link_text("Customers").click()
        summary_buttom = driver.find_element_by_css_selector('.btn.btn-primary').click()

        assert "No results found." not in driver.page_source


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()