from model.locators import LoginPageLocators


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        if len(wd.find_elements(*LoginPageLocators.WELCOME_MESSAGE)) > 0:
            wd.find_element(*LoginPageLocators.USER_EMAIL).click()
            wd.find_element(*LoginPageLocators.USER_EMAIL).clear()
            wd.find_element(*LoginPageLocators.USER_EMAIL).send_keys(username)
            wd.find_element(*LoginPageLocators.USER_PASSWORD).click()
            wd.find_element(*LoginPageLocators.USER_PASSWORD).clear()
            wd.find_element(*LoginPageLocators.USER_PASSWORD).send_keys(password)
            wd.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
            wd.implicitly_wait(3)

    def logout(self):
        wd = self.app.wd
        wd.find_element(*LoginPageLocators.LOGGED_USER).click()
        wd.find_element_by_link_text("Выход").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(*LoginPageLocators.LOGGED_USER)) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(*LoginPageLocators.LOGGED_USER).text

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
