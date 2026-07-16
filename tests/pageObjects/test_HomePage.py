import pytest
from selenium.webdriver.support.ui import Select

from tests.data import sdata
from tests.pageObjects.homepage import HomePage
from tests.pageObjects.Baseclass import BaseClass


class TestHomePage(BaseClass):
    def test_formsubmission(self,more):
        log =self.getLogger()
        homepage = HomePage(self.driver)
        homepage.shopItems().send_keys(more[0])
        log.info("getting name")
        homepage.emailcheck().send_keys(more[1])
        log.info("getting email")
        homepage.exampleCheck().send_keys(more[2])
        log.info("getting password")


        sel = Select(homepage.selCheck())
        sel.select_by_visible_text("Male")

        homepage.subCheck().click()
        alertText = homepage.alertCheck().text
        assert ("success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=sdata.datatosend)
    def more(self,request):
        return request.param


