
from pages.catalog_checkout_page import CatalogCheckoutPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestChooseSelfPickup(BaseTest):
    def test_choose_self_pickup(self):

        pp = ProductPage(self.driver)
        pp.get_product_page()
        pp.accept_cookies()
        pp.adding_to_cart()

        ccp = CatalogCheckoutPage(self.driver)
        ccp.choose_self_pickup()