from model.locators import DistrictPageLocators
from model.locators import NavigationLocators
from model.locators import HousePageLocators
from model.house import House, Premise
from model.intercom import Intercom
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HousePageHelper:

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

    def open_house_page(self, district):
        wd = self.app.wd
        # подождать пока появится ссылка на Районы
        district_link = WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                                    ((By.XPATH,
                                                      "(.//*[normalize-space(text()) and normalize-space(.)='Комфорт'])[1]/following::a[2]")))
        district_link.click()
        time.sleep(3)
        #open house
        wd.find_element(By.XPATH, '//a[@href="'+district.link+'"]').click()
        time.sleep(3)
        house_link = WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                                    ((By.XPATH, "//div[@id='districtTabContent']/div/div/div[2]/div/div[2]/table/tbody/tr/td[3]/a")))
        house_link.click()
        time.sleep(3)

    def open_house_page_by_url(self, url):
        wd = self.app.wd
        wd.get(url)
        time.sleep(3)

    def change_field_value(self, choose_method, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(choose_method, field_name).click()
            wd.find_element(choose_method, field_name).clear()
            wd.find_element(choose_method, field_name).send_keys(text)

    def locate_districts_by_name(self, district):
        wd = self.app.wd
        # подождать пока таблица со списком районов загрузится
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.XPATH,
                                      "(.//*[normalize-space(text()) and normalize-space(.)='Название'])[1]/following::a[1]")))
        districts = []
        # пройти по строкам таблицы районов и спарсить строки в которых название района совпадает с заданым
        for i in range(len(wd.find_elements(*DistrictPageLocators.DISTRICT_LIST))):
            if wd.find_elements(*DistrictPageLocators.DISTRICT_NAME)[i].text == district.name:
                name = wd.find_elements(*DistrictPageLocators.DISTRICT_NAME)[i].text
                deleteLink = wd.find_elements(*DistrictPageLocators.DISTRICT_DELETE)[i].get_attribute("href")
                editLink = wd.find_elements(*DistrictPageLocators.DISTRICT_EDIT)[i].get_attribute("href")
                districts.append(District(name=name, deleteLink=deleteLink, editLink=editLink))
        # возвращаем список из распаршенных объектов
        return districts

#Appearance
    def should_be_tabs_at_house_page(self):
        wd = self.app.wd
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INFO_TAB), "Tab 'Информация' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_TECH_TAB), "Tab 'Тех.помещения' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_SCHEMA_TAB), "Tab 'Схема' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INTERCOM_TAB), "Tab 'Домофоны' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_FLATS_TAB), "Tab 'Квартиры' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_BKFN_TAB), "Tab 'БКФН' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_PARKING_TAB), "Tab 'Машиноместа' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_STORE_TAB), "Tab 'Кладовки' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_ORG_TAB), "Tab 'Организации' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_NEWS_TAB), "Tab 'Объявления УК' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_EDIT_BUTTON), "Tab 'Редактировать дом' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_EDIT_BUTTON), "Button 'Редактировать дом' is not present"

    def should_be_info_tab(self):
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INFO_TITLE), "Title 'Информация' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INFO_FLATS_CARD), "Card 'Квартир' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INFO_DEVICES_CARD), "Card 'Устройства' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INFO_ACTIVE_DEVICES_24_CARD), "Card 'Активные устройства за 24 часа' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INFO_ACTIVE_DEVICES_7_CARD), "Card 'Активные устройства за 7 дней' is not present"
        assert self.is_element_present(
            *HousePageLocators.HOUSE_INFO_ACTIVE_DEVICES_MONTH_CARD), "Card 'Активные устройства за месяц' is not present"

