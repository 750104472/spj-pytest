import pytest
import logging
from api.SchoolClassLib import SchoolClassLib
from common.record_log import logger

sc = SchoolClassLib()

@pytest.fixture(scope='session',autouse=True)
def f_delete_all_school_classes():
    sc.delete_all_school_classes()
    logger.info('----------SETUP删除所有班级成功-----------')
    yield
    sc.delete_all_school_classes()
    logger.info('----------TEARDOWN删除所有班级成功-----------')

@pytest.fixture
def f_add_school_class():
    bodyDict = sc.add_school_class(1,'七年级1班',60)
    class_id = bodyDict['id']
    logger.info(f'----------SETUP添加[1,七年级1班,60]成功,班级id为{class_id}-----------')
    yield class_id
    sc.delete_school_class(class_id)
    logger.info('----------TEARDOWN删除[1,七年级1班,60]成功-----------')

# if __name__ == "__main__":
#     f_add_school_class()