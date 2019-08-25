"""
------------------------------------
@Time : 2019/7/23 20:22
@Auth : linux超
@File : conftest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest

from pages.loginPage import LoginPage
from pages.modelplatesPage import ModelplatesPage
from datas.modelplates_datas import ModelplatesData
from pages.newprojectPage import NewprojectPage
from datas.newproject_datas import NewprojectData


from selenium import webdriver
from py._xmlgen import html
from common.record_log import logger

_driver = None



# 测试失败时添加截图和测试用例描述(用例的注释信息)
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Description'))
#     cells.insert(2, html.th('Test_nodeid'))
#     cells.pop(2)
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)


def _capture_screenshot():
    """
    截图保存为base64
    :return:
    """
    return _driver.get_screenshot_as_base64()


@pytest.fixture(scope='session')
def driver():
    global _driver
    if _driver is None:
        logger.info('------------open browser------------')
        _driver = webdriver.Firefox()
        # _driver.maximize_window()
    yield _driver
    logger.info('------------close browser------------')
    _driver.quit()









@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    modelplates_page = ModelplatesPage(driver)
    newproject_page = NewprojectPage(driver)
    yield driver, login_page,modelplates_page,newproject_page
#
#
# test_login.py调用
@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    login_page.open_url()
    yield login_page
    driver.delete_all_cookies()

# @pytest.fixture(scope='function')
# def login(ini_pages):
#     driver, login_page, home_page, loan_page, member_page = ini_pages
#     login_page.open_url()
#     login_page.login(InvestData.user_password['phone'],
#                      InvestData.user_password['pwd'])
#     yield login_page, home_page, loan_page, member_page
#     driver.delete_all_cookies()

# test_login.py调用
@pytest.fixture(scope='function')
def login(ini_pages):
    driver, login_page, modelplates_page,newproject_page= ini_pages
    login_page.open_url()
    login_page.login(ModelplatesData.user_password['username'],
                     ModelplatesData.user_password['password'])

    yield login_page,modelplates_page,newproject_page
    driver.delete_all_cookies()

# # test_modelplates.py调用   (适用范围不一样)
# @pytest.fixture(scope='class')
# def login_modelplates(ini_pages):
#     driver, login_page, modelplates_page = ini_pages
#     login_page.open_url()
#     login_page.login(ModelplatesData.user_password['username'],
#                      ModelplatesData.user_password['password'])
#
#     yield login_page,modelplates_page
#     driver.delete_all_cookies()

# # 继承
# # test_modelplates.py调用


@pytest.fixture(scope='function')
def login_cgr(ini_pages):
    driver, login_page, modelplates_page,newproject_page= ini_pages
    login_page.open_url()
    login_page.login(NewprojectData.user_password['username'],
                     NewprojectData.user_password['password'])

    yield login_page,modelplates_page,newproject_page
    driver.delete_all_cookies()




