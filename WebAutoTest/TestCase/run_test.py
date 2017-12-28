import unittest, sys
from HTMLTestRunner import HTMLTestRunner
from My_Function import send_email

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_order.py')


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


