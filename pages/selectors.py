from selenium.webdriver.common.by import By

selectores = {
    'elementBtn': 'div.card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > svg:nth-child(1) > path:nth-child(1)',
    'elementTitle': 'html body div#app div.body-height div.container.playgound-body div.pattern-backgound.playgound-header div.main-header',
    'textBoxBtn': 'html body div#app div.body-height div.container.playgound-body div.row div.col-12.mt-4.col-md-3 div.left-pannel div.accordion div.element-group div.element-list.collapse.show ul.menu-list li#item-0.btn.btn-light span.text',
    'fullNameInput': '#userName',
    'emailInput': '#userEmail',
    'currentAdressInput': '#currentAddress',
    'submitBtb': '#submit',
    'nameTxt': '#name',
    'emailTxt': '#email',
    'currentAdressTxt': 'p#currentAddress'
}


def return_web_element(driver, element):
    return driver.find_element(By.CSS_SELECTOR, find_selector(element))


def click_on_web_element(driver, element):
    driver.find_element(By.CSS_SELECTOR, find_selector(element)).click()


def find_selector(element):
    return selectores.get(element)