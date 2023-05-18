import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture()
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            service=Service("/Users/vamshi/Downloads/drivers/chromedriver_mac_arm64/chromedriver"))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service("/Users/vamshi/Downloads/drivers/geckodriver-v0.32.2-macos-aarch64"
                                                   "/geckodriver"))
    # request.cls.driver = driver
    driver.implicitly_wait(3)
    return driver


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'vamshi'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
