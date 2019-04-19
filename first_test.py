import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time



'''Written by Bobo Isamov'''
class AdminExportTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def test_admin_export(self):
        driver = self.driver
        driver.get("https://dcechat.herokuapp.com/admin")
        element = driver.find_element_by_name("username")
        element.clear()
        element.send_keys("admin")
        element2 = driver.find_element_by_name("password")
        element2.clear()
        element2.send_keys("1instructor1")
        element.send_keys(Keys.RETURN)
        element3 = driver.find_element_by_link_text("Chat Messages")
        driver.implicitly_wait(5)
        element3.click()
        element4 = driver.find_element_by_link_text("EXPORT")
        element4.click()
        select = Select(driver.find_element_by_id('id_file_format'))
        select.select_by_index(1)
        element5 = driver.find_element_by_css_selector(".default").click()

        assert "No results found." not in driver.page_source


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()