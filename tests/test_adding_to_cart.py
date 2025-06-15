from tests.base_test import BaseTest
from pages.product_page import ProductPage

class TestAddingToCart(BaseTest):
    def test_adding_to_cart(self):

        pp = ProductPage(self.driver)
        pp.get_product_page()
        pp.accept_cookies()
        pp.adding_to_cart()