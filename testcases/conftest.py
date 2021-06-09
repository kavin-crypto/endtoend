import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def browser_invoke(request):
    global driver
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
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


