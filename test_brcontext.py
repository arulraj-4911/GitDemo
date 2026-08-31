from playwright.sync_api import Page , expect ,Playwright
import pytest

@pytest.mark.skip
def test_browser_context(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)#created browser
    context = browser.new_context()#created context
    page1 = context.new_page()
    page2 = context.new_page()
    page1.goto("https://testautomationpractice.blogspot.com/")
    page2.goto("https://testautomationpractice.blogspot.com/")

def test_handle_popup(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)  # created browser
    context = browser.new_context()  # created context
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("popup",lambda popup: popup.wait_for_load_state())
    page.locator("#PopUp").click()
    page.wait_for_timeout(5000)
    all_popups = context.pages
    print("all popups length",len(all_popups))
    #capturing url  for all popups
    for pw in all_popups:
        print("page urls=====>",pw.url)
        title=pw.title()
        if "Playwright" in title:
            pw.get_by_role("link",name="Get started").click()
            pw.wait_for_timeout(4000)
            expect(pw).to_have_title("Installation | Playwright")
            pw.close()#close the  playwright popup window


