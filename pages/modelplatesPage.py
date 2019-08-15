"""
------------------------------------
@Time : 2019/7/13 19:55
@Auth : linux超
@File : loginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH
from selenium.webdriver.support.select import Select
import time

class ModelplatesPage(Base):

    locator = ParseConfig(LOCATOR_PATH)
    modelplatesurl = locator('TestUrl','modelplatesurl')
    indexurl = locator('TestUrl', 'indexurl')
    add_model_btn = locator('ModelplatesPage', 'add_model_btn')  # 新增模板按钮
    add_model_name = locator('ModelplatesPage', 'add_model_name') #模板名称
    first_categoryname = locator('ModelplatesPage', 'first_categoryname')
    second_categoryname = locator('ModelplatesPage', 'second_categoryname')
    save_model_btn = locator('ModelplatesPage', 'save_model_btn')
    model_names = locator('ModelplatesPage', 'model_names')
    add_model_key = locator('ModelplatesPage', 'add_model_key')
    add_key_name = locator('ModelplatesPage', 'add_key_name')
    key_type = locator('ModelplatesPage', 'key_type')
    key_sort = locator('ModelplatesPage', 'key_sort')
    save_key_btn = locator('ModelplatesPage', 'save_key_btn')
    logout_btn = locator('LoginPage', 'logout_btn')  # 登出按钮



    def open_model_plates_url(self):
        self.open(self.modelplatesurl)
    def open_index_url(self):
        self.open(self.indexurl)

################################# 新增配置模板 ############################################
    @property
    def new_model(self):
        """新增模板按钮"""
        return self.find_element(*self.add_model_btn)

    def click_new_model(self):
        """点击新增模板按钮"""
        self.logger.info("点击新增模板按钮")
        self.new_model.click()

    def input_model_name(self,model_name):
        """输入模板名称"""
        self.logger.info("输入模板名称：{}".format(model_name))
        action = self.move_to_element_click(*self.add_model_name)
        self.send_keys(*self.add_model_name,model_name)
        action.release().perform()


    def choose_catrgory_name1(self,firstservice_name):
        self.logger.info("正在选择一级品目：{}".format(firstservice_name))
        Select(self.find_element(*self.first_categoryname)).select_by_visible_text(firstservice_name)

    def choose_catrgory_name2(self, secondservice_name):
        self.logger.info("正在选择二级品目：{}".format(secondservice_name))
        Select(self.find_element(*self.second_categoryname)).select_by_visible_text(secondservice_name)

    def click_save_model(self,model_name):
        self.logger.info("正在保存配置模板：{}".format(model_name))
        self.click(*self.save_model_btn)
        self.logger.info("保存配置模板：{}成功".format(model_name))

################################# 新增模板KEY ############################################

    def modelsetting_btn(self):
        return self.find_elements(*self.model_names)[0]

    def click_modelsetting_btn(self):
        self.modelsetting_btn().click()
        self.logger.info("进入模板字段配置成功")

    def click_add_model_key(self):
        self.click(*self.add_model_key)

    def input_key_name(self,key_name):
        """输入模板KEY名称"""
        self.logger.info("输入模板KEY名称：{}".format(key_name))
        action = self.move_to_element_click(*self.add_key_name)
        self.send_keys(*self.add_key_name,key_name)
        action.release().perform()

    def select_key_type(self,key_typename):
        self.logger.info("正在选择KEY类型：{}".format(key_typename))
        Select(self.find_element(*self.key_type)).select_by_visible_text(key_typename)

    def input_key_sort(self,key_sortnum):
        action = self.move_to_element_click(*self.key_sort)
        self.send_keys(*self.key_sort,key_sortnum)
        action.release().perform()
        self.logger.info("选择KEY排序：{}".format(key_sortnum))

    def click_save_key_btn(self,key_name):
        self.click(*self.save_key_btn)
        self.logger.info("KEY：{}保存成功".format(key_name))

    def click_log_out_btn(self):
        self.click(*self.logout_btn)
        self.logger.info("登出成功")