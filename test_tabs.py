from playwright.sync_api import Page , expect ,Playwright
import pytest

def test_brow_tabs(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    parentpage=context.new_page()
    parentpage.goto("https://testautomationpractice.blogspot.com/")
    parentpage.on("page",lambda page: page.wait_for_load_state())
    parentpage.locator("button:has-text('New Tab')").click()
    parentpage.wait_for_timeout(4000)
    all_pages = context.pages
    print(len(all_pages))
    print("title of the parent page:",all_pages[0].title())
    print("title of the child page:", all_pages[1].title())



