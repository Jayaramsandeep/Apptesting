from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\Dell\\Downloads\\chromedriver_win32\\jayaram.exe")
        print("Launching Chrome browser............")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\Dell\\Downloads\\geckodriver-v0.29.1-win64\\geckodriver.exe")
        print("Launching FireFox...........")

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############ PyTest HTML Report ################

# It is hook for Adding Enivronment info to html report

def pytest_configure(config):
    config._metadata['project Name'] = ' nopCommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = ' Jayaram sandeep '

# It is hook for delet/Modify enivronment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
