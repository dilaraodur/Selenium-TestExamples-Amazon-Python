from locator import *
from element import BasePageElement

class EmailTextElement(BasePageElement):
    locator = "email"

class PasswordTextElement(BasePageElement):
    locator = "password"

class SearchTextElement(BasePageElement):
    locator = "field-keywords"

class BasePage(object):
    #object is optional
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches_MainPage(self):
        return True if "Amazon" in self.driver.title else False

    def click_signin(self):
        element = self.driver.find_element(*MainPageLocators.SIGNIN_ELEMENT)
        element.click()


    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SignInPage(BasePage):
    email_text_element = EmailTextElement()
    password_text_element = PasswordTextElement()

    def click_continue_button(self):
        element = self.driver.find_element(*SingInPageLocators.CONTINUE_BUTTON)
        element.click()

    def click_signin_button(self):
        element = self.driver.find_element(*SingInPageLocators.SIGNIN_BUTTON)
        main_page = element.click()
        return main_page

    def is_title_matches_SignIn(self):
        return True if "Sign-In" in self.driver.title else False


class SearchResultPage(BasePage):

    def is_result_found(self):
        return True if "No result found." not in self.driver.page_source else False

    def click_sorting_button(self):
        sorting_element = self.driver.find_element(*SearchResultsPageLocators.SORTING_BUTTON)
        sorting_element.click()

    def click_avr_review_element(self):
        avr_review_element = self.driver.find_element(*SearchResultsPageLocators.SORTING_AVR_REVIEW)
        avr_review_element.click()


    def is_sorting_page_url_matches(self):
        url = str(self.driver.current_url)
        return True if "review-rank" in url else False
