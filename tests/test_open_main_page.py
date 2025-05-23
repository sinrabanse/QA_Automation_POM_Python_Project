from pages.main_page import MainPage
from tests.base_test import BaseTest



class Test1(BaseTest):

    def test_open_main_page(self):
        self.get_driver()
        mp = MainPage(self.driver)
        mp.get_main_url()