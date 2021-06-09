from selenium.webdriver.common.by import By


class Odd:
    location = (By.XPATH, "//*[@id='country']")
    listloc = (By.XPATH, "//*[contains(@class,'suggestions')]/ul/li/a")
    tc = (By.XPATH, "//*[@type='checkbox']")
    submit = (By.XPATH, "//*[@type='submit']")
    confrim = (By.XPATH, "//*[contains(@class,'alert alert-success alert-dismissible')]/strong")

    def __init__(self, driver):
        self.driver = driver

    def delloc(self):
        return self.driver.find_element(*Odd.location)

    def getlistloc(self):
        return self.driver.find_elements(*Odd.listloc)

    def tcbox(self):
        return self.driver.find_element(*Odd.tc)

    def butsub(self):
        return self.driver.find_element(*Odd.submit)

    def orderconfrim(self):
        return self.driver.find_element(*Odd.confrim)
