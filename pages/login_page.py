from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url is not True"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is missing"

    def register_new_user(self, email, password):
        email_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_registration.send_keys(email)
        password_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_registration.send_keys(password)
        password_registration_again = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_AGAIN)
        password_registration_again.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_registration.click()
