from playwright.sync_api import Page , expect ,Playwright
import pytest

#inject user login with url:

#approach-1

@pytest.mark.skip
def test_authentication_popup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    content=page.locator("div[class='example'] p")
    expect(content).to_contain_text("Congratulations! You must have the proper credentials.")
    page.wait_for_timeout(5000)

#using context  - we can pass user and password along with context
#approach--2
def test_authentication2_popup(playwright):
    browser = playwright.chromium.launch(headless=False)
    content=browser.new_context(http_credentials={"username":"admin","password":"admin"})
    page=content.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    content=page.locator("div[class='example'] p")
    expect(content).to_contain_text("Congratulations! You must have the proper credentials.")
    page.wait_for_timeout(5000)

