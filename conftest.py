import pytest
from selenium import webdriver

@pytest.fixture()
def initialize_driver():
    driver = webdriver.Chrome