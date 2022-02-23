from pages.formPage2 import Form
from pages.homePage import Home
from test.conftest import browser, quit_browser, readData, old_browser


def test_fill_form2(browser):
    form_page = Form(browser)
    home_page = Home(browser)

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
    form_page.verify("name")
    """
    form_page.verifyNameIsDisplayed()
    form_page.verifyEmailIsDisplayed()
    form_page.verifyCurrentAddressIsDisplayed()
    """
