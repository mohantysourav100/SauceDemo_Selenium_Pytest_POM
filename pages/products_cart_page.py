from utils.base_utility import Base
from selenium.webdriver.common.by import By


class ProductCart(Base):
    CART_ITEMS = (By.XPATH,"//div[@class = 'inventory_item']")
    PRODUCT_NAME =(By.XPATH,"div[@class='inventory_item_description']/div/a/div")
    ADD_TO_CART = (By.XPATH,"div[@class='inventory_item_description']/div/button")
    CART_BUTTON = (By.CLASS_NAME,"shopping_cart_link")
    CART_ITEM_COUNTS = (By.XPATH,"//span[@data-test = 'shopping-cart-badge']")
    added_count = 0


    def add_product_toCart(self,product: list):
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        for item in cart_items:
            for prod in product:
                if item.find_element(*self.PRODUCT_NAME).text.strip() == prod:
                    item.find_element(*self.ADD_TO_CART).click()
                    self.added_count += 1

    def product_count_validation(self):
        expected_count = self.added_count
        actual_count = self.text_off(self.CART_ITEM_COUNTS)
        if expected_count != 0:
            assert expected_count == int(actual_count)
            print(f"Numbers items displayed {actual_count} in Cart screen is same as number of items added {expected_count} to the cart")

    def navigate_toCart(self):
        self.click(self.CART_BUTTON)
        from pages.your_cart_page import YourCart
        your_cart = YourCart(self.driver)
        return your_cart