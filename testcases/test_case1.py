import time


import pytest

from Datas.testdata import Data
from Utilities.bassclass import BassClass
from page_design.HomePage import Dataentery


class TestFormFill(BassClass):

    def test_fill(self, textdata):

        log = self.getLogger()
        formfill = Dataentery(self.driver)
        print(self.driver.title)
        log.info("Name: "+textdata["name"])
        formfill.form_name().send_keys(textdata["name"])
        log.info("Email: " + textdata["email"])
        formfill.form_email().send_keys(textdata["email"])
        log.info("Password: " + textdata["password"])
        formfill.form_password().send_keys(textdata["password"])
        log.info("Gender: " + textdata["gender"])
        self.selecttag(formfill.form_gender(),textdata["gender"])
        log.info("DOB: " + textdata["DOB"])
        formfill.form_dob().send_keys(textdata["DOB"])
        formfill.form_submit().click()
        mission = formfill.form_conform().text
        assert "success" in mission
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
        self.driver.refresh()

@pytest.fixture(params=Data.home_pg_data)
def textdata (request):
    return request.param

