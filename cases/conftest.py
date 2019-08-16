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




