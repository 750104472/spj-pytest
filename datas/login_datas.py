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


class LoginData(object):
    """登录功能测试数据"""

    login_success_data = [
        (
            '管理员',
            '123456',
            '【后台管理】'
        )
    ]

    login_format_data = [
        (
            '',
            'python',
            '账号或密码不能为空'
        ),
        (
            '18684720553',
            '',
            '账号或密码不能为空'
        ),
        (
            '',
            '',
            '账号或密码不能为空'
        )
    ]

    login_account_error_data = [
        (
            'kfq_cgr',
            'python',
            '温馨提示：登录名或密码错误'
        ),
        (
            '18684720553',
            'pwd_error',
            '温馨提示：没有该用户，请您重新注册。'
        )
    ]


if __name__ == '__main__':
    login = LoginData()
    print(login.login_account_error_data)
