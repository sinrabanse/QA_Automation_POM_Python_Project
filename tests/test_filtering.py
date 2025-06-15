from tests.base_test import BaseTest
from pages.main_page import MainPage

class TestFiltering(BaseTest):
    def test_filtering(self):
        mp = MainPage(self.driver)
        mp.filtering_products()