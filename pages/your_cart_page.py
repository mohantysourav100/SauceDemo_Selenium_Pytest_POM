from selenium.webdriver.common.by import By
from pages.checkout_your_information_page import YourInformation
from utils.base_utility import Base


class YourCart(Base):
    cart_item_names = []
    CHECKOUT_BUTTON = (By.ID,"checkout")
    CART_ITEMS_NAMES =(By.CLASS_NAME,"inventory_item_name")

    def cart_item_validation(self,product: list):
        elements = self.driver.find_elements(*self.CART_ITEMS_NAMES)
        if len(self.cart_item_names)== 0:
            for ele in elements:
                self.cart_item_names.append(ele.text.strip())
            assert self.cart_item_names == product
            print("Displayed items in Cart is same as items added in the cart")

    def cart_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        your_info = YourInformation(self.driver)
        return your_info