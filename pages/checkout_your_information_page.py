from selenium.webdriver.common.by import By
from pages.checkout_overview_page import CheckoutOverview
from utils.base_utility import Base


#from utils.base_utility import Base


class YourInformation(Base):
    FIRST_NAME = (By.ID,"first-name")
    LAST_NAME = (By.ID,"last-name")
    ZIP_CODE = (By.ID,"postal-code")
    CONTINUE_BUTTON = (By.ID,"continue")

    def fill_yourDetails(self,fname,lname,zipcode):
        self.type(self.FIRST_NAME,fname)
        self.type(self.LAST_NAME,lname)
        self.type(self.ZIP_CODE,zipcode)

    def click_Continue(self):
        self.click(self.CONTINUE_BUTTON)
        overview = CheckoutOverview(self.driver)
        return overview