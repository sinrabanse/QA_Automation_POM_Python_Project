import requests

from base.base_class import Base
from data.urls import TestUrls
from data.test_data import TestData
from utilities.decorators import log_step

class CatalogCheckoutPage(Base):

    url = TestUrls.catalog_checkout_url

    # Locators
    first_continue_button = "//a[@id='PopupShipping-btnJs_id']"
    choose_shop_dropdown = "//span[@id='select2-selectCity_pic-container']"
    shop_search_field =  "//input[@type='search' and contains(@aria-label, 'בחר סניף')]"
    choose_holon_shop = "//li[contains(text(), 'חולון') and @role='treeitem']"
    second_continue_button = "(//button[@type='button' and contains(@data-no-suboption-msg, 'יש לבחור את הסניף שממנו נרצה לאסוף את ההזמנה')])[1]"
    fast_buy_full_name_field = "//input[@data-save-address-fld='fname']"
    fast_buy_email_field = "//input[@data-save-address-fld='email']"
    fast_buy_phone_field = "//input[@data-save-address-fld='phone']"
    fast_buy_city_field = "//input[@data-save-address-fld='city']"
    fast_buy_street_name_field = "//input[@data-save-address-fld='street_name']"
    fast_buy_home_number_field = "//input[@data-save-address-fld='street_number']"
    remove_from_cart_button = "//a[@class='btn-remove-item-cart linkInited']"
    empty_cart_locator = "//div[@class='col-12 title']"


    # Getters
    def get_first_continue_button(self):
        return self._get_element_by_xpath(self.first_continue_button)
    
    def get_choose_shop_dropdown(self):
        return self._get_element_by_xpath(self.choose_shop_dropdown)
    
    def get_shop_search_field(self):
        return self._get_element_by_xpath(self.shop_search_field)
    
    def get_choose_holon_shop(self):
        return self._get_element_by_xpath(self.choose_holon_shop)
    
    def get_second_continue_button(self):
        return self._get_element_by_xpath(self.second_continue_button)
    
    def get_fast_buy_full_name_field(self):
        return self._get_element_by_xpath(self.fast_buy_full_name_field)
    
    def get_fast_buy_email_field(self):
        return self._get_element_by_xpath(self.fast_buy_email_field)
    
    def get_fast_buy_phone_field(self):
        return self._get_element_by_xpath(self.fast_buy_phone_field)
    
    def get_fast_buy_city_field(self):
        return self._get_element_by_xpath(self.fast_buy_city_field)
    
    def get_fast_buy_street_name_field(self):
        return self._get_element_by_xpath(self.fast_buy_street_name_field)
    
    def get_fast_buy_home_number_field(self):
        return self._get_element_by_xpath(self.fast_buy_home_number_field)
    
    def get_remove_from_cart_button(self):
        return self._get_element_by_xpath(self.remove_from_cart_button)
    
    def get_empty_cart_locator(self):
        return self._get_element_by_xpath(self.empty_cart_locator)
    
    # Actions
    def click_first_continue_button(self):
        self.get_first_continue_button().click()
        print("Click first continue button")

    def click_choose_shop_dropdown(self):
        self.get_choose_shop_dropdown().click()
        print("Click choose shop dropdown")

    def click_choose_holon_shop(self):
        self.get_choose_holon_shop().click()
        print("Click choose Holon shop")

    def click_second_continue_button(self):
        self.get_second_continue_button().click()
        print("Click second continue button")

    def click_remove_from_cart_button(self):
        self.get_remove_from_cart_button().click()
        print("Click remove from cart button")

    def submit_order_mock(self, data=None):
        if data is None:
            data = {
                "full_name": TestData.test_full_name,
                "email": TestData.test_email,
                "phone": TestData.test_phone,
                "city": TestData.test_city,
                "street": TestData.test_street,
                "home_number": TestData.test_home_number
            }
        response = requests.post("http://localhost:5001/submit-order", json=data)
        assert response.status_code == 200
        result = response.json()
        assert result.get("status") == "success", f"Wrong response: {result}"
        print(f"Order is done: {result}")
        return result

    # Methods

    @log_step()
    def choose_self_pickup(self):
        self.assert_url(self.url)
        self.click_first_continue_button()
        self.click_choose_shop_dropdown()
        self.get_shop_search_field().send_keys("חולון")
        self.click_choose_holon_shop()
        self.click_second_continue_button()
        self.assert_url(TestUrls.personal_info_url)

    @log_step()
    def fill_customer_info(self):
        self.get_fast_buy_full_name_field().send_keys(TestData.test_full_name)
        self.get_fast_buy_email_field().send_keys(TestData.test_email)
        self.get_fast_buy_phone_field().send_keys(TestData.test_phone)
        self.get_fast_buy_city_field().send_keys(TestData.test_city)
        self.get_fast_buy_street_name_field().send_keys(TestData.test_street)
        self.get_fast_buy_home_number_field().send_keys(TestData.test_home_number)
        self.submit_order_mock()

    @log_step()
    def remove_from_cart(self):
        self.assert_url(self.url)
        self.click_remove_from_cart_button()
        self.assert_phrase(self.get_empty_cart_locator(), TestData.empty_cart_text)


