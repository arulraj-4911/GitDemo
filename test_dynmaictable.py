from playwright.sync_api import Page , expect
import re


def test_dynamic(page : Page):
       page.goto("https://testautomationpractice.blogspot.com/")
       rows=page.locator("table[id=taskTable] tbody")
       columns = rows.locator("tr").all()
       value=""
       for i in columns:
           chrome = i.locator("td").nth(0).inner_text()
           if chrome == "Chrome":
               print(chrome)

               value = i.locator("td", has_text=re.compile(r"\d+%")).inner_text()
               print(value)
               break

       confirm = page.locator("strong[class='chrome-cpu']")
       expect(confirm).to_contain_text(value)
       page.wait_for_timeout(3000)









