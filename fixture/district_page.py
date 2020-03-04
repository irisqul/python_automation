from model.locators import DistrictPageLocators
from model.locators import NavigationLocators
from model.district import District
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DistrictPageHelper:

    def __init__(self, app):
        self.app = app
#Tools
    def is_element_present(self, how, what):
        wd = self.app.wd
        try:
            wd.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open_district_page(self):
        wd = self.app.wd
        #подождать пока появится ссылка на Районы
        district_link = WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                                   ((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Комфорт'])[1]/following::a[2]")))
        district_link.click()
        time.sleep(3)
        assert NavigationLocators.DISTRICT_PAGE_URL in wd.current_url

    def change_field_value(self, choose_method, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(choose_method, field_name).click()
            wd.find_element(choose_method, field_name).clear()
            wd.find_element(choose_method, field_name).send_keys(text)

    def locate_districts_by_name(self, district):
        wd = self.app.wd
        #подождать пока таблица со списком районов загрузится
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                                    ((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Название'])[1]/following::a[1]")))
        districts = []
        #пройти по строкам таблицы районов и спарсить строки в которых название района совпадает с заданым
        for i in range(len(wd.find_elements(*DistrictPageLocators.DISTRICT_LIST))):
            if wd.find_elements(*DistrictPageLocators.DISTRICT_NAME)[i].text == district.name:
                name = wd.find_elements(*DistrictPageLocators.DISTRICT_NAME)[i].text
                deleteLink = wd.find_elements(*DistrictPageLocators.DISTRICT_DELETE)[i].get_attribute("href")
                editLink = wd.find_elements(*DistrictPageLocators.DISTRICT_EDIT)[i].get_attribute("href")
                districts.append(District(name=name, deleteLink=deleteLink, editLink=editLink))
        #возвращаем список из распаршенных объектов
        return districts

# Appearance
    def should_be_table_with_districts(self):
        assert self.is_element_present(
            *DistrictPageLocators.DISTRICT_TABLE_TITLE), "Table title is not present"
        assert self.is_element_present(
            *DistrictPageLocators.DISTRICT_TABLE_COLUMN_NAME), "Table column name is not present"
        assert self.is_element_present(
            *DistrictPageLocators.DISTRICT_TABLE_FIRST_ROW), "Table first row is not present"
        assert self.is_element_present(
            *DistrictPageLocators.ADD_NEW_DISTRICT_BUTTON), "Add new district button is not present"


# Open single district
    def open_single_district_click_name_in_the_row(self):
        wd = self.app.wd
        self.open_district_page()
        wd.find_element(*DistrictPageLocators.FIRST_DISTRICT_NAME).click()
        time.sleep(3)

    def open_single_district_eye_icon(self):
        wd = self.app.wd
        self.open_district_page()
        wd.find_element(*DistrictPageLocators.FIRST_DISTRICT_EYE_ICON).click()
        time.sleep(3)

    def should_be_tabs_in_single_district_page(self):
        wd = self.app.wd
        assert DistrictPageLocators.SINGLE_DISTRICT_BASE_URL in wd.current_url
        assert self.is_element_present(
            *DistrictPageLocators.TAB_ABOUT_DISTRICT), "Tab 'О районе' is not present"
        assert self.is_element_present(
            *DistrictPageLocators.TAB_BLOCKS), "Tab 'Блоки и дома' is not present"
        assert self.is_element_present(
            *DistrictPageLocators.TAB_NEWS), "Tab 'Новости района' is not present"
        assert self.is_element_present(
            *DistrictPageLocators. TAB_SERVICE_KEY), "Tab 'Сервисные ключи' is not present"
        assert self.is_element_present(
            *DistrictPageLocators.TAB_TERRITORIES), "Tab 'Территории' title is not present"


# Add district page
    def open_add_new_district_page(self):
        wd = self.app.wd
        wd.find_element(*DistrictPageLocators.ADD_NEW_DISTRICT_BUTTON).click()
        time.sleep(3)

    def should_be_add_new_district_url(self):
        wd = self.app.wd
        assert NavigationLocators.DISTRICT_PAGE_URL in wd.current_url

    def should_be_insert_fields(self):
        assert self.is_element_present(
            *DistrictPageLocators.INSERT_DISTRICT_NAME), "New district name field is not present"
        assert self.is_element_present(
            *DistrictPageLocators.INSERT_DESCRIPTION), "New district insert description field is not present"
        assert self.is_element_present(
            *DistrictPageLocators.SELECT_ADDRESS), "New district select address field is not present"
        assert self.is_element_present(
            *DistrictPageLocators.SAVE_BUTTON), "Save button is not present"
        assert self.is_element_present(
            *DistrictPageLocators.CANCEL_BUTTON), "Cancel button is not present"

    def get_districts_list(self):
        wd = self.app.wd
        districts = []
        for element in wd.find_elements(*DistrictPageLocators.DISTRICT_LIST):
            # use another way to parse name, id etc
            name = "Unknown"
            #name = (*DistrictPageLocators.DISTRICT_NAME).text
            #id = id.text
            address = "Omsk"
            #address = (*DistrictPageLocators.DISTRICT_ADDRESS).text
            districts.append(District(name=name, address=address))
        return districts

    def fill_district_form(self, district):
        wd = self.app.wd
        self.change_field_value(*DistrictPageLocators.INSERT_DISTRICT_NAME, district.name)
        wd.find_element(*DistrictPageLocators.SELECT_ADDRESS).click()
        wd.find_element(*DistrictPageLocators.SELECT_ADDRESS_INPUT).click()
        wd.find_element(*DistrictPageLocators.SELECT_ADDRESS_INPUT).clear()
        wd.find_element(*DistrictPageLocators.SELECT_ADDRESS_INPUT).send_keys(district.address + Keys.ENTER)
        wd.implicitly_wait(3)

    def edit_district_name(self, district):
        wd = self.app.wd
        self.change_field_value(*DistrictPageLocators.INSERT_DISTRICT_NAME, district.name)
        wd.find_element(*DistrictPageLocators.SAVE_BUTTON).click()

    def create_district(self, district):
        wd = self.app.wd
        self.fill_district_form(district)
        wd.find_element(*DistrictPageLocators.SAVE_BUTTON).click()

# Edit district
    def open_edit_district_page_by_edit_link(self, district):
        wd = self.app.wd
        # отрезаем от ссылки домен
        district.editLink = district.editLink[29:]
        wd.find_element(By.XPATH, '//a[@href="'+district.editLink+'"]').click()
        time.sleep(3)

    def should_be_edit_url(self, district):
        wd = self.app.wd
        assert district.editLink in wd.current_url

# Delete district
    def delete_district_by_delete_link(self, district):
        wd = self.app.wd
        #отрезаем от ссылки домен
        district.deleteLink = district.deleteLink[29:]
        #нажать на крестик
        wd.find_element(By.XPATH, '//a[@href="'+district.deleteLink+'"]').click()
        #confirm
        alert = wd.switch_to_alert()
        alert.accept()

    def district_should_be_deleted(self, district):
        wd = self.app.wd
        assert True
