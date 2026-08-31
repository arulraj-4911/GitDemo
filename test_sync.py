from playwright.sync_api import Page ,  expect
def test_verify(page:Page):
      page.goto("https://playwright.dev/")
      url = page.url
      print(url)
      expect(page).to_have_url("https://playwright.dev/")

def test_title(page:Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

