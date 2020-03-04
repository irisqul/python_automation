import time
import random
from model.house import House
from model.locators import HousePageLocators
from model.district import District
import string

def test_open_house(app):
    district = District(link="/buildings")
    app.house_page.open_house_page(district)
    app.house_page.should_be_tabs_at_house_page()

def test_open_house_by_url(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_house_page_by_url(url)
    app.house_page.should_be_tabs_at_house_page()
    app.house_page.should_be_info_tab()

def test_technical_tab_appearence(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_tech_tab(url)
    app.house_page.should_be_tabs_at_house_page()
    app.house_page.should_be_tech_tab()

def test_technical_tab_add_premise_appearence(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_tech_tab(url)
    app.house_page.open_add_premise()
    app.house_page.should_be_add_premise_appearance()

def test_technical_tab_add_premise(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_tech_tab(url)
    random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    old_premise_list = app.house_page.get_premise_list()
    app.house_page.add_premise(random_name)
    time.sleep(3)
    app.house_page.find_premise_by_name(random_name)
    new_premise_list = app.house_page.get_premise_list()
    assert len(old_premise_list) + 1 == len(new_premise_list)

def test_technical_tab_edit_premise(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_tech_tab(url)
    random_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    old_premise_list = app.house_page.get_premise_list()
    premise = random.choice(old_premise_list)
    app.house_page.open_premise_to_edit_by_editlink(premise, random_name)
    app.house_page.find_premise_by_name(random_name)
    new_premise_list = app.house_page.get_premise_list()
    assert len(old_premise_list) == len(new_premise_list)

def test_technical_tab_delete_premise(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_tech_tab(url)
    old_premise_list = app.house_page.get_premise_list()
    premise = random.choice(old_premise_list)
    app.house_page.delete_premise(premise)
    time.sleep(3)
    new_premise_list = app.house_page.get_premise_list()
    assert len(old_premise_list) - 1 == len(new_premise_list)

def test_technical_tab_single_premise(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_tech_tab(url)
    old_premise_list = app.house_page.get_premise_list()
    premise = random.choice(old_premise_list)
    app.house_page.open_single_premise(premise)
    time.sleep(3)
    app.house_page.should_be_single_premise()
    app.house_page.should_be_tabs_at_house_page()

#flat tab
def test_flat_tab_appearance(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_flat_tab(url)
    app.house_page.should_be_flat_tab()

def test_create_flat(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_flat_tab(url)
    app.house_page.create_flat_with_number(number)
    assert app.house_page.property_with_number_exist(number) == 1

def test_delete_flat(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_flat_tab(url)
    if app.house_page.property_with_number_exist(number) != 1:
        app.house_page.create_flat_with_number(number)
    app.house_page.delete_property_by_number(number)
    time.sleep(2)
    assert app.house_page.property_with_number_exist(number) != 1

#parking tab
def test_parking_tab_appearance(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_parking_tab(url)
    app.house_page.should_be_parking_tab()

def test_create_parking(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_parking_tab(url)
    app.house_page.create_parking_with_number(number)
    assert app.house_page.property_with_number_exist(number) == 1

def test_delete_parking(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_parking_tab(url)
    if app.house_page.property_with_number_exist(number) != 1:
        app.house_page.create_parking_with_number(number)
    app.house_page.delete_property_by_number(number)
    time.sleep(2)
    assert app.house_page.property_with_number_exist(number) != 1

# Storage tab
def test_storage_tab_appearance(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_storage_tab(url)
    app.house_page.should_be_storage_tab()

def test_create_storage(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_storage_tab(url)
    app.house_page.create_storage_with_number(number)
    assert app.house_page.property_with_number_exist(number) == 1

def test_delete_storage(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_storage_tab(url)
    if app.house_page.property_with_number_exist(number) != 1:
        app.house_page.create_storage_with_number(number)
    app.house_page.delete_property_by_number(number)
    time.sleep(2)
    assert app.house_page.property_with_number_exist(number) != 1

#BKFN tab
def test_bkfn_tab_appearance(app):
    url = HousePageLocators.HOUSE_URL
    app.house_page.open_bkfn_tab(url)
    app.house_page.should_be_bkfn_tab()

def test_create_bkfn(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_bkfn_tab(url)
    app.house_page.create_bkfn_with_number(number)
    assert app.house_page.property_with_number_exist(number) == 1

def test_delete_bkfn(app):
    url = HousePageLocators.HOUSE_URL
    number = "1"
    app.house_page.open_bkfn_tab(url)
    if app.house_page.property_with_number_exist(number) != 1:
        app.house_page.create_bkfn_with_number(number)
    app.house_page.delete_property_by_number(number)
    time.sleep(2)
    assert app.house_page.property_with_number_exist(number) != 1

