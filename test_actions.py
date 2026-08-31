from playwright.sync_api import Page , expect
import pytest

@pytest.mark.skip
def test_mouse(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    mouse = page.get_by_role("button",name="Point Me")
    page.wait_for_timeout(3000)
    mouse.hover()
    objects=page.locator("div[class='dropdown-content'] a").nth(0)
    page.wait_for_timeout(3000)
    objects.hover()
    page.wait_for_timeout(3000)
@pytest.mark.skip
def test_mouse_right_click(page:Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    button=page.locator(".context-menu-one")
    button.click(button="right")#tp perform right click
    page.wait_for_timeout(5000)
    page.on("dialog",lambda dialog:dialog.accept())
    page.wait_for_timeout(5000)
    options=page.locator(".context-menu-item").nth(0)
    options.click()
    page.wait_for_timeout(5000)
@pytest.mark.skip
def test_mouse_double_click(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    button=page.locator("button[ondblclick='myFunction1()']")
    button.dblclick() #perform double clicks
    b1=page.locator("input[id='field1']")
    b2=page.locator("input[id='field2']")
    expect (b2).to_have_value("Hello World!")
    page.wait_for_timeout(5000)

def test_mouse_dragdrop(page: Page):
        page.goto("https://testautomationpractice.blogspot.com/")
        source = page.locator("#draggable")
        destination = page.locator("#droppable")

       # approach:1
        #source.hover()
        #page.mouse.down() #click and hold the one need to be dragged
       ## destination.hover()
       ## page.mouse.up()
      #  page.wait_for_timeout(5000)

        #approach 2
        source.drag_to(destination)
        page.wait_for_timeout(5000)






