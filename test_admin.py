from logger import LogGen
from loginpage import Loginpage
from adminpage import Adminpage


def  test_admin_search(setup):
    logger = LogGen.loggen()
    driver = setup

    login = Loginpage(driver)

    login.login("Admin","admin123")
    logger.info("login page created")


    admin = Adminpage(driver)
    logger.info("admin page created")
    admin.admin_menu()

    admin.Usernamee("arulraj")
    admin.userrolee()
    admin.employeee("jaga")
    admin.statuss()