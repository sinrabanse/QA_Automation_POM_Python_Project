from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method to get current URL

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

    #Method to assert words

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"Good value word {value_word} = {result}")

    #Method to assert several words

    def assert_phrase(self, word, result):
        value_word = word.text
        assert result in value_word
        print(f"Good value word {result} in {value_word}")

    #Method assert URL

    def assert_url(self, result, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(result))
            print(f"Good value URL: {result}")
        except Exception:
            current = self.driver.current_url
            raise AssertionError(f"Expected URL to be '{result}', but got '{current}'")
        
    #Method to accept cookies

    def accept_cookies(self, timeout=5):
        try:
            agree_button = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='approvedCookie()']")))
            agree_button.click()
            print("Cookies accepted")
        except Exception as e:
            print("No cookies banner appeared or already accepted.")

    #Method to get locators

    def _get_element_by_xpath(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))