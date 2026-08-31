from playwright.sync_api  import Page , expect
import pytest
def test_login(page: Page):
     page.goto("https://www.google.com")
     expect(page).to_have_title("Google")


def test_login_invalid(page: Page):
     page.goto("https://www.google.com")
     expect(page).to_have_title("Google123")


