from itertools import dropwhile

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class Adminpage:

    adminmenu = (By.XPATH, "//span[text()='Admin']")
    Username = (By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div//input")
    userrole = (By.XPATH, "//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
    employee = (By.XPATH,"//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    status = (By.XPATH,"//label[text()='Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")

    def __init__(self,driver):
        self.driver = driver

    def admin_menu(self,):
        self.driver.find_element(*self.adminmenu).click()

    def Usernamee(self,username):
       self. driver.find_element(*self.Username).send_keys(username)

    def userrolee (self,):
      dropdown =   self.driver.find_element(*self.userrole)
      dropdown.click()
      dropdown.send_keys(Keys.ARROW_DOWN)
      dropdown.send_keys(Keys.ENTER)
    def employeee(self,employee):
        self.driver.find_element(*self.employee).send_keys(employee)
    def statuss (self):
        select = self.driver.find_element(*self.status)
        select.click()
        select.send_keys(Keys.ARROW_DOWN)
        select.send_keys(Keys.ENTER)
