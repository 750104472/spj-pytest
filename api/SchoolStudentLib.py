import requests,json
from cfg import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn
import logging

class  SchoolStudentLib:
    URL = "http://ci.ytesting.com/api/3school/students"

    def __init__(self):
        self.vcode = g_vcode


    def delete_school_student(self,studentid):
        payload = {
            'vcode'  : self.vcode,
        }

        url = '{}/{}'.format(self.URL,studentid)
        response = requests.delete(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def list_school_student(self):
        params = {
            'vcode':self.vcode,
            'action':'search_with_pagenation'
        }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        return bodyDict


    def add_school_student(self,username,realname,gradeid,classid,phonenumber,idSavedName=None):
        payload = {
            'vcode'  : self.vcode,
            'action' : 'add',
            'username'  : username,
            'realname'   : realname,
            'gradeid'  : gradeid,
            'classid' : classid,
            'phonenumber' : phonenumber
        }
        response = requests.post(self.URL,data=payload)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)

        if idSavedName:
            BuiltIn().set_global_variable('${%s}'%idSavedName,bodyDict['id'])
        return bodyDict

    def modify_school_student(self,studentid,realname=None,phonenumber=None):
        payload = {
            'vcode':self.vcode,
            'action':'modify'
        }
        if realname:
            payload['realname'] = realname
        if phonenumber:
            payload['phonenumber'] = phonenumber

        url='{}/{}'.format(self.URL,studentid)
        response = requests.put(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict

    def delete_all_school_students(self):
        # 先列出所有班级
        rd =  self.list_school_student()
        pprint(rd, indent=2)

        # 删除列出的所有班级
        for one in rd['retlist']:
            self.delete_school_student(one['id'])

        #再列出七年级所有班级
        rd =  self.list_school_student()
        pprint (rd,indent=2)

        # 如果没有删除干净，通过异常报错给RF
        # 参考http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#reporting-keyword-status
        if rd['retlist'] != []:
            raise  Exception("cannot delete all school students!!")


    def studentlist_should_contain(self,studentlist,username, realname, classid, phonenumber, studentid,expectedtimes=1):
        item = {
            "classid": classid,
            "username": username,
            "realname": realname,
            "phonenumber": phonenumber,
            "id": int(studentid)
        }
        print(studentlist)
        print(item)
        occurTimes = studentlist.count(item)
        logging.info('occur {} times'.format(occurTimes))

        if occurTimes != int(expectedtimes):
            raise Exception(f'学生列表包含了{occurTimes}次指定信息,期望包含{expectedtimes}次')

if __name__ == '__main__':
    scm = SchoolStudentLib()
    ret = scm.list_school_student()

    # ret = scm.add_school_class(1,'新测试',77)
    # print(json.dumps(ret, indent=2))
    #
    # ret = scm.delete_school_class(28)
    # print(json.dumps(ret, indent=2))
    #
    # ret = scm.list_school_class(1)
    # print(json.dumps(ret, indent=2))
    # #
    # scm.delete_all_school_classes()

