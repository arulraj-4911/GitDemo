from playwright.sync_api import Page


def select_checkin(page: Page, year,month,day):
    while True:
        checkin_month = page.locator(
            "h3[id^='bui-calendar-month-']"
        ).nth(0).inner_text()
        selected_month,selected_year=checkin_month.split()
        if selected_month==month and selected_year==year:
            break
        else:
            page.locator("span[class='fc70cba028 e2a1cd6bfe']").click()

    checkin_date=page.locator("div[class='d7bd90e008']").nth(0).locator("table[class='b8fcb0c66a'] td").all()

    for dates in checkin_date:
        all_text=dates.inner_text()
        if all_text==day:
            dates.click()
            break

def select_checkout(page: Page, year,month,day):
    while True:
        checkout_month = page.locator(
            "h3[id^='bui-calendar-month-']"
        ).nth(1).inner_text()
        selected_month,selected_year=checkout_month.split()
        if selected_month==month and selected_year==year:
            break
        else:
            page.locator("span[class='fc70cba028 e2a1cd6bfe']").click()


    checkin_date = page.locator("div[class='d7bd90e008']").nth(1).locator("table[class='b8fcb0c66a'] td").all()

    for dates in checkin_date:
        all_text = dates.inner_text()
        if all_text == day:
            dates.click()
            break

def test_bookingdate(page:Page):
    page.goto("https://www.booking.com/")
    box=page.get_by_test_id("searchbox-dates-container")
    box.click()


    select_checkin(page,"2025","August","28")
    select_checkout(page,"2025","September","10")

    selected_start=page.get_by_test_id("date-display-field-start").inner_text()
    selected_end=page.get_by_test_id("date-display-field-end").inner_text()
    print("selected checkin date:",selected_start)
    print("selected checkout date:",selected_end)



