import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.cls.driver
        driver.save_screenshot(f"{report.nodeid.replace('::', '_')}.png")