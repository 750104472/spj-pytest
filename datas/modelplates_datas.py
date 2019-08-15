"""
------------------------------------
@Time : 2019/7/16 9:56
@Auth : linux超
@File : login_datas.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class ModelplatesData(object):
    """配置模板测试数据"""

    # 正确的用户名和密码
    user_password = {

            # 管理员
            'username': '管理员',
            'password': '123456'

            # 开发区采购人
            # 'username': 'kfq_cgr',
            # 'password': '12345678'

            # 崇川区区采购人
            # 'username': 'ccq_cgr',
            # 'password': '12345678'

            # 港闸区采购人
            # 'username': 'gzq_cgr',
            # 'password': '12345678'

        }

    cgr_account = {

        # 开发区采购人
        'username': 'kfq_cgr',
        'password': '12345678'

        # 崇川区区采购人
        # 'username': 'ccq_cgr',
        # 'password': '12345678'

        # 港闸区采购人
        # 'username': 'gzq_cgr',
        # 'password': '12345678'

    }


    add_model_nums = [
        # 模板名称 模板一级品目 模板二级品目
        (
            '印刷服务品目',
            '印刷服务',
            '印刷'
        )

        # (
        #     '办公楼物业管理服务品目',
        #     '物业服务',
        #     '办公楼物业管理'
        # )

        # (
        #     '宿舍物业管理服务品目',
        #     '物业服务',
        #     '宿舍物业管理'
        # )

    ]

    add_key_nums = [
        (
            '印刷品名称',
            '大文本',
            '1'
        ),
        (
            '印刷数量',
            '大文本',
            '2'
        ),
        (
            '备注',
            '大文本',
            '3'
        )
    ]



