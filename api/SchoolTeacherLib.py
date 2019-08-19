import requests,json
from cfg import g_vcode
from pprint import pprint
from robot.libraries.BuiltIn import BuiltIn
import logging
import pdb

class  SchoolTeacherLib:
    URL = "http://ci.ytesting.com/api/3school/teachers"

    def __init__(self):
        self.vcode = g_vcode

    def set_vcode(self,vcode):
        self.vcode = vcode



    def delete_school_teacher(self,teacherid):
        payload = {
            'vcode'  : self.vcode,
        }

        url = '{}/{}'.format(self.URL,teacherid)
        response = requests.delete(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict


    def list_school_teacher (self,subjectid=None):      #subjectid 学科id
        if subjectid != None:
            params = {
                'vcode':self.vcode,
                'action':'search_with_pagenation',
                'subjectid':int(subjectid)
            }
        else:
            params = {
                'vcode':self.vcode,
                'action':'search_with_pagenation'
            }

        response = requests.get(self.URL,params=params)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)
        return bodyDict

#subjectid为学科id
    def add_school_teacher(self,username,realname,subjectid,classlist,phonenumber,email,idcardnumber,idSavedName=None):
        teplist = str(classlist).split(',')
        newclasslist = [{"id":one}  for one in teplist if one!='']
        payload = {
            'vcode'  : self.vcode,
            'action' : 'add',
            'username'  : username,
            'realname'   : realname,
            'subjectid'  : subjectid,
            'classlist' : json.dumps(newclasslist),
            'phonenumber' : phonenumber,
            'email' : email,
            'idcardnumber' : idcardnumber

        }
        response = requests.post(self.URL,data=payload)

        bodyDict = response.json()
        pprint (bodyDict,indent=2)

        if idSavedName:
            BuiltIn().set_global_variable('${%s}'%idSavedName,bodyDict['id'])
        return bodyDict

    def modify_school_teacher(self,teacherid,realname=None,subjectid=None,classlist=None,phonenumber=None,email=None,idcardnumber=None):
        payload = {
            'vcode':self.vcode,
            'action':'modify'
        }
        if realname:
            payload['realname'] = realname
        if subjectid:
            payload['subjectid'] = subjectid
        if phonenumber:
            payload['phonenumber'] = phonenumber
        if email:
            payload['email'] = email
        if idcardnumber:
            payload['idcardnumber'] = idcardnumber
        if classlist:
            templist = str(classlist.split(','))
            newclasslist = [{"id":one} for one in templist if one!='']
            payload['classlist'] = json.dumps(newclasslist)

        url='{}/{}'.format(self.URL,teacherid)
        response = requests.put(url,data=payload)
        bodyDict = response.json()
        pprint(bodyDict)
        return bodyDict

    def delete_all_school_teachers(self):
        # 先列出所有班级
        rd =  self.list_school_teacher()
        pprint(rd, indent=2)

        # 删除列出的所有班级
        for one in rd['retlist']:
            self.delete_school_teacher(one['id'])

        #再列出七年级所有老师
        rd =  self.list_school_teacher()
        pprint (rd,indent=2)

        # 如果没有删除干净，通过异常报错给RF
        # 参考http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#reporting-keyword-status
        if rd['retlist'] != []:
            raise  Exception("cannot delete all school teachers!!")


    def teacherlist_should_contain(self,
                                   teacherlist,
                                   username,
                                   realname,
                                   teacherid,
                                   classlist,
                                   phonenumber,
                                   email,
                                   idcardnumber,
                                   expectedtimes=1):

        teacherclasslist = str(classlist)

        item = {
            "username": username,
            "teachclasslist": [int(one.strip()) for one in teacherclasslist.split(',')],
            "realname": realname,
            "id": int(teacherid),
            "phonenumber": str(phonenumber),
            "email": email,
            "idcardnumber": str(idcardnumber)
        }

        occurTimes = teacherlist.count(item)
        logging.info('occur {} times'.format(occurTimes))

        if occurTimes != int(expectedtimes):
            raise Exception(f'教师列表包含了{occurTimes}次指定信息,期望包含{expectedtimes}次')

if __name__ == '__main__':
    scm = SchoolTeacherLib()
    ret = scm.list_school_teacher()

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

