from time import sleep
from selenium.webdriver.common.by import By
from features.page_objects.base_page import BasePage


class LogoutPage(BasePage):
    logout_button = (By.CSS_SELECTOR, 'a[href="/logout"]')
    logout_message = (By.CSS_SELECTOR, '.logout')
    hamburger_menu = (By.CSS_SELECTOR, 'div.bm-burger-button')

    def logout_via_logout_button(self):
        self.wait_for_element(self.hamburger_menu)
        sleep(1)
        hamburger_menu_button = self.find_element(*self.hamburger_menu)
        self.browser.execute_script("arguments[0].click();", hamburger_menu_button)
        self.wait_for_element(self.logout_button)
        logout_button = self.find_element(*self.logout_button)
        self.browser.execute_script("arguments[0].click();", logout_button)

    def logged_out_user_state(self):
        self.wait_for_element(self.logout_message)

    def enter_logout_url(self):
        self.visit()
