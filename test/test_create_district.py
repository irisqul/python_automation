from model.district import District

def test_district_page_appearance(app):
    district = District(name="Test", address="Москва")
    # allure.step('Открыть вкладку район')
    app.district_page.open_district_page()
    old_districts = app.district_page.get_districts_list()
    # allure.step('Нажать кнопку "Новый район"')
    app.district_page.open_add_new_district_page()
    # allure.step('Создать новый район')
    app.district_page.create_district(district)
    new_districts = app.district_page.get_districts_list()
    # allure.step('Общее количество районов увеличилось на один')
    assert len(old_districts) + 1 == len(new_districts)

