from selenium import webdriver
import pytest

@pytest.mark.usefixtures("initialize_driver")
class BaseTest():

    def get_driver(self):
        self.driver = webdriver.Chrome()