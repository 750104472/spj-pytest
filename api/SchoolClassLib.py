import requests
from cfg import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn
import json
from common.record_log import logger

class  SchoolClassLib:
    URL = "http://ci.ytesting.com/api/3school/school_classes"

    def __init__(self):
        self.vcode = g_vcode

    def delete_school_class(self,classid):
        payload = {
            'vcode'  : self.vcode,
        }

        url = '{}/{}'.format(self.URL,classid)
        response = requests.delete(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def list_school_class(self,gradeid=None):
        if gradeid != None:
            params = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade',
                'gradeid':int(gradeid)
            }
        else:
            params = {
                'vcode':self.vcode,
                'action':'list_classes_by_schoolgrade'
            }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        return bodyDict


    def add_school_class(self,gradeid,name,studentlimit,class_id=None):                #idSavedName是classid的全局变量
        payload = {
            'vcode'  : self.vcode,
            'action' : 'add',
            'grade'  : int(gradeid),
            'name'   : name,
            'studentlimit'  : int(studentlimit),
        }
        response = requests.post(self.URL,data=payload)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)

        if class_id:
            class_id = bodyDict['id']
            print(class_id)


        return bodyDict


    def modify_school_class(self,classid,name,studentlimit):
        payload = {
            'vcode':self.vcode,
            'action':'modify',
            'name':name,
            'studentlimit':int(studentlimit),
        }
        url='{}/{}'.format(self.URL,classid)
        response = requests.put(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict

    def delete_all_school_classes(self):
        # 先列出所有班级
        rd =  self.list_school_class()
        pprint(rd, indent=2)

        # 删除列出的所有班级
        for one in rd['retlist']:
            self.delete_school_class(one['id'])

        #再列出七年级所有班级
        rd =  self.list_school_class()
        pprint (rd,indent=2)

        # 如果没有删除干净，通过异常报错给RF
        # 参考http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#reporting-keyword-status
        if rd['retlist'] != []:
            raise  Exception("cannot delete all school classes!!")

    def classlist_should_contain(self,classlist,grade_name,classid,invitecode,classname,studentlimit,expectedtimes=1):
        item = {
            "name": classname,
            "grade__name":grade_name,
            "invitecode":invitecode,
            "studentlimit":studentlimit,
            "studentnumber":0,
            "id": classid,
            "teacherlist":[]
        }

        occurTimes = classlist.count(item)
        logger.info('occur {} times'.format(occurTimes))

        if occurTimes != int(expectedtimes):
            raise Exception(f'班级列表包含了{occurTimes}次指定信息,期望包含{expectedtimes}次')





if __name__ == '__main__':
    scm = SchoolClassLib()
    ret = scm.list_school_class()

    # ret = scm.add_school_class(1,'新测试',77,'class_id')
    # print(json.dumps(ret, indent=2))
    #
    # ret = scm.delete_school_class(28)
    # print(json.dumps(ret, indent=2))
    #
    # ret = scm.list_school_class(1)
    # print(json.dumps(ret, indent=2))
    # #
    # scm.delete_all_school_classes()

