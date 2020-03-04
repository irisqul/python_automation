from model.base_page import BasePage
from model.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
