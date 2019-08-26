import pytest
from common.create_dirs import CreateDir
from config.config import REPORT_DIR
import yagmail

# from common.send_mail import SendEmail
# SE = SendEmail()

def sendemail(report):
    yag = yagmail.SMTP(user="15851398152@163.com",
                       password="921124lgw",
                       host="smtp.163.com")
    subject = "主题：自动化测试报告"
    contents = "正文，请查看附件"
    yag.send("750104472@qq.com",subject,contents,report)
    print("15851398152@163.com邮件发送成功,查收750104472@qq.com邮箱" )


def main():
    CreateDir.create_dir(REPORT_DIR)
    html_name = CreateDir.generate_filename('html')

    # addopts = -v --reruns 1 - -html = report / report.html --self-contained-html
    args = ['-v','--reruns', '1','--html=report/' + html_name,'--self-contained-html']
    pytest.main(args)
    sendemail('%s/%s'%(REPORT_DIR,html_name))


if __name__ == '__main__':
    main()