#Tech tab
    def open_tech_tab(self, url):
        wd = self.app.wd
        self.open_house_page_by_url(url)
        wd.find_element(*HousePageLocators.HOUSE_TECH_TAB).click()
        time.sleep(3)

    def should_be_tech_tab(self):
        assert self.is_element_present(
            *HousePageLocators.ADD_PREMISE), "Button 'Добавить помещение' is not present"
        assert self.is_element_present(
            *HousePageLocators.TITLE_NAME), "Title 'Название' is not present"

    def open_add_premise(self):
        wd = self.app.wd
        wd.find_element(*HousePageLocators.ADD_PREMISE).click()

    def open_edit_premise(self):
        wd = self.app.wd
        wd.find_element(*HousePageLocators.ADD_PREMISE).click()

    def add_premise(self, name):
        wd = self.app.wd
        self.open_add_premise()
        self.change_field_value(*HousePageLocators.ADD_PREMISE_NAME_INPUT, name)
        wd.find_element(*HousePageLocators.SAVE_BUTTON).click()

    def should_be_add_premise_appearance(self):
        wd = self.app.wd
        assert HousePageLocators.ADD_PREMISE_URL in wd.current_url
        assert self.is_element_present(
            *HousePageLocators.SAVE_BUTTON), "Button 'Сохранить' is not present"
        assert self.is_element_present(
            *HousePageLocators.CANCEL_BUTTON), "Button 'Отменить' is not present"
        assert self.is_element_present(
            *HousePageLocators.ADD_PREMISE_TITLE), "Title 'Новое помещение' is not present"
        assert self.is_element_present(
            *HousePageLocators.ADD_PREMISE_NAME_INPUT), "Name input is not present"

    def find_premise_by_name(self, name):
        wd = self.app.wd
        assert self.is_element_present(
            By.XPATH, "//a[contains(text(),'"+name+"')]"), "Added premise is not present"

    def open_premise_to_edit_by_editlink(self, premise, name):
        wd = self.app.wd
        # отрезаем от ссылки домен
        premise.editLink = premise.editLink[29:]
        wd.find_element(By.XPATH, '//a[@href="' + premise.editLink + '"]').click()
        time.sleep(3)
        self.change_field_value(*HousePageLocators.ADD_PREMISE_NAME_INPUT, name)
        wd.find_element(*HousePageLocators.SAVE_BUTTON).click()

    def delete_premise(self, premise):
        wd = self.app.wd
        # отрезаем от ссылки домен
        premise.deleteLink = premise.deleteLink[29:]
        wd.find_elements(By.XPATH, '//a[@href="' + premise.deleteLink + '"]')[2].click()
        alert = wd.switch_to_alert()
        alert.accept()

    def get_premise_list(self):
        wd = self.app.wd
        premise = []
        for i in range(len(wd.find_elements(*HousePageLocators.PREMISE_ROW))):
            name = wd.find_elements(By.CSS_SELECTOR, "td:nth-child(2) a")[i].text
            deleteLink = wd.find_elements(By.CSS_SELECTOR, "[data-method='delete']")[i].get_attribute("href")
            editLink = wd.find_elements(By.CSS_SELECTOR, ".action-link:nth-child(2)")[i].get_attribute("href")
            premise.append(Premise(name=name, deleteLink=deleteLink, editLink=editLink))
        return premise

    def open_single_premise(self, premise):
        wd = self.app.wd
        # отрезаем от ссылки домен
        premise.deleteLink = premise.deleteLink[29:]
        wd.find_elements(By.XPATH, '//a[@href="' + premise.deleteLink + '"]')[1].click()
        time.sleep(3)

    def should_be_single_premise(self):
        assert self.is_element_present(
            By.XPATH, "//span[contains(text(),'Название')]"), "'Название' is not present"
        assert self.is_element_present(By.XPATH, "//*[contains(text(),'Доступ к квартирам: ')]"), "'Доступ к квартирам:' is not present"
        assert self.is_element_present(
            By.XPATH, "//*[contains(text(),'Доступ к машиноместам:')]"), "'Доступ к машиноместам:' is not present"
        assert self.is_element_present(
            By.XPATH, "//*[contains(text(),'Доступ к кладовкам:')]"), "'Доступ к кладовкам:' is not present"
        assert self.is_element_present(
            By.XPATH, "//*[contains(text(),'Bkfn numbers:')]"), "'Bkfn numbers:' is not present"
        assert self.is_element_present(
            By.XPATH, "//*[contains(text(),'Домофоны')]"), "'Домофоны' is not present"
        assert self.is_element_present(
            By.XPATH, "//*[contains(text(),'Модель')]"), "'Модель' is not present"
        assert self.is_element_present(
            By.XPATH, "//button[contains(text(),'Добавить')]"), "Button 'Добавить' is not present"

