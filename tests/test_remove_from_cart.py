from pages.catalog_checkout_page import CatalogCheckoutPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest

class TestRemoveFromCart(BaseTest):
    def test_remove_from_cart(self):

        pp = ProductPage(self.driver)
        pp.get_product_page()
        pp.accept_cookies()
        pp.adding_to_cart()

        ccp = CatalogCheckoutPage(self.driver)
        ccp.remove_from_cart()