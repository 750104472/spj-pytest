"""
------------------------------------
@Time : 2019/7/13 20:01
@Auth : linux超
@File : test_login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest

from datas.modelplates_datas import ModelplatesData
from datas.newproject_datas import NewprojectData
from common.record_log import logger
import pdb


class TestModelplates(object):
    """登录测试用例"""
    logger = logger
    t_data = ModelplatesData
    p_data = NewprojectData

    @pytest.mark.parametrize('model_name, firstservice_name, secondservice_name', t_data.add_model_nums)
    def test_add_modelplates(self,login,model_name,firstservice_name,secondservice_name):
        """登录:登录成功"""
        modelplates_page = login[1]
        """新增配置模板页面"""
        modelplates_page.open_model_plates_url()
        modelplates_page.click_new_model()        # 点击新增配置模板
        modelplates_page.input_model_name(model_name)        # 输入配置模板名称
        modelplates_page.choose_catrgory_name1(firstservice_name)        # 选择一级品目
        modelplates_page.choose_catrgory_name2(secondservice_name)        # 选择二级品目
        modelplates_page.click_save_model(model_name)        # 保存模板




    @pytest.mark.parametrize('key_name, key_typename, key_sortnum', t_data.add_key_nums)
    def test_add_modelkeys(self, login, key_name, key_typename,key_sortnum):
        """登录:登录成功"""
        modelplates_page = login[1]
        """新增配置模板页面"""
        modelplates_page.open_model_plates_url()
        modelplates_page.click_modelsetting_btn()  # 点击配置模板字段按钮
        modelplates_page.click_add_model_key()
        modelplates_page.input_key_name(key_name)
        modelplates_page.select_key_type(key_typename)
        modelplates_page.input_key_sort(key_sortnum)
        modelplates_page.click_save_key_btn(key_name)

    # 采购人新增项目
    @pytest.mark.parametrize('username, password', p_data.cgr_account)
    @pytest.mark.parametrize('model_name, firstservice_name, secondservice_name', t_data.add_model_nums)
    @pytest.mark.parametrize('projectname, user_name, userphone,budgetamount,serviceperiod,file_path', p_data.add_project_nums)
    def test_add_project(self, open_url,inherit, username, password,model_name,firstservice_name,secondservice_name,
                         projectname,user_name, userphone,budgetamount,serviceperiod,file_path):
        login_page = open_url
        login_page.login(username,password)
        newproject_page = inherit[2]
        newproject_page.open_newprojecturl()
        newproject_page.input_project_name(projectname)
        newproject_page.choose_procurement_category_level1(firstservice_name)
        newproject_page.choose_procurement_category_level2(secondservice_name)
        newproject_page.input_user(user_name)
        newproject_page.input_user_phone(userphone)
        newproject_page.click_address()
        newproject_page.click_invoice()
        newproject_page.input_budget_amount(budgetamount)
        newproject_page.input_service_period(serviceperiod)
        newproject_page.click_Attachment_click()
        newproject_page.send_Attachment_file(file_path)
        newproject_page.click_save_next()






