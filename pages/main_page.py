from base.base_class import Base

class MainPage(Base):
    
    url = "https://www.ivory.co.il/"

    #Methods

    def get_main_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()