import pytest
from playwright.async_api import Page , expect , async_playwright

@pytest.mark.asyncio
async def test_verify():
     async with async_playwright() as p:
      browser = await p.chromium.launch(headless=False)
      mypage = await browser.new_page()
      await mypage.goto("https://playwright.dev/")
      url = mypage.url
      print(url)

