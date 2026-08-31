from playwright.sync_api import Page , expect


def test_example(page : Page):
       page.goto("https://bstackdemo.com/")
       page.locator("div[class='sort']>select").select_option(label="Lowest to highest")
       products = page.locator("//div[@class='shelf-item']//p").all_text_contents()
       price = page.locator("//div[@class='val']//b").all_text_contents()
       pro = products.copy()
       sort = sorted(pro)
       price1 = price.copy()
       sort1 = sorted(price1,key=int)
       for i in sort:
        print("product is:",i)
       for j in sort1:
        print("price is :", j)

        page.wait_for_timeout(5000)