import json
import selenium.webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


#@pytest.fixture()
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
    driver.get("https://demoqa.com/")
    driver.implicitly_wait(10)
    #yield driver
    #driver.quit()
    return driver



def quit_browser(webdriver):
    webdriver.quit()


def readData():
    # Read the file
    with open('data.json') as data_file:
        config = json.load(data_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

