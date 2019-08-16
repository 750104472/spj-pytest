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
from datas.modelplates_datas import ModelplatesData

class NewprojectPage(Base):

    locator = ParseConfig(LOCATOR_PATH)
    newprojecturl = locator('TestUrl','newprojecturl')
    project_name = locator('NewprojectPage', 'project_name')
    procurement_category_level1 = locator('NewprojectPage', 'procurement_category_level1')
    procurement_category_level2 = locator('NewprojectPage', 'procurement_category_level2')
    user = locator('NewprojectPage', 'user')
    user_phone = locator('NewprojectPage', 'user_phone')
    address = locator('NewprojectPage', 'address')
    invoice = locator('NewprojectPage', 'invoice')
    budget_amount = locator('NewprojectPage', 'budget_amount')
    service_period = locator('NewprojectPage', 'service_period')
    Attachment_click = locator('NewprojectPage', 'Attachment_click')
    Attachment_file = locator('NewprojectPage', 'Attachment_file')
    save_next = locator('NewprojectPage', 'save_next')
    descripefield = locator('NewprojectPage', 'descripefield')
    descripetext = locator('NewprojectPage', 'descripetext')
    save_project_btn = locator('NewprojectPage', 'save_project_btn')


    def open_newprojecturl(self):
        self.open(self.newprojecturl)

    def input_project_name(self,projectname):
        """输入项目名称"""
        self.logger.info("输入项目名称：{}".format(projectname))
        action = self.move_to_element_click(*self.project_name)
        self.send_keys(*self.project_name,projectname)
        action.release().perform()

    def choose_procurement_category_level1(self,category_level1_name):
        self.logger.info("正在选择一级品目：{}".format(category_level1_name))
        Select(self.find_element(*self.procurement_category_level1)).select_by_visible_text(category_level1_name)

    def choose_procurement_category_level2(self, category_level2_name):
        self.logger.info("正在选择二级品目：{}".format(category_level2_name))
        Select(self.find_element(*self.procurement_category_level2)).select_by_visible_text(category_level2_name)

    def input_user(self,user_name):

        self.logger.info("输入联系人：{}".format(user_name))
        action = self.move_to_element_click(*self.user)
        self.send_keys(*self.user, user_name)
        action.release().perform()

    def input_user_phone(self,userphone):

        self.logger.info("输入联系人：{}".format(userphone))
        action = self.move_to_element_click(*self.user_phone)
        self.send_keys(*self.user_phone, userphone)
        action.release().perform()

    def click_address(self):
        self.click(*self.address)
        self.logger.info("选择服务地址成功")

    def click_invoice(self):
        self.click(*self.invoice)
        self.logger.info("选择发票成功")

    def input_budget_amount(self,budgetamount):

        self.logger.info("输入预算金额：{}".format(budgetamount))
        action = self.move_to_element_click(*self.budget_amount)
        self.send_keys(*self.budget_amount, budgetamount)
        action.release().perform()

    def input_service_period(self,serviceperiod):

        self.logger.info("输入服务周期：{}".format(serviceperiod))
        action = self.move_to_element_click(*self.service_period)
        self.send_keys(*self.service_period, serviceperiod)
        action.release().perform()

    def click_Attachment_click(self):
        self.click(*self.Attachment_click)
        self.logger.info("点开附件按钮成功")

    def send_Attachment_file(self,file_path):
        self.send_keys(*self.Attachment_file,file_path)
        self.logger.info("上传附件成功")

    def click_save_next(self):
        self.click(*self.save_next)
        self.logger.info("项目暂存成功")

    def find_descripe_fields(self):
        eles = self.find_elements(*self.descripefield)
        self.logger.info("获取到多个需求描述字段元素")
        return eles

    def find_descripe_texts(self):
        eles = self.find_elements(*self.descripetext)
        self.logger.info("获取到多个需求描述字段输入框元素")
        return eles

    def click_save_project(self):
        self.click(*self.save_project_btn)
        self.logger.info("点击保存项目按钮成功")

    def switch_to_alert(self):
        self.accept_alert()
        self.logger.info("提交项目成功")


