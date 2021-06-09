import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def browser_invoke(request):
    browser = request.config.getoption("--browser_name")

    customize = webdriver.ChromeOptions()
    customize.add_argument("--start-fullscreen")
    customize.add_argument("--ignore-certificate-errors")
    customize.add_argument("incognito")

    if browser == "chrome":
        driver = webdriver.Chrome("/Users/kavin/Downloads/chromedriver-3",options=customize)
    elif browser == "safari":
        driver = webdriver.Safari()

    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver # cls.driver :: were our driver object is passed to fixtures instance [request],so once we call fixture this driver also invoke
    yield
    driver.quit()


