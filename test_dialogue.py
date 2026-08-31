import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def  test_alerts(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #registering an event:
    #approach-1
    def handle_dialog(dialog):
        dialog.accept()

    page.on("dialog", handle_dialog)
    page.wait_for_timeout(5000)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def  test_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #approach-2
    page.on("dialog", lambda dialog:dialog.accept())
    page.wait_for_timeout(5000)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)
@pytest.mark.skip
def  test_confirmation_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #approach-3
    page.on("dialog", lambda dialog:dialog.dismiss())
    page.wait_for_timeout(5000)
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)
    text = page.locator("#demo").inner_text()
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")
    print("text displayed:",text)

def  test_prompt(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #approach-4
    page.on("dialog", lambda dialog:dialog.accept("aj"))
    page.wait_for_timeout(5000)
    page.locator("#promptBtn").click()

    text = page.locator("#demo").inner_text()
    expect(page.locator("#demo")).to_have_text("Hello aj! How are you today?")
    print("text displayed:",text)

    

