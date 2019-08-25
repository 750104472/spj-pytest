from api.SchoolTeacherLib import SchoolTeacherLib
import cfg
import pytest
import pdb
from common.record_log import logger
from datas.schoolteacherlib_datas import SchoolteacherlibData

sc = SchoolTeacherLib()
st_data = SchoolteacherlibData
class TestTeacher(object):
    @pytest.mark.parametrize("username,realname,subjectid,phonenumber,email,idcardnumber",st_data.add_school_teacher_data)
    def test_addteacher1(self,f_add_school_class,username,realname,subjectid,phonenumber,email,idcardnumber):
        """tc001001"""
        bodyDict = sc.add_school_teacher(username,realname,subjectid,f_add_school_class,phonenumber,email,idcardnumber)
        assert bodyDict['retcode'] == 0
        studentlist = sc.list_school_teacher()['retlist']
        sc.teacherlist_should_contain(studentlist,username,realname,bodyDict['id'],f_add_school_class,phonenumber,email,idcardnumber)
        sc.delete_school_teacher(bodyDict['id'])

    @pytest.mark.parametrize("username,realname,subjectid,phonenumber,email,idcardnumber",st_data.add_school_teacher_data2)
    def test_addteacher2(self,f_add_school_class,f_add_school_teacher,username,realname,subjectid,phonenumber,email,idcardnumber):
        """tc001002"""
        bodyDict = sc.add_school_teacher(username, realname, subjectid, f_add_school_class, phonenumber, email,idcardnumber)
        assert bodyDict['retcode'] == 0

    @pytest.mark.parametrize("username,realname,subjectid,phonenumber,email,idcardnumber",st_data.add_school_teacher_data3)
    def test_addteacher3(self,f_add_school_class,f_add_school_teacher,username,realname,subjectid,phonenumber,email,idcardnumber):
        """tc001003"""
        bodyDict = sc.add_school_teacher(username, realname, subjectid, f_add_school_class, phonenumber, email,idcardnumber)
        assert bodyDict['retcode'] == 1
        assert bodyDict['reason'] == f"登录名 {username} 已经存在"

