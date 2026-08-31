from playwright.sync_api import Page, expect
import pytest
@pytest.mark.skip
def test_pagination(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    has_manypage = True
    while has_manypage:
        rows = page.locator("//table[@id='example']//tbody//tr").all()
        for row in rows:
            print(row.inner_text())

        next_button = page.get_by_role("link", name="Next")
        is_disabled = next_button.get_attribute("class")
        if "disabled" in is_disabled:
            has_manypage = False
        else:
            next_button.click()
            page.wait_for_timeout(500)  # let the table refresh before re-querying rows

def test_filtering(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")
    dropdown=page.locator("select[id='dt-length-0']")
    dropdown.select_option(label="25")
    rows = page.locator("//table[@id='example']//tbody//tr")
    expect(rows).to_have_count(25)



