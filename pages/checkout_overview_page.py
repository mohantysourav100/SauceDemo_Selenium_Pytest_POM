from functools import reduce

from selenium.webdriver.common.by import By

from utils.base_utility import Base
from utils.regular_utility import Regular


class CheckoutOverview(Base,Regular):
    PRICE_ALL_ITEMS = (By.CLASS_NAME,"inventory_item_price")
    PAYMENT_INFO = (By.CSS_SELECTOR,"div[data-test = 'payment-info-value']")
    SHIPPING_INFO = (By.CSS_SELECTOR,"[data-test = 'shipping-info-value']")
    ITEM_TOTAL_PRICE = (By.CLASS_NAME,"summary_subtotal_label")
    TAX_AMOUNT = (By.XPATH,"//div[@data-test = 'tax-label']")
    FINAL_AMOUNT = (By.XPATH,"//div[@data-test = 'total-label']")
    FINISH_BUTTON = (By.ID,"finish")
    item_prices = []

    def item_totalAmount_validation(self):
        actual_final_amount = 0
        prices = self.driver.find_elements(*self.PRICE_ALL_ITEMS)
        if len(self.item_prices) == 0:
            for price in prices:
                self.item_prices.append(self.text_spliting(price.text))
        item_actual_price = list(map(float,self.item_prices))
        total_price  = reduce(lambda x,y : x + y, item_actual_price)
        if self.is_displayed(self.ITEM_TOTAL_PRICE):
            expected_price = float(self.text_spliting(self.text_off(self.ITEM_TOTAL_PRICE)))
            assert total_price == expected_price
            print(f"TOTAL PRICE : {total_price} same as DISPLAYED PRICE : {expected_price}")
        if self.is_displayed(self.TAX_AMOUNT):
            actual_tax = float(self.text_spliting(self.text_off(self.TAX_AMOUNT)))
            actual_final_amount = total_price + actual_tax
        if self.is_displayed(self.FINAL_AMOUNT):
            expected_final_amount = float(self.text_spliting(self.text_off(self.FINAL_AMOUNT)))
            assert actual_final_amount == expected_final_amount
            print(f"TOTAL AMOUNT : {actual_final_amount} same as DISPLAYED AMOUNT : {expected_final_amount} including tax")

    def payment_shippingInfo_validation(self,msg_text: list[str,str]):
        if self.find(self.PAYMENT_INFO).text.strip():
            assert msg_text[0] in self.find(self.PAYMENT_INFO).text.strip()
        if self.find(self.SHIPPING_INFO).text.strip():
            assert msg_text[1] in self.find(self.SHIPPING_INFO).text.strip()

    def click_finish(self):
        self.click(self.FINISH_BUTTON)



