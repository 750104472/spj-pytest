from api.SchoolClassLib import SchoolClassLib
from datas.schoolclasslib_datas import SchoolclasslibData
import pytest
import pdb
from common.record_log import logger

sc = SchoolClassLib()
c_data = SchoolclasslibData
class TestClass(object):
    @pytest.mark.tc000001
    @pytest.mark.parametrize("gradeid,name,studentlimit",c_data.add_school_class_data)
    def test_addclass1(self,gradeid,name,studentlimit):
        bodyDict = sc.add_school_class(gradeid,name,studentlimit)
        assert bodyDict["retcode"]==0
        logger.info(f'添加班级：{gradeid, name, studentlimit}成功')
        result = sc.list_school_class(gradeid)
        s_bodyDict = result['retlist'][0]
        assert s_bodyDict['id'] == bodyDict['id']
        assert s_bodyDict['invitecode'] == bodyDict['invitecode']
        sc.delete_school_class(bodyDict["id"])
        logger.info(f'删除班级：{gradeid, name, studentlimit}成功')

    def test_addclass2(self,f_add_school_class):
        bodyDict = sc.add_school_class(1, '七年级2班', 60)
        assert bodyDict['retcode']==0
        logger.info('添加班级：[1, 七年级2班, 60]成功')
        classlist = sc.list_school_class()
        sc.classlist_should_contain(classlist['retlist'],'七年级',bodyDict['id'],bodyDict['invitecode'],"七年级2班",60)
        sc.delete_school_class(bodyDict['id'])
        logger.info('删除班级：[1, 七年级2班, 60]成功')

    def test_addclass3(self,f_add_school_class):
        classlist_before = sc.list_school_class()
        bodyDict = sc.add_school_class(1,'七年级1班',60)
        assert bodyDict['retcode']==1
        assert bodyDict['reason']!="duplicated class name","实际失败原因与接口文档不一致"

        classlist_after = sc.list_school_class()
        assert classlist_before == classlist_after

    def test_modifyclass1(self,f_add_school_class):
        bodyDict = sc.modify_school_class(f_add_school_class,"啦啦啦",70)
        logger.info(f"修改id为{f_add_school_class}的班级，班级名称修改为'啦啦啦',人数修改为70")
        assert bodyDict['retcode'] == 0
        classlist_after = sc.list_school_class()['retlist'][0]
        assert classlist_after['name'] == "啦啦啦",f"列表内班级名称为{classlist_after['name']},与预期的班级名称：'啦啦啦'不一致"

    def test_modifyclass2(self,f_add_school_class):
        bodyDict = sc.add_school_class(1,"七年级2班",70)
        assert bodyDict['retcode'] == 0
        logger.info('添加班级：[1, 七年级2班, 60]成功')
        classlist_before = sc.list_school_class()
        modifyDict = sc.modify_school_class(bodyDict['id'],'七年级1班',60)
        logger.info(f"修改id为{bodyDict['id']}的班级，班级名称修改为'七年级1班',人数修改为60")
        assert modifyDict['retcode'] == 1
        assert modifyDict['reason'] == "duplicated class name"
        classlist_after = sc.list_school_class()
        assert classlist_before == classlist_after,f"修改失败后，列表返回内容发生了变化"
        sc.delete_school_class(bodyDict['id'])
        logger.info('删除班级：[1, 七年级2班, 60]成功')

    def test_modifyclass3(self,f_add_school_class):
        bodyDict = sc.modify_school_class(f_add_school_class+1,"啦啦啦",70)
        logger.info(f"修改id为{f_add_school_class+1}的班级，班级名称修改为'啦啦啦',人数修改为70")
        assert bodyDict['retcode'] == 404
        assert bodyDict['reason'] == f"id 为`{f_add_school_class+1}`的班级不存在"

    def test_deleteclass1(self,f_add_school_class):
        bodyDict = sc.delete_school_class(f_add_school_class+1)
        logger.info(f"删除id为{f_add_school_class+1}的班级")
        assert bodyDict['retcode'] == 404
        assert bodyDict['reason'] == f"id 为`{f_add_school_class+1}`的班级不存在"

    def test_deleteclass2(self,f_add_school_class):
        pdb.set_trace()
        bodyDict = sc.delete_school_class(f_add_school_class)
        logger.info(f"删除id为{f_add_school_class}的班级")
        assert bodyDict['retcode'] == 0
        classlist = sc.list_school_class()
        assert classlist['retlist'] == [],f"id 为`{f_add_school_class}`的班级仍然存在"
        logger.info("删除成功后，列表为空")
