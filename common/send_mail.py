# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import os


# def find_report_name():
#     """查找最后生成的报告文件的路径"""
#     result_dir = os.path.abspath('..') + "\\report\\"
#     lists = os.listdir(result_dir)
#     lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
#     file_name = os.path.join(result_dir, lists[-1])
#     return file_name

class SendEmail(object):
    def send_email(self,report_file):
        """发送邮件方法"""
        try:
            # 配置邮件信息
            # 接收邮箱
            receiver = "750104472@qq.com"
            # 发送邮件服务器
            smtp_server = "smtp.163.com"
            port = "25"
            # 发送邮箱账号和密码（授权码）
            username = "15851398152@163.com"
            password = "921124lgw"

            # 读取测试报告文件
            mail_body = open(report_file, "r", encoding="utf-8").read()
            # 定义邮件内容
            msg = MIMEMultipart()
            body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
            msg['Subject'] = "政府采购网上服务超市自动化测试报告"
            msg['from'] = username
            msg['to'] = receiver
            msg["date"] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
            msg.attach(body)
            # 定义附件内容
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename= "report.html"'
            msg.attach(att)

            # 连接邮箱服务器
            smtp = smtplib.SMTP()
            smtp.connect(host=smtp_server, port=port)
            # tls加密方式
            # smtp.ehlo()
            # smtp.starttls()
            # smtp.ehlo()
            # 登录邮箱
            smtp.login(username, password)
            # 发送邮件
            smtp.sendmail(username, receiver, msg.as_string())
            # 断开连接
            smtp.quit()
            print("%s 发送成功,查收%s邮箱" % (username, receiver))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    pass