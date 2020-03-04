from model.locators import KeyPageLocators
from model.locators import NavigationLocators
from model.locators import DistrictPageLocators
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class KeyPageHelper:

    def __init__(self, app):
        self.app = app

    # Tools
    def is_element_present(self, how, what):
        wd = self.app.wd
        try:
            wd.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


# Appearance
    def open_key_page(self):
        wd = self.app.wd
        # подождать пока появится ссылка на Ключи доступа
        key_link = WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                                    ((By.XPATH,
                                                      "//*[contains(text(),'Ключи доступа')]")))
        key_link.click()
        time.sleep(3)

    def key_elements_are_present(self):
        wd = self.app.wd
        assert NavigationLocators.KEY_PAGE_URL in wd.current_url
        assert self.is_element_present(
            *KeyPageLocators.SEARCH), "Search input is not present"
        assert self.is_element_present(
            *KeyPageLocators.SEARCH_BUTTON), "Search button is not present"
        assert self.is_element_present(
            *KeyPageLocators.KEY_NEW_BUTTON), "Add new key button is not present"
        assert self.is_element_present(
            *KeyPageLocators.KEY_UPLOAD_BUTTON), "Upload key is not present"
        assert self.is_element_present(
            *KeyPageLocators.KEY_LAST_PAGE), "Last page button is not present"
        assert self.is_element_present(
            *KeyPageLocators.KEY_NEXT_PAGE), "Next page button is not present"

# SEARCH
    def perform_search(self, text):
        wd = self.app.wd
        wd.find_element(*KeyPageLocators.SEARCH).click()
        wd.find_element(*KeyPageLocators.SEARCH).clear()
        wd.find_element(*KeyPageLocators.SEARCH).send_keys(text)
        wd.find_element(*KeyPageLocators.SEARCH_BUTTON).click()

    def search_result_are_present(self, text):
        assert self.is_element_present(
            *KeyPageLocators.KEY_NUMBER_TITLE), "Search result table is not present"
        assert self.is_element_present(
            By.XPATH,
            "//*[contains(text(),'"+text+"')]"), "Search result table is not present"

    def search_result_nothing_found_is_present(self):
        assert self.is_element_present(
            *KeyPageLocators.NOTHING_FOUND_MESSAGE), "Nothing found message is not present"

# Service key
    def open_page_by_url(self, url):
        wd = self.app.wd
        wd.get(url)
        time.sleep(1)

    def open_service_key_page(self,url):
        wd = self.app.wd
        self.open_page_by_url(url)
        time.sleep(2)
        wd.find_element(*DistrictPageLocators.TAB_SERVICE_KEY).click()
        time.sleep(2)
        wd.find_element(*KeyPageLocators.FIRST_KEY_EYE_ICON).click()

    def should_be_service_key_page(self):
        wd = self.app.wd
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, ".row:nth-child(1) .x_title h2")))
        assert self.is_element_present(
            *KeyPageLocators.SERVICE_KEY_TITLE), "Service key title is not present"
        assert self.is_element_present(
            *KeyPageLocators.EDIT_SERVICE_KEY_BUTTON), "Edit service key button is not present"
        assert self.is_element_present(
            *KeyPageLocators.EDIT_SERVICE_KEY_RIGHTS_BUTTON), "Edit service key button is not present"
        # assert self.is_element_present(
        #     *KeyPageLocators.BLOCK_SERVICE_KEY_BUTTON), "Block service key button is not present"
        assert self.is_element_present(
            *KeyPageLocators.DELETE_SERVICE_KEY_BUTTON), "Delete service key button is not present"

    def open_edit_service_key_by_url(self, url):
        wd = self.app.wd
        self.open_page_by_url(url)
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, ".row:nth-child(1) .x_title h2")))
        wd.find_element(*KeyPageLocators.EDIT_SERVICE_KEY_BUTTON).click()

    def should_be_edit_service_key_page(self):
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, ".row:nth-child(1) .x_title h2")))
        assert self.is_element_present(
            *KeyPageLocators.SERVICE_KEY_TITLE), "Service key title is not present"