from playwright.sync_api import Page , expect

#single selected dropdown
#def test_drop(page : Page):
       # page.goto("https://testautomationpractice.blogspot.com/")
        #3 wyas to select dropdown
        #page.locator("#country").select_option(label="China")#by label locating ,label is optional
        #page.locator("#country").select_option(value="germany")  # by value locating , value is optional
        #page.locator("#country").select_option(index=2)  # by value index, should mention index word rather than simply giving numbers
       # total = page.locator("//select[@id='country']//option")
       # print(total.count())
       ## expect(total).to_have_count(10)
       ## contents =[test.strip() for test in total.all_text_contents()]
     ##   for option in contents:
    #        print(option)
   #     page.wait_for_timeout(3000)

#multi selected dropdowns
def test_multi(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #page.locator("#colors").select_option(label = ["Red","Green"]) #by label
    page.locator("#colors").select_option(value=["red", "white","green"])  # by value
    page.locator("#colors").select_option(index=[3,4])  # by indexes
    options = page.locator("select[id='colors']>option")
    expect(options).to_have_count(7)
    total = options.all_text_contents()
    for i in total:
        print(i)
    page.wait_for_timeout(3000)