#Property tabs
    def property_tab_appearance(self):
        assert self.is_element_present(
            *HousePageLocators.FLOOR_TITLE), "Title 'Этаж' is not present"
        assert self.is_element_present(
            *HousePageLocators.FLOOR_CONTAINER), "Container 'Этаж' is not present"
        assert self.is_element_present(
            *HousePageLocators.ENTRANCE_TITLE), "Title 'Подъезд' is not present"
        assert self.is_element_present(
            *HousePageLocators.ENTRANCE_CONTAINER), "Container 'Подъезд' is not present"
        assert self.is_element_present(
            *HousePageLocators.KEYS_TITLE), "Title 'Ключи' is not present"
        assert self.is_element_present(
            *HousePageLocators.KEYS_CONTAINER), "Container 'Ключи' is not present"
        assert self.is_element_present(
            *HousePageLocators.DEVICES_TITLE), "Title 'Устройства' is not present"
        assert self.is_element_present(
            *HousePageLocators.DEVICES_CONTAINER), "Container 'Устройства' is not present"
        assert self.is_element_present(
            *HousePageLocators.STATUS_TITLE), "Title 'Статус ЛС' is not present"
        assert self.is_element_present(
            *HousePageLocators.STATUS_CONTAINER), "Container 'Статус ЛС' is not present"
        assert self.is_element_present(
            *HousePageLocators.GROUP_CHANGES_BUTTON), "Button 'Групповые изменения' is not present"
        assert self.is_element_present(
            *HousePageLocators.SYNC_BUTTON), "Button 'Синхронизация' is not present"
        assert self.is_element_present(
            *HousePageLocators.IMPORT_BUTTON), "Button 'Импорт' is not present"

    def delete_property_by_number(self, number):
        wd = self.app.wd
        for i in range(len(wd.find_elements(*HousePageLocators.CELL_WITH_PROPERTY_NUMBER))):
            property_number = wd.find_elements(*HousePageLocators.CELL_WITH_PROPERTY_NUMBER)[i].text
            if property_number == number:
                wd.find_elements(*HousePageLocators.DELETE_PROPERTY_ROW)[i].click()
                alert = wd.switch_to_alert()
                alert.accept()
                time.sleep(2)
                return

    def property_with_number_exist(self, number):
        wd = self.app.wd
        for i in range(len(wd.find_elements(*HousePageLocators.CELL_WITH_PROPERTY_NUMBER))):
            property_number = wd.find_elements(*HousePageLocators.CELL_WITH_PROPERTY_NUMBER)[i].text
            if property_number == number:
                return 1



#Flat tab
    def open_flat_tab(self, url):
        wd = self.app.wd
        self.open_house_page_by_url(url)
        wd.find_element(*HousePageLocators.HOUSE_FLATS_TAB).click()
        time.sleep(3)

    def should_be_flat_tab(self):
        wd = self.app.wd
        self.property_tab_appearance()
        assert self.is_element_present(
            *HousePageLocators.NEW_FLATS_BUTTON), "Button 'Добавить квартиру' is not present"
        assert HousePageLocators.FLAT_TAB_URL in wd.current_url

    def create_flat_with_number(self, number):
        wd = self.app.wd
        self.delete_property_by_number(number)
        wd.find_element(*HousePageLocators.NEW_FLATS_BUTTON).click()
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, "#apartment_section")))
        self.change_field_value(*HousePageLocators.APARTMENT_SECTION, 1)
        self.change_field_value(*HousePageLocators.APARTMENT_PROPERTY_NUMBER, number)
        wd.find_element(*HousePageLocators.SAVE_BUTTON).click()


#parking tab
    def open_parking_tab(self, url):
        wd = self.app.wd
        self.open_house_page_by_url(url)
        wd.find_element(*HousePageLocators.HOUSE_PARKING_TAB).click()
        time.sleep(3)

    def should_be_parking_tab(self):
        wd = self.app.wd
        self.property_tab_appearance()
        assert self.is_element_present(
            *HousePageLocators.NEW_PARKING_BUTTON), "Button 'Добавить машиноместо' is not present"
        assert HousePageLocators.PARKING_TAB_URL in wd.current_url

    def create_parking_with_number(self, number):
        wd = self.app.wd
        self.delete_property_by_number(number)
        wd.find_element(*HousePageLocators.NEW_PARKING_BUTTON).click()
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, "#parking_place_section")))
        self.change_field_value(*HousePageLocators.PARKING_SECTION, 1)
        self.change_field_value(*HousePageLocators.PARKING_PROPERTY_NUMBER, number)
        wd.find_element(*HousePageLocators.SAVE_BUTTON).click()

#Storage tab
    def open_storage_tab(self, url):
        wd = self.app.wd
        self.open_house_page_by_url(url)
        wd.find_element(*HousePageLocators.HOUSE_STORE_TAB).click()
        time.sleep(3)

    def should_be_storage_tab(self):
        wd = self.app.wd
        self.property_tab_appearance()
        assert self.is_element_present(
            *HousePageLocators.NEW_STORAGE_BUTTON), "Button 'Добавить кладовку' is not present"
        assert HousePageLocators.STORAGE_TAB_URL in wd.current_url

    def create_storage_with_number(self, number):
        wd = self.app.wd
        self.delete_property_by_number(number)
        wd.find_element(*HousePageLocators.NEW_STORAGE_BUTTON).click()
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, "#storeroom_section")))
        self.change_field_value(*HousePageLocators.STORAGE_SECTION, 1)
        self.change_field_value(*HousePageLocators.STORAGE_PROPERTY_NUMBER, number)
        wd.find_element(*HousePageLocators.SAVE_BUTTON).click()

