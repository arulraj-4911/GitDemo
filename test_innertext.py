from itertools import product

from playwright.sync_api import Page , expect


def test_innertext(page : Page):
       page.goto("https://demowebshop.tricentis.com/")
       fall=page.locator(".product-title")
       total=fall.count()

       #inner text  vs text_content
       print("using inner_txt",fall.nth(1).inner_text())#will return actual text
       print("using text_cnt",fall.nth(1).text_content())#return content with text and special characters and spaces

       for i in range(total):
           print("using inner_txt", fall.nth(i).inner_text())  # will return actual text
           print("using text_cnt", fall.nth(i).text_content())  # return content with text and special characters and spaces

    #all inner text vs all text contents
       product_name = fall.all_text_contents()
       print(product_name)
       product_name1 = fall.all_inner_texts()
       print(product_name1)

    # all method
       locators=fall.all()
       print(locators[0].inner_text())



