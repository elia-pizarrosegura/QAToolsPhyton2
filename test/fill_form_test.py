from pages.formPage import Form
from pages.homePage import Home
from test.conftest import browser, quit_browser, readData


def test_fill_form(driver):
    form_page = Form(driver, config) #config)
    home_page = Home(driver)

    # Given the form is displayed
    # home_page.load()
    home_page.verifyToolsQAPage()
    home_page.clickOnElements()
    form_page.clickOnForm()

    # When user fill the name, email and current address and click on submit
    form_page.fillName()
    form_page.fillEmail()
    form_page.fillCurrentAddress()
    form_page.clickSubmitButton()

    # Then system displays above the information that user has fill previously
    form_page.verifyNameIsDisplayed()
    form_page.verifyEmailIsDisplayed()
    form_page.verifyCurrentAddressIsDisplayed()


config = readData()
driver = browser(config)
test_fill_form(driver)
quit_browser(driver)
