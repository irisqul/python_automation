import pytest
import json
import os.path
from fixture.application import Application


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    wd = item.funcargs['app'].wd
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(wd.current_url))
        screenshot = wd.get_screenshot_as_base64()
        extra.append(pytest_html.extras.image(screenshot, ''))
        xfail = hasattr(report, 'wasxfail')
        #if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            #extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
            # screenshot = wd.get_screenshot_as_base64()
            # extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")