from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)


    def open(self,url: str):
        self.driver.get(url)

    def find(self,locator: tuple[str,str]):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self,locator: tuple[str,str]):
        ele = self.wait.until(EC.element_to_be_clickable(locator))
        ele.click()

    def type(self,locator: tuple[str,str],text: str):
        ele = self.find(locator)
        ele.clear()
        ele.send_keys(text)

    def text_off(self,locator: tuple[str,str]) -> str:
        return self.find(locator).text.strip()

    def is_displayed(self,locator: tuple[str,str]) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception as E:
            print(E)
            return False