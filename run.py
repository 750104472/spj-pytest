import pytest
from common.create_dirs import CreateDir
from config.config import REPORT_DIR
from common.send_mail import SendEmail

SE = SendEmail()
def main():
    CreateDir.create_dir(REPORT_DIR)
    html_name = CreateDir.generate_filename('html')

    # addopts = -v --reruns 1 - -html = report / report.html --self-contained-html
    args = ['-v','--reruns', '1', '--html=report/' + html_name,'--self-contained-html']
    pytest.main(args)
    SE.send_email('%s/%s'%(REPORT_DIR,html_name))


if __name__ == '__main__':
    main()
