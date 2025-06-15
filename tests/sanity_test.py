from pages.main_page import MainPage
from tests.base_test import BaseTest
from pages.product_page import ProductPage
from pages.catalog_checkout_page import CatalogCheckoutPage
import pytest


@pytest.mark.sanity
@pytest.mark.usefixtures("mock_server")
class TestSanity(BaseTest):

    def test_sanity_test(self):
        mp = MainPage(self.driver)
        mp.going_to_product_card()


        pp = ProductPage(self.driver)
        pp.fast_order()

        ccp = CatalogCheckoutPage(self.driver)
        ccp.choose_self_pickup()
        ccp.fill_customer_info()