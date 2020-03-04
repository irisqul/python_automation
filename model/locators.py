#in that file were locators and URL of an actual web-app, thus I deleted most of them in order to follow NDA.
#I left few not real examples to show the way I work with CSS and X-PATH

from selenium.webdriver.common.by import By


class BasePageLocators():
    CITY_LINK = (By.CSS_SELECTOR, ".icon-city")


class DistrictPageLocators():
    CANCEL_BUTTON = (By.CSS_SELECTOR, ".btn-danger")


class HousePageLocators():
# Appearance
    HOUSE_URL = "https://some-url.ru"
    HOUSE_INFO_TAB = (By.XPATH, "//a[contains(text(),'Информация')]")
    HOUSE_SCHEMA_TAB = (By.XPATH, "//a[contains(text(),'Схема')]")
    TITLE_NAME = (By.XPATH, "//th[contains(text(),'Название')]")
    SAVE_BUTTON = (By.CSS_SELECTOR, "[value='Сохранить']")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(),'Отменить')]")

# Tech tab
    ADD_PREMISE_NAME_INPUT = (By.CSS_SELECTOR, "#technical_area_name")


class SignupPageLocators():
    SIGNUP_FORM = (By.CSS_SELECTOR, ".box-item:nth-child(1) #new_user")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, '.box-item:nth-child(1)  .actions')



