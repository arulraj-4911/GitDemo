from playwright.sync_api import Page , expect

def test_radio(page: Page):
        page.goto("https://testautomationpractice.blogspot.com/")
        male = page.locator("#male")
        page.wait_for_timeout(2000)
        #to check button ic not clicked
        expect(male).not_to_be_checked()
        #clicking and checking
        male.check()
        expect(male).to_be_checked()
        page.wait_for_timeout(5000)