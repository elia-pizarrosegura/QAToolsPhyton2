from pages.selectors import *


class Form:

    def __init__(self, driver):
        self.driver = driver

    def verifyElementPage(self):
        title = self.driver.find_element(By.CSS_SELECTOR, find_selector("elementTitle"))
        #  self.betterIdea(10, title.text)
        assert title.text == "Elements"
        print("Element page is displayed.")

    def clickOnForm(self):
        self.driver.find_element(By.CSS_SELECTOR, find_selector("textBoxBtn")).click()

    def fillName(self):
        full_name = self.driver.find_element(By.CSS_SELECTOR, find_selector("fullNameInput"))
        full_name.send_keys("Elia")

    def fillEmail(self):
        self.driver.find_element(By.CSS_SELECTOR, find_selector("emailInput")).send_keys("elia@elia.com")

    def fillCurrentAddress(self):
        self.driver.find_element(By.CSS_SELECTOR, find_selector("currentAdressInput")).send_keys("dirección")

    def clickSubmitButton(self):
        element = return_web_element(self.driver, "submitBtb")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(By.CSS_SELECTOR, find_selector("submitBtb")).click()

    def verify(self, verify):
        if verify == 'name':
            self.verifyNameIsDisplayed()
        elif verify == 'email':
            self.verifyEmailIsDisplayed()
        elif verify == 'address':
            self.verifyCurrentAddressIsDisplayed()
        else:
            assert False, "The element to verify is unknown."

    def verifyNameIsDisplayed(self):
        name = self.driver.find_element(By.CSS_SELECTOR, find_selector("nameTxt"))
        if "Elia" not in name.text:
            assert False, "The name is not displayed"
        else:
            print(f'The name {name.text} is displayed')

    def verifyEmailIsDisplayed(self):
        email = self.driver.find_element(By.CSS_SELECTOR, find_selector("emailTxt"))
        assert email.text == "Email:elia@elia.com"
        print(f'The email {email.text} is displayed.')

    def verifyCurrentAddressIsDisplayed(self):
        address = self.driver.find_element(By.CSS_SELECTOR, find_selector("currentAdressTxt"))
        if "dirección" not in address.text:
            assert False, "The current address is not displayed."
        else:
            print(f'The current address {address.text} is displayed.')


"""
    def terribleIdea(self, time):
        time.sleep(time)

    def betterIdea(self, time, text):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, time).until(EC.title_is(text))
"""
