from playwright.sync_api import Page , expect
import pytest

def test_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    box1 = page.locator("input[id='input1']")
    box2 = page.locator("input[id='input2']")
    box3 = page.locator("input[id='input3']")

    #insert_text()method
    box1.focus()
    page.keyboard.insert_text("arulraj")


    #to select the content
    page.keyboard.press("Control+A")

    #to copy the content
    page.keyboard.press("Control+C")

    #press tab key
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #filling the value
    page.keyboard.press("Control+V")

    # press tab key
    for i in range(2):
        page.keyboard.press("Tab")
        


    # filling the value
    page.keyboard.press("Control+V")

    expect(box2).to_have_value("arulraj")
    expect(box3).to_have_value("arulraj")

    page.wait_for_timeout(10000)