# BKFN tab
    def open_bkfn_tab(self, url):
        wd = self.app.wd
        self.open_house_page_by_url(url)
        wd.find_element(*HousePageLocators.HOUSE_BKFN_TAB).click()
        time.sleep(3)

    def should_be_bkfn_tab(self):
        wd = self.app.wd
        assert self.is_element_present(
            *HousePageLocators.NEW_BKFN_BUTTON), "Button 'Добавить БКФН' is not present"
        assert HousePageLocators.BKFN_TAB_URL in wd.current_url

    def create_bkfn_with_number(self, number):
        wd = self.app.wd
        self.delete_property_by_number(number)
        wd.find_element(*HousePageLocators.NEW_BKFN_BUTTON).click()
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, "#bkfn_section")))
        self.change_field_value(*HousePageLocators.BKFN_SECTION, 1)
        self.change_field_value(*HousePageLocators.BKFN_PROPERTY_NUMBER, number)
        wd.find_element(*HousePageLocators.SAVE_BUTTON).click()

#Intercom tab
#Appearance
    def open_intercom_tab(self, url):
        wd = self.app.wd
        self.open_house_page_by_url(url)
        wd.find_element(*HousePageLocators.HOUSE_INTERCOM_TAB).click()
        time.sleep(3)
        #wd.save_screenshot('intercom_page.png')

    def should_be_intercom_tab(self):
        wd = self.app.wd
        assert HousePageLocators.INTERCOM_TAB_URL in wd.current_url
        assert self.is_element_present(
            *HousePageLocators.TERRITORY_TITLE), "Title 'Территории' is not present"
        assert self.is_element_present(
            *HousePageLocators.TERRITORY_ADD_INTERCOM), "Add intercom button in block 'Территории' is not present"
        assert self.is_element_present(
            *HousePageLocators.AROUND_TERRITORY_TITLE), "Title 'Придомовая территория' is not present"
        assert self.is_element_present(
            *HousePageLocators.AROUND_TERRITORY_ADD_INTERCOM), "Add intercom button in block 'Придомовая территория' is not present"
        assert self.is_element_present(
            *HousePageLocators.ENTRANCE_TITLE_INTERCOM), "Title 'Подъезд' is not present"
        assert self.is_element_present(
            *HousePageLocators.ENTRANCE_ADD_INTERCOM), "Add intercom button in block 'Подъезд' is not present"
        assert self.is_element_present(
            *HousePageLocators.FLOOR_TITLE_INTERCOM), "Title 'Этаж' is not present"
        assert self.is_element_present(
            *HousePageLocators.FLOOR_ADD_INTERCOM), "Add intercom button in block  'Этаж' is not present"
        assert self.is_element_present(
            *HousePageLocators.TECH_TITLE_INTERCOM), "Title 'Тех.помещение' is not present"
        assert self.is_element_present(
            *HousePageLocators.TECH_ADD_INTERCOM), "Add intercom button in block 'Тех.помещение' is not present"

# Add intercom
    def should_be_add_intercom(self):
        assert self.is_element_present(
            *HousePageLocators.MODEL_CONTAINER), "Title 'Территории' is not present"

    def open_territory_intercom(self):
        wd = self.app.wd
        wd.find_element(*HousePageLocators.TERRITORY_ADD_INTERCOM).click()
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, "#intercom_human_name")))

    def open_around_territory_intercom(self):
        wd = self.app.wd
        wd.find_element(*HousePageLocators.AROUND_TERRITORY_ADD_INTERCOM).click()
        WebDriverWait(wd, 30).until(EC.presence_of_element_located
                                    ((By.CSS_SELECTOR, "#intercom_human_name")))

    def fill_intercom(self, intercom):
        wd = self.app.wd
        wd.find_element(*HousePageLocators.MODEL_CONTAINER).click()
        wd.find_element(*HousePageLocators.SELECT_SEARCH).send_keys(intercom.model + Keys.ENTER)
        wd.find_element(*HousePageLocators.TERRITORY_CONTAINER).click()
        time.sleep(1)
        wd.find_element(*HousePageLocators.TERRITORY_INPUT).send_keys(intercom.territory + Keys.ENTER)
        self.change_field_value(*HousePageLocators.INTERCOM_NAME, intercom.name)
        self.change_field_value(*HousePageLocators.INTERCOM_HUMAN_NAME, intercom.human_name)
        self.change_field_value(*HousePageLocators.INTERCOM_IP, intercom.ip)
        self.change_field_value(*HousePageLocators.INTERCOM_PASSWORD, intercom.password)
        wd.find_element(*HousePageLocators.SAVE_BUTTON).click()
