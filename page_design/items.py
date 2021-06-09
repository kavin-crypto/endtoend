from selenium.webdriver.common.by import By

from page_design.Checkout import Cartpage


class Items:
    cart = (By.XPATH,"//*[contains(@class,'card-footer')]/button")
    out = (By.XPATH,"//*[contains(@class,'nav-link btn btn-primary')]")

    def __init__(self, driver):
        self.driver = driver


    def cartnam(self):
        return self.driver.find_elements(*Items.cart)

    def checkout(self):
        self.driver.find_element(*Items.out).click()
        cart = Cartpage(self.driver)
        return cart
