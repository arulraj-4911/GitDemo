from playwright.sync_api import Page , expect ,Playwright
import pytest

def test_record_video(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(http_credentials={"username":"admin","password":"admin"},record_video_dir="videos/",record_video_size={"width":1024,"height":768})
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    content = page.locator("div[class='example'] p")
    expect(content).to_contain_text("Congratulations! You must have the proper credentials.")
    page.wait_for_timeout(5000)
    context.close()
    browser.close()
