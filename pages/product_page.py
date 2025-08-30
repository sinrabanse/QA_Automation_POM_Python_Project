from selenium.webdriver.common.action_chains import ActionChains
import time

from base.base_class import Base
from data.test_data import TestData
from data.urls import TestUrls
from utilities.decorators import log_step

class ProductPage(Base):

    # Locators
    product_card_title = "//h1[@id='titleProd']"
    buy_now_button = "(//button[@id='fastBuy'])[2]"
    close_recommendation_button = "//button[@id='buy_get_close']"
    add_to_cart_button = "(//button[@id='addToCart'])[2]"
    go_to_cart_button = "(//a[@class='cart-btn cart-target linkInited'])[1]"
    add_amount_product_button = "//button[@id='plusAmount']"
    error_amount_product_field = "//div[@id='amountErrorMsg']"

    # Getters
        
    def get_product_title(self):
        return self._get_element_by_xpath(self.product_card_title)
    
    def get_buy_now_button(self):
        return self._get_element_by_xpath(self.buy_now_button)
    
    def get_close_recommendation_button(self):
        return self._get_element_by_xpath(self.close_recommendation_button)
    
    def get_add_to_cart_button(self):
        return self._get_element_by_xpath(self.add_to_cart_button)
    
    def get_go_to_cart_button(self):
        return self._get_element_by_xpath(self.go_to_cart_button)
    
    def get_add_amount_product_button(self):
        return self._get_element_by_xpath(self.add_amount_product_button)

    def get_error_amount_product_field(self):
        return self._get_element_by_xpath(self.error_amount_product_field)
    
    # Actions
    def click_buy_now_button(self):
        ActionChains(self.driver).move_to_element(self.get_buy_now_button()).click().perform()
        print("Click buy now button")

    def click_add_to_cart_button(self):
        ActionChains(self.driver).move_to_element(self.get_add_to_cart_button()).click().perform()
        print("Click add to cart button")

    def click_close_recommendation_button(self):
        self.get_close_recommendation_button().click()
        print("Click close recommendation button")
    
    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click() 
        print("Click go to cart button")

    def click_add_amount_product_button(self, count):
        self.get_add_amount_product_button().click()
        print(f"CLick add amount product button {count+1}")

    # Methods
    @log_step()
    def fast_order(self):
        self.assert_phrase(self.get_product_title(), "iPhone 16")
        self.assert_url(TestUrls.iphone_16_black_url)
        self.click_buy_now_button()
        self.click_close_recommendation_button()

    @log_step()
    def get_product_page(self):
        self.driver.get(TestUrls.iphone_16_black_url)
        self.driver.maximize_window()
        self.get_current_url() 
        self.assert_url(TestUrls.iphone_16_black_url)

    @log_step()
    def adding_to_cart(self):
        self.click_add_to_cart_button()
        self.click_close_recommendation_button()
        time.sleep(1) #waiting animations
        self.click_go_to_cart_button()
        self.assert_url(TestUrls.catalog_checkout_url)

    @log_step()
    def pushing_plus_button(self, count):
        for j in range(0, count):
            self.click_add_amount_product_button(j)
        self.assert_phrase(self.get_error_amount_product_field(), TestData.error_amount_product_text)