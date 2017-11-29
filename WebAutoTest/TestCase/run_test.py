import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


def send_email(dir, flag):
    report = open(dir, 'rb')
    mail_body = report.read()
    report.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('EHSY-自动化测试报告-' + flag, 'utf-8')
    msg['From'] = 'rick_zhang@ehsy.com'
    msg['To'] = "rick_zhang@ehsy.com"
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    smtp.login('rick_zhang@ehsy.com', '690903Zr')
    smtp.sendmail('rick_zhang@ehsy.com', 'rick_zhang@ehsy.com', msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    file = open('../TestResult/order.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='EHSY-WWW自动化测试报告', description='自动化测试详情')
    result = runner.run(discover)
    file.close()

    if result.errors:
        msg = 'Error!'
    elif result.failures:
        msg = 'Failed!'
    else:
        msg = 'Success!'

    dir = '../TestResult/order.html'
    send_email(dir, msg)


