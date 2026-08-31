from playwright.sync_api import Page , expect


def test_static(page : Page):
       page.goto("https://testautomationpractice.blogspot.com/")
       #locating table
       table1=page.locator("table[name='BookTable'] tbody")
       expect(table1).to_be_visible()
       #to locate total number of rows in a table
       rows = table1.locator("tr")
       count=rows.count()
       print("total_rows",count)
       expect(rows).to_have_count(count)
       # to  count total numbers of headers/columns in a table
       columns = rows.locator("th")
       count1 = columns.count()
       print("total_columns", count1)
       expect(columns).to_have_count(count1)
       #to read all the data in second row of the column
       data = rows.nth(2).locator("td")
       page.wait_for_timeout(3000)
       second = data.all_inner_texts()
       print("datas==>",second)
       #read all the data in the table
       all_data=rows.all() #=====> all is for making all the locators in a list like a list of locators
       #for i in all_data[1:]:
         #  print("data being printed")

         #  print(i)

       #on conditional statement
       for row in all_data[1:]:
           author = row.locator("td").nth(1).inner_text()
           print(author)
           if author=="Mukesh":
               bookname=row.locator("td").nth(0).inner_text()
               print(f"{author}\t{bookname}")

       #total of all the products
       total_price=0
       for row in all_data[1:]:
           price = row.locator("td").nth(3).inner_text()
           total_price+= int(price)
           print(total_price)





