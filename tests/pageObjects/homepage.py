from selenium.webdriver.common.by import By


class HomePage:
     def __init__(self,driver):
        self.driver = driver


     name = (By.CSS_SELECTOR,"[name='name']")
     email = (By.NAME,"email")
     example = (By.ID,"exampleCheck1")
     sel = (By.ID,"exampleFormControlSelect1")
     sub = (By.XPATH,"//input[@value='Submit']")
     alert = (By.CSS_SELECTOR,"[class*='alert-success']")

     def shopItems(self):
        return self.driver.find_element(*HomePage.name)

     def emailcheck(self):
         return self.driver.find_element(*HomePage.email)

     def exampleCheck(self):
         return self.driver.find_element(*HomePage.example)
     def selCheck(self):
        return self.driver.find_element(*HomePage.sel)
     def subCheck(self):
        return self.driver.find_element(*HomePage.sub)
     def alertCheck(self):
        return self.driver.find_element(*HomePage.alert)



