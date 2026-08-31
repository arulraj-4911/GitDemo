import openpyxl
from playwright.sync_api import Page,expect
import pytest
login_data=[]
workbook=openpyxl.load_workbook("playwright/playwright_excel.xlsx")
sheet=workbook.active
for i in sheet.iter_rows(min_row=2,values_only=True):
    email,password,validity=i
    login_data.append((str(email or ""),str(password or ""),str(validity)))#here or "" is used bcoz some times excel sheet may empty mistakenly so it will take as no value type
    workbook.close()
@pytest.mark.parametrize("email,password,validity",login_data)
def test_datadriven_xl(email,password,validity,page: Page):
    page.goto("https://demowebshop.tricentis.com")
    page.get_by_role("link",name="Log in").click()
    page.get_by_role("textbox",name="Email").fill(email)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button",name="Log in").click()
    if validity == "valid":
        login=page.get_by_role("link",name="Log out")
        expect(login).to_be_visible(timeout=4000)
        print("original is passed")

    else:
        error=page.locator("div[class='validation-summary-errors'] li")
        Mess=error.inner_text()
        print(Mess)
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")
        print("not authourized")


