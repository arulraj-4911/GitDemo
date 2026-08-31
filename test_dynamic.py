from playwright.sync_api import Page , expect
import pytest
def test_dynamic_xpath(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    for i in range(5):
     button = page.locator("//button[starts-with(@name,'st')  ]")
     button.click()
     page.wait_for_timeout(2000)
