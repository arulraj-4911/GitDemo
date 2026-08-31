from playwright.sync_api import Page , expect

def test_boxws(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    box = page.locator("input[id='name']")
    expect(box).to_be_visible()
    expect(box).to_have_attribute("maxlength","15")
    length = box.get_attribute("maxlength")
    print("lengh of the box is ",length)
    box.fill("arul")
    entered = box.input_value()
    print("entered is ",entered)

