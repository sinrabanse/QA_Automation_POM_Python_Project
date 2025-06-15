from tests.base_test import BaseTest
from pages.product_page import ProductPage

class TestLimitTesting(BaseTest):
    def test_limit_testing(self):

        pp = ProductPage(self.driver)
        pp.get_product_page()
        pp.accept_cookies()
        pp.pushing_plus_button(20)