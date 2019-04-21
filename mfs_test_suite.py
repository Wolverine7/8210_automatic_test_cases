from unittest import TestLoader, TestSuite, TextTestRunner

from Scripts.add_customers import AdminAddCustomersTest
from Scripts.add_product import AddProductTest
from Scripts.add_services import AddServiceTest
from Scripts.edit_customer import EditCustomerTest
from Scripts.edit_product import EditProductTest
from Scripts.edit_service import EditServiceTest
from Scripts.generate_customer_summary import CustomerSummaryTest
from Scripts.delete_service import ServiceDeleteTest
from Scripts.delete_product import ProductDeleteTest
from Scripts.delete_customer import CustomerDeleteTest
from Scripts.registration import RegistrationTest

if __name__ == "__main__":
    loader = TestLoader()

    suite = TestSuite((
        loader.loadTestsFromTestCase(AdminAddCustomersTest),
        loader.loadTestsFromTestCase(AddProductTest),
        loader.loadTestsFromTestCase(AddServiceTest),
        loader.loadTestsFromTestCase(EditCustomerTest),
        loader.loadTestsFromTestCase(EditServiceTest),
        loader.loadTestsFromTestCase(EditProductTest),
        loader.loadTestsFromTestCase(CustomerSummaryTest),
        loader.loadTestsFromTestCase(ServiceDeleteTest),
        loader.loadTestsFromTestCase(ProductDeleteTest),
        loader.loadTestsFromTestCase(CustomerDeleteTest),
        loader.loadTestsFromTestCase(RegistrationTest),
    ))

runner = TextTestRunner(verbosity=2)
runner.run(suite)