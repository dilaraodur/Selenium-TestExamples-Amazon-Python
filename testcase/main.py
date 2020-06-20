
import unittest
from selenium import webdriver
import page
import loginInfo


class AmazonTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.com/")

    def test_page_load(self):
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(3)
        self.assertTrue(mainPage.is_title_matches_MainPage())

    def test_sign_in_button(self):
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(3)
        mainPage.click_signin()
        self.driver.implicitly_wait(3)
        signInPage = page.SignInPage(self.driver)
        self.driver.implicitly_wait(3)
        self.assertTrue(signInPage.is_title_matches_SignIn())

    def test_login(self):
        mainPage = page.MainPage(self.driver)
        self.driver.implicitly_wait(5)
        mainPage.click_signin()
        self.driver.implicitly_wait(5)
        signInPage = page.SignInPage(self.driver)
        signInPage.email_text_element = loginInfo.email
        signInPage.click_continue_button()
        self.driver.implicitly_wait(5)
        signInPage.password_text_element = loginInfo.password
        signInPage.click_signin_button()
        main_Page = page.MainPage(self.driver)
        self.driver.implicitly_wait(5)
        self.assertTrue(main_Page.is_title_matches_MainPage())

    def test_search(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "macbook"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        self.assertTrue(search_result_page.is_result_found())


    def test_sorting_avr_customer_review(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "macbook"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.click_sorting_button()
        self.driver.implicitly_wait(15)
        search_result_page.click_avr_review_element()
        self.driver.implicitly_wait(5)
        self.assertTrue(search_result_page.is_sorting_page_url_matches())


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


