from selenium.webdriver.common.by import By

from page_design.items import Items


class Dataentery:

    formname = (By.XPATH, "//*[contains(text(),'Name')]/parent :: div/input")
    email = (By.XPATH, "//*[@name='email']")
    password = (By.XPATH, "//*[@placeholder='Password']")
    dob = (By.XPATH, "//*[@name='bday']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit = (By.XPATH, "//input[@type='submit']")
    conformation = (By.XPATH,"//*[contains(@class,'alert-success')]")
    button = (By.XPATH,"//*[contains(text(),'Shop')]")

    def __init__(self, driver):
        self.driver = driver


    def form_name(self):
        return self.driver.find_element(*Dataentery.formname)

    def form_email(self):
        return self.driver.find_element(*Dataentery.email)

    def form_password(self):
        return self.driver.find_element(*Dataentery.password)

    def form_dob(self):
        return self.driver.find_element(*Dataentery.dob)

    def form_gender(self):
        return self.driver.find_element(*Dataentery.gender)

    def form_submit(self):
        return self.driver.find_element(*Dataentery.submit)

    def form_conform(self):
        return self.driver.find_element(*Dataentery.conformation)

    def shop_button(self):
        self.driver.find_element(*Dataentery.button).click()
        brandselt = Items(self.driver)
        return brandselt
