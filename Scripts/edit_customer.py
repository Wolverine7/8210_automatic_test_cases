import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time



'''Written by Bobo Isamov'''
class EditCustomerTest(unittest.TestCase):

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
        product_link = driver.find_element_by_link_text("Customers").click()
        edit_buttom = driver.find_element_by_css_selector('.btn.btn-warning').click()

        '''Add the Data to the cells'''
        customer_cell = driver.find_element_by_name("cust_name")
        customer_cell.clear()
        customer_cell.send_keys("Bobodzhon Isamov")

        organization_cell = driver.find_element_by_name("organization")
        organization_cell.clear()
        organization_cell.send_keys("UNO")

        role_cell = driver.find_element_by_name("role")
        role_cell.clear()
        role_cell.send_keys("Student")

        email_cell = driver.find_element_by_name("email")
        email_cell.clear()
        email_cell.send_keys("bisamov@unomaha.edu")

        bldgroom_cell = driver.find_element_by_name("bldgroom")
        bldgroom_cell.clear()
        bldgroom_cell.send_keys("Pki Room 270")

        address_cell = driver.find_element_by_name("address")
        address_cell.clear()
        address_cell.send_keys("72nd Dodge Street")

        account_number_cell = driver.find_element_by_name("account_number")
        account_number_cell.clear()
        account_number_cell.send_keys("5738")

        city_cell = driver.find_element_by_name("city")
        city_cell.clear()
        city_cell.send_keys("Omaha")

        state_cell = driver.find_element_by_name("state")
        state_cell.clear()
        state_cell.send_keys("NE")

        zipcode_cell = driver.find_element_by_name("zipcode")
        zipcode_cell.clear()
        zipcode_cell.send_keys("68116")

        phone_number_cell = driver.find_element_by_name("phone_number")
        phone_number_cell.clear()
        phone_number_cell.send_keys("4023062555")

        update_buttom = driver.find_element_by_css_selector('.save.btn.btn-default').click()
        assert "No results found." not in driver.page_source


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()