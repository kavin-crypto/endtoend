import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Datas.testdata import Data
from Utilities.bassclass import BassClass
from page_design.HomePage import Dataentery


class TestShopSite(BassClass):

    def test_mobile(self,textdata):
        log = self.getLogger()
        esite = Dataentery(self.driver)
        brandselt = esite.shop_button()
        phon = brandselt.cartnam()
        log.info("Card title :"+textdata["mobilebrand"])
        for mob in phon:
            if mob.find_element_by_xpath("parent::div/parent::div/div[1]//a").text == textdata["mobilebrand"]:
                mob.click()

        cart = brandselt.checkout()
        assert textdata["mobilebrand"] == cart.getconf().text
        order = cart.cartbutton()
        order.delloc().send_keys("in")
        self.wait("//*[contains(@class,'suggestions')]/ul/li/a")
        sug = order.getlistloc()
        log.info("Country Selected :"+textdata["country"])
        for sugg in sug:
            if sugg.text == textdata["country"]:
                sugg.click()
                break

        assert not order.tcbox().is_selected()
        order.butsub().click()
        log.info("Text received from application is " + order.orderconfrim().text)
        assert "Success!" == order.orderconfrim().text
        self.driver.refresh()


@pytest.fixture(params=Data.shop_page)
def textdata (request):
    return request.param