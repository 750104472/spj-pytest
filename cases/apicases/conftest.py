import pytest
import logging
import cfg
from api.SchoolClassLib import SchoolClassLib
from common.record_log import logger
from api.SchoolTeacherLib import SchoolTeacherLib
sc = SchoolClassLib()
st = SchoolTeacherLib()
@pytest.fixture(scope='function',autouse=True)
def f_delete_all_school_classes():
    st.delete_all_school_teachers()
    sc.delete_all_school_classes()
    logger.info('----------SETUP删除所有老师、班级成功-----------')
    yield
    st.delete_all_school_teachers()
    sc.delete_all_school_classes()
    logger.info('----------TEARDOWN删除所有老师、班级成功-----------')

@pytest.fixture
def f_add_school_class():
    bodyDict = sc.add_school_class(1,'七年级1班',60)
    class_id = bodyDict['id']
    logger.info(f'----------SETUP添加[1,七年级1班,60]成功,班级id为{class_id}-----------')
    yield class_id
    sc.delete_school_class(class_id)
    logger.info('----------TEARDOWN删除[1,七年级1班,60]成功-----------')

@pytest.fixture
def f_add_school_teacher(f_add_school_class):
    bodyDict = st.add_school_teacher("linguowei","linguowei",cfg.g_math,f_add_school_class,15851398151,"750104472@qq.com","320283828323")
    logger.info('----------SETUP添加老师【"linguowei","linguowei",cfg.g_math,f_add_school_class,15851398151,"750104472@qq.com","320283828323"】成功-----------')
    yield bodyDict['id']
    st.delete_school_teacher(bodyDict['id'])
    logger.info('----------TEARDOWN删除老师【"linguowei","linguowei",cfg.g_math,f_add_school_class,15851398151,"750104472@qq.com","320283828323"】成功-----------')


# if __name__ == "__main__":
#     f_add_school_class()