from base.base_class import Base
from data.urls import TestUrls
from utilities.decorators import log_step

class MainPage(Base):

    # Locators

    search_panel = "//input[@id='qSearch']"
    search_button = "//button[@id='searchButton']"
    search_result_title = "//h1[@id='main-cats-lbm ']"
    checkbox_filter_phones = "//div[contains(@class, 'col-md-auto col-12 pr-2 pl-2 sinunLabelnewLabel d-flex')]//span[contains(@id, \
        'sinunTitle_2735') and contains(text(), 'טלפונים סלולרים וסמארטפונים')]"
    apply_filter_button = "//button[@class=' btn btn_filters hoverBtn filter-by-cats-btn']"
    iPhone16BlueCart = "//div[@class='col-md-12 col-12 title_product_catalog mb-md-1 main-text-area' \
        and contains(text(), 'אייפון Apple iPhone 16 128GB בצבע כחול')]"
    apply_filter_button = "//button[@class=' btn btn_filters hoverBtn filter-by-cats-btn']"

    # Getters

    def get_search_panel(self):
        return self._get_element_by_xpath(self.search_panel)

    def get_search_button(self):
        return self._get_element_by_xpath(self.search_button)

    def get_search_result_title(self):
        return self._get_element_by_xpath(self.search_result_title)
    
    def get_checkbox_filter_phones(self):
        return self._get_element_by_xpath(self.checkbox_filter_phones)
    
    def get_checkbox_filter_button(self):
        return self._get_element_by_xpath(self.apply_filter_button)
    
    def get_iphone_16_blue_cart(self):
        return self._get_element_by_xpath(self.iPhone16BlueCart)
    
    def get_apply_filter_button(self):
        return self._get_element_by_xpath(self.apply_filter_button)

    # Actions

    def click_search_button(self):
        self.get_search_button().click()
        print("Click search button")

    def click_checkbox_filter_phones(self):
        self.get_checkbox_filter_phones().click()
        print("Click checkbox filter phones")

    def click_checkbox_filter_button(self):
        self.get_checkbox_filter_button().click()
        print("Click checkbox filter button")

    def click_iphone_16_blue_cart(self):
        self.get_iphone_16_blue_cart().click()
        print("Click iPhone 16 Blue Cart")

    def click_apply_filter_button(self):
        self.get_apply_filter_button().click()
        print("Click apply filter button")

    # Methods
    @log_step()
    def going_to_product_card(self):
        self.driver.get(TestUrls.main_page_url)
        self.driver.maximize_window()
        self.get_current_url() 
        self.assert_url(TestUrls.main_page_url)
        self.accept_cookies()
        self.get_search_panel().clear()
        self.get_search_panel().send_keys("iPhone 16")
        self.click_search_button()
        self.assert_word(self.get_search_result_title(), "תוצאות חיפוש לiPhone 16")
        self.click_checkbox_filter_phones()
        self.click_checkbox_filter_button()
        self.click_iphone_16_blue_cart()

    @log_step()
    def filtering_products(self):
        self.driver.get(TestUrls.main_page_url)
        self.driver.maximize_window()
        self.get_current_url() 
        self.assert_url(TestUrls.main_page_url)
        self.accept_cookies()
        self.get_search_panel().clear()
        self.get_search_panel().send_keys("iPhone 16")
        self.click_search_button()
        self.assert_url(TestUrls.search_iphone_16_url)
        self.click_checkbox_filter_phones()
        self.click_apply_filter_button()
        self.assert_url(TestUrls.filtered_iphone_16_url)