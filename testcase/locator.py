from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.XPATH, '//*[@id="nav-search"]/form/div[2]/div/input')
    SIGNIN_ELEMENT = (By.XPATH,'//*[@id="nav-link-accountList"]/span[1]')


class SingInPageLocators(object):
    CONTINUE_BUTTON = (By.ID, 'continue')
    SIGNIN_BUTTON = (By.ID, 'signInSubmit')


class SearchResultsPageLocators(object):
    SORTING_BUTTON = (By.XPATH, '//*[@id="a-autoid-0-announce"]/span[1]')
    SORTING_AVR_REVIEW = (By.XPATH, '//*[@id="s-result-sort-select_3"]')
