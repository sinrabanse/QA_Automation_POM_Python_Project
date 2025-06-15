from selenium import webdriver
import pytest

@pytest.mark.usefixtures("initialize_driver")
class BaseTest():
    pass