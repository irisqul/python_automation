from model.district import District
import random
import time


def test_delete_district(app):
    test_district = District(name="Test", address="Москва")
    # allure.step('Открыть вкладку "Район"')
    app.district_page.open_district_page()
    if len(app.district_page.locate_districts_by_name(test_district)) == 0:
        app.district_page.open_add_new_district_page()
        app.district_page.create_district(test_district)
    old_districts = app.district_page.get_districts_list()
    # allure.step('Выбрать для удаления случайный тестовый район')
    test_districts = app.district_page.locate_districts_by_name(test_district)
    district = random.choice(test_districts)
    # allure.step('Нажать иконку удаления у выбранного района')
    app.district_page.delete_district_by_delete_link(district)
    time.sleep(10)
    new_districts = app.district_page.get_districts_list()
    # allure.step('Количество районов уменьшилось на один')
    assert len(old_districts) - 1 == len(new_districts)
    assert len(test_districts) - 1 == len(app.district_page.locate_districts_by_name(test_district))




