from pages.selectors import *
from test.constants import *


class Home:

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://demoqa.com/")

    def clickOnElements(self):
        self.driver.find_element(By.CSS_SELECTOR, find_selector(ELEMENT_BTN)).click()

    def verifyToolsQAPage(self):
        assert self.driver.title == "ToolsQA"
        print("ToolsQA page is displayed.")


