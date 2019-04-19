import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import csv



'''Written by Bobo Isamov'''
class AdminAddCustomersTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def test_admin_export(self):
        '''Sign in and navigate to Customer table'''
        driver = self.driver
        driver.get("https://bobo-food-service.herokuapp.com/admin")
        element = driver.find_element_by_name("username")
        element.clear()
        element.send_keys("bobo")
        element2 = driver.find_element_by_name("password")
        element2.clear()
        element2.send_keys("Simcards1.")
        element.send_keys(Keys.RETURN)
        element3 = driver.find_element_by_link_text("Customers").click()

        '''Read CSV File'''
        with open('Customers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                customer = line[0]
                organization = line[1]
                role = line[2]
                email = line[3]
                bldgroom = line[4]
                address = line[5]
                account_number = line[6]
                city = line[7]
                state = line[8]
                zipcode = line[9]
                phone_number = line[10]

                print(customer)

                element4 = driver.find_element_by_link_text("ADD CUSTOMER")
                element4.click()

                '''Add the Data to the cells'''
                customer_cell = driver.find_element_by_name("cust_name")
                customer_cell.send_keys("", customer)

                organization_cell = driver.find_element_by_name("organization")
                organization_cell.send_keys("", organization)

                role_cell = driver.find_element_by_name("role")
                role_cell.send_keys("", role)

                email_cell = driver.find_element_by_name("email")
                email_cell.send_keys("", email)

                bldgroom_cell = driver.find_element_by_name("bldgroom")
                bldgroom_cell.send_keys("", bldgroom)

                address_cell = driver.find_element_by_name("address")
                address_cell.send_keys("", address)

                account_number_cell = driver.find_element_by_name("account_number")
                account_number_cell.send_keys("", account_number)

                city_cell = driver.find_element_by_name("city")
                city_cell.send_keys("", city)

                state_cell = driver.find_element_by_name("state")
                state_cell.send_keys("", state)

                zipcode_cell = driver.find_element_by_name("zipcode")
                zipcode_cell.send_keys("", zipcode)

                phone_number_cell = driver.find_element_by_name("phone_number")
                phone_number_cell.send_keys("", phone_number)

                save_button = driver.find_element_by_css_selector(".default").click()


                assert "No results found." not in driver.page_source


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()