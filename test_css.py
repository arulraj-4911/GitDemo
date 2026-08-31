#css -- work  based on DOM
#usage of css
#tag along with id  ---tag#id
#tag along with class  ---tag.class
#tag with any attribute  ---tag[attribute=value]
#tag class attribute  ---tag.class[attribute=value]
import pytest
from playwright.sync_api import Page , expect
#def test_css_verify(page: Page):
    #page.goto("https://demowebshop.tricentis.com/")
    #tag and id combo
   # page.locator("input#small-searchterms").fill("mobile")
    #tag and class combo
   #page.locator("input.search-box-text").fill("Mobile")
    #tag and attribute
    #page.locator("input[name=q]").fill("Mobile")
    #tag class and attribute
   # page.locator("input.search-box-text[name=q]").fill("Mobile")

def test_testing_app(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    logo=page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()
    page.locator("input.search-box-text").fill("computer")
    page.get_by_role("button",name="Search").click()
    page.wait_for_timeout(3000)
    result=page.locator("h2>a[href$='computer']")
    print(result.count())
    op=[]
    for i in range(result.count()):
         op.append(result.nth(i).text_content())

    print(op[0])
    print(op[2])
    print(op[1])
   



