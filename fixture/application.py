from selenium import webdriver
from fixture.session import SessionHelper
from fixture.district_page import DistrictPageHelper
from fixture.house_page import HousePageHelper
from fixture.key_page import KeyPageHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
             self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.district_page = DistrictPageHelper(self)
        self.house_page = HousePageHelper(self)
        self.key_page = KeyPageHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

