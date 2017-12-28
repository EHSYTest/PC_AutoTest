import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email(dir, flag):
    report = open(dir, 'rb')
    mail_body = report.read()
    report.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('EHSY-自动化测试报告-' + flag, 'utf-8')
    msg['From'] = 'EHSY自动化测试'
    msg['To'] = 'rick_zhang@ehsy.com, vivien_tang@ehsy.com'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    smtp.login('rick_zhang@ehsy.com', '690903Zr')
    smtp.sendmail('rick_zhang@ehsy.com', ['rick_zhang@ehsy.com', 'vivien_tang@ehsy.com'], msg.as_string())
    smtp.quit()
