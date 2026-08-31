from playwright.sync_api import Page , expect ,Playwright
import time
import datetime


def test_screenshot(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    time_stamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    #page screenshot
    #page.screenshot(path=f"screenshot/homepage-{time_stamp}.png")
    #full page screenshot
   # page.screenshot(path=f"screenshot/homepage-{time_stamp}.png",full_page=True)
    #specific section screenshot
    logo=page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=f"screenshot/homepage-{time_stamp}.png")
    
