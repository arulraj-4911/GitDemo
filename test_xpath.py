from playwright.sync_api import Page , expect

def test_xpath(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    #xpath absolute locator

    #logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
   # expect(logo).to_be_visible()

    #relative xpath  //tagname[@attribute='value']|
   # expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()

  #  page.wait_for_timeout(3000)

    #x path with contains
    #products = page.locator("//h2//a[contains(@href,'computer')]")
    #got=products.count()
    #expect(products).to_have_count(got)
    #print(products.first.text_content())
    #print(products.last.text_content())
    #print(products.nth(2).text_content())

  #x parth with starts-with()
    building = page.locator("//h2//a[starts-with(@href,'/build')]")
    total = building.count()
    expect(total).to_have_count(total)
 #xpath  with text()  --representing innner text of the element

    page.locator("//a[text()='Register']")

    #xpath with last()
    #same as before but additionally //li[last()] will be added

    #xpath with position
    #same as before but additionally //li[position()=desired positon number like 2 or 3 or 4 ] will be added




