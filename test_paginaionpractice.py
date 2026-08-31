from playwright.sync_api import Page , expect



def test_example(page : Page):
       page.goto("https://testautomationpractice.blogspot.com/")
       page.wait_for_timeout(3000)
       values=page.locator("table[id='productTable'] tbody tr").all()
       for i in values:
           real = i.locator("td").all_inner_texts()
           click = i.locator("td input[type='checkbox']")
           print(real)
           click.click()
           print("clicked")

