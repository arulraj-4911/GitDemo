from playwright.sync_api import Page , expect


def test_sorted(page : Page):
       page.goto("https://testautomationpractice.blogspot.com/")
       options = page.locator("select[id='colors']>option")  #unsorted
       option1=page.locator("#animals>option")#sorted
       original = [test.strip() for test in option1.all_text_contents()]
       text = original.copy()
       sorted_list = sorted(original)
       assert text == sorted_list
       print("options is  sorted list")
       original1 = [test.strip() for test in options.all_text_contents()]
       text1 = original1.copy()
       sorted_list1= sorted(original1)
       if text1  == sorted_list1:
         print("option1 is  sorted list")
       else:
           print("options is not sorted list")
       page.wait_for_timeout(5000)
