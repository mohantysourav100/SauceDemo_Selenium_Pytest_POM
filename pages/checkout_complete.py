from selenium.webdriver.common.by import By

from utils.base_utility import Base


#from SauceDemo_Selenium_Pytest_POM.utils.base_utility import Base


class CheckoutComplete(Base):
    THANK_YOU_MSG = (By.CLASS_NAME,"complete-header")
    CONFIRMATION_MSG = (By.CLASS_NAME,"complete-text")
    HOME_BUTTON = (By.ID,"back-to-products")

    def checkout_confirmation(self,msg: list[str ,str]):
        if self.is_displayed(self.THANK_YOU_MSG):
            assert msg[2] in self.text_off(self.THANK_YOU_MSG)
            print(self.text_off(self.THANK_YOU_MSG))
            if self.is_displayed(self.CONFIRMATION_MSG):
                assert msg[3] in self.text_off(self.CONFIRMATION_MSG)
                print(self.text_off(self.CONFIRMATION_MSG))

    def click_home(self):
        self.click(self.HOME_BUTTON)