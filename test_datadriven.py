from playwright.sync_api import Page,expect
import pytest


search_items=["laptop","smartphone","monitor"]

@pytest.mark.parametrize("item", search_items)

def test_datadriven(item,page: Page):
    page.goto("https://demowebshop.tricentis.com")
    page.locator("#small-searchterms").fill(item) # need to pass items name..
    page.get_by_role("button",name="Search").click()
    page.wait_for_timeout(2000)
    items_dis=page.locator("h2 a").nth(0)
    expect(items_dis).to_contain_text(item,ignore_case=True)

