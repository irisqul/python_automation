import time
import random
from model.district import District

def test_district_page_appearance(app):
    app.district_page.open_district_page()
    app.district_page.should_be_table_with_districts()

def test_add_district_appearance(app):
    app.district_page.open_district_page()
    app.district_page.open_add_new_district_page()
    app.district_page.should_be_add_new_district_url()
    app.district_page.should_be_insert_fields()

def test_single_district_appearance_open_from_eye_icon(app):
    app.district_page.open_single_district_eye_icon()
    app.district_page.should_be_tabs_in_single_district_page()

def test_single_district_appearance_open_from_name_click(app):
    app.district_page.open_single_district_click_name_in_the_row()
    app.district_page.should_be_tabs_in_single_district_page()

def test_edit_district_appearance(app):
    test_district = District(name="Test", address="Москва")
    app.district_page.open_district_page()
    if len(app.district_page.locate_districts_by_name(test_district)) == 0:
        app.district_page.open_add_new_district_page()
        app.district_page.create_district(test_district)
    test_districts = app.district_page.locate_districts_by_name(test_district)
    district = random.choice(test_districts)
    app.district_page.open_edit_district_page_by_edit_link(district)
    time.sleep(4)

    app.district_page.should_be_edit_url(district)

def test_edit_district(app):
    test_district = District(name="Test", address="Москва")
    edited_district = District(name="Test1")
    app.district_page.open_district_page()
    if len(app.district_page.locate_districts_by_name(test_district)) == 0:
        app.district_page.open_add_new_district_page()
        app.district_page.create_district(test_district)
    test_districts = app.district_page.locate_districts_by_name(test_district)
    old_edited_districts = app.district_page.locate_districts_by_name(edited_district)
    district = random.choice(test_districts)
    app.district_page.open_edit_district_page_by_edit_link(district)
    time.sleep(4)
    app.district_page.edit_district_name(edited_district)
    assert len(app.district_page.locate_districts_by_name(edited_district)) - 1 == len(old_edited_districts)