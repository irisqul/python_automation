from model.locators import KeyPageLocators
import time

def test_open_key_page(app):
    app.key_page.open_key_page()
    time.sleep(3)
    app.key_page.key_elements_are_present()

#Testing search input
def test_perform_search(app):
    text = "2989837468"
    app.key_page.open_key_page()
    app.key_page.perform_search(text)
    app.key_page.search_result_are_present(text)

def test_perform_search_nothing_found(app):
    text = "298983746832-387387"
    app.key_page.open_key_page()
    app.key_page.perform_search(text)
    app.key_page.search_result_nothing_found_is_present()

#Service key
def test_service_key_appearance_direct_open(app):
    url = KeyPageLocators.SERVICE_KEY_URL
    app.key_page.open_page_by_url(url)
    app.key_page.should_be_service_key_page()

def test_service_key_appearance_open_from_district(app):
    url = KeyPageLocators.DISTRICT_URL
    app.key_page.open_service_key_page(url)
    app.key_page.should_be_service_key_page()


# def test_import_key_page(app):
#     pass