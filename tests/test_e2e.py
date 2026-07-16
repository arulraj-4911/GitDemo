from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from tests.pageObjects.homepage import HomePage
from tests.pageObjects.Baseclass import BaseClass


#@pytest.mark.usefixtures("setup")

class Test1(BaseClass):
       def test_e2e(self):
        homepage = HomePage(self.driver)
        action = ActionChains(self.driver)
        action.move_to_element(homepage.shopItems()).perform()
        action.move_to_element(self.driver.find_element(By.LINK_TEXT, "Top")).click().perform()

