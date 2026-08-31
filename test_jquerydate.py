from playwright.sync_api import Page


def select_date(page, date, month, year, is_future):
    while True:
        current_month = page.locator("span.ui-datepicker-month").text_content()
        current_year = page.locator("span.ui-datepicker-year").text_content()
        if current_month == month and current_year == year:
            break

        if is_future:
            page.locator(".ui-datepicker-next").click()
        else:
            page.locator(".ui-datepicker-prev").click()

        page.wait_for_timeout(300)  # let the calendar re-render

    date_picker = page.locator("table[class='ui-datepicker-calendar'] td").all()

    for dates in date_picker:
        text = dates.inner_text()
        if text == date:
         dates.click()
         break



def test_date(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    box = page.locator("input#datepicker")
    box.click()

    is_future = False
    date = "20"
    month = "August"
    year = "2020"

    select_date(page, date, month, year, is_future)