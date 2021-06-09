from selenium.webdriver.common.by import By

from page_design.Purchase import Odd


class Cartpage:

    conformation = (By.XPATH,"//*[contains(@class,'media-body')]/h4/a")
    button = (By.XPATH,"//*[contains(@class,'btn btn-success')]")

    def __init__(self, driver):
        self.driver = driver

    def getconf(self):
        return self.driver.find_element(*Cartpage.conformation)

    def cartbutton(self):
        self.driver.find_element(*Cartpage.button).click()
        order = Odd(self.driver)
        return order