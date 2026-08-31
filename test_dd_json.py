from playwright.sync_api import Page,expect
import pytest
import json

#to read json file
f = open("playwright/file.json", "r")
login_data=json.load(f)
@pytest.mark.parametrize("email,password,validity",[(data["email"],data["password"],data["validity"])for data in login_data])
def test_datadriven(email,password,validity,page: Page):
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


