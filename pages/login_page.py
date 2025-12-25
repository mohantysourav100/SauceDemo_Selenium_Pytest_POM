from selenium.webdriver.common.by import By
from pages.products_cart_page import ProductCart
from utils.base_utility import Base

class Login(Base):
    USERNAME = (By.ID,"user-name")
    PASSWORD = (By.ID,"password")
    LOGIN_BTN = (By.ID,"login-button")

    def site_load(self,url):
        self.open(url)

    def login(self,username: str,password: str):
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)
        products = ProductCart(self.driver)
        return products