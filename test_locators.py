import re

from playwright.sync_api import Page, expect

def test_locating(page: Page):
    page.goto("https://automationexercise.com/")

    logo = page.get_by_alt_text("Website for automation practice")#al_text
    expect(logo).to_be_visible()
    expect(page.get_by_text(re.compile(".*Subscription.*"))).to_be_visible()#get_by_text
    expect(page.get_by_role("heading",name="FEATURES ITEMS")).to_be_visible()#GET BY ROLE
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_placeholder("First Name").fill("Arulraj")#placeholder --when the overlay  of text is visible in text box or has the atribute placeholder
    page.get_by_label("Last Name").fill("dff")#by label -- commonly for filling name and all
    page.get_by_title("title value")#title
    page.get_by_test_id()


def test_hrmlogin(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()

