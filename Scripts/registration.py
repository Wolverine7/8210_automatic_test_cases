import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time



'''Written by Bobo Isamov'''
class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def test_admin_export(self):
        driver = self.driver
        driver.get("https://bobo-food-service.herokuapp.com/")
        registration_link = driver.find_element_by_link_text("Register").click()
        username = driver.find_element_by_name("username")
        username.clear()
        username.send_keys("test")
        password = driver.find_element_by_name("password1")
        password.clear()
        password.send_keys("test12345")
        password_confirm = driver.find_element_by_name("password2")
        password_confirm.clear()
        password_confirm.send_keys("test12345")
        register_buttom = driver.find_element_by_xpath("//input[@type='submit']").click()


        assert "No results found." not in driver.page_source


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()