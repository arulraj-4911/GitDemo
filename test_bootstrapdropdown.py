from playwright.sync_api import Page , expect


def test_dropdown(page : Page):
       page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
       page.get_by_placeholder("Username").fill("Admin")
       page.get_by_placeholder("Password").fill("admin123")
       page.get_by_role("button",name="Login").click()
       page.get_by_text("PIM").click()
       page.locator("form i").nth(2).click()
       options= page.locator("div[role='listbox'] span")
       page.wait_for_timeout(3000)
       count=options.count()
       print(count)
       page.wait_for_timeout(6000)
       print(options.all_text_contents())
       #for i in range(count):
              #print(options.nth(i).text_content())

       for i in range(count):
              text=(options.nth(i).inner_text())
              print("option to be selected",text)
              if text=="HR Manager":
                     print("matching success:===>",text)
                     options.nth(i).click()
                     break



       page.wait_for_timeout(5000)

