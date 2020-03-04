from model.locators import AdminPanelPageLocators
from model.locators import BasePageLocators
from model.locators import IntercomsPageLocators
from model.key import Key


class KeyHelper:

    def __init__(self, app):
        self.app = app

    def open_key_card(self):
        wd = self.app.wd
        wd.find_element(*IntercomsPageLocators.KEY_CARD).click()
        wd.implicitly_wait(3)

    def open_connected_key(self):
        wd = self.app.wd
        self.wd.find_element(*IntercomsPageLocators.KEY_CONNECTED).click()
        wd.implicitly_wait(3)

    def open_keyset(self):
        wd = self.app.wd
        self.wd.find_element(*IntercomsPageLocators.KEY_SETS).click()
        wd.implicitly_wait(3)

    def open_district_page(self):
        wd = self.app.wd
        wd.find_element(*BasePageLocators.ADMIN_PANEL_LINK).click()
        wd.implicitly_wait(3)

    def open_add_key(self):
        wd = self.app.wd
        self.open_district_page()
        wd.find_element(*BasePageLocators.ADD_BUTTON).click()
        wd.implicitly_wait(3)
        wd.find_element(*BasePageLocators.ADD_BUTTON_KEY).click()
        wd.implicitly_wait(3)
        wd.find_element(*BasePageLocators.ADD_KEY).click()
        wd.implicitly_wait(3)

    def fill_add_key_form(self, key):
        wd = self.app.wd
        self.change_field_value("group_name", key.name)
        self.change_field_value("group_header", key.header)
        self.change_field_value("group_footer", key.footer)
        wd.find_element(*BasePageLocators.SAVE_BUTTON).click()
        wd.implicitly_wait(3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)






