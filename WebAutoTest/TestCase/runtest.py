import unittest
from HTMLTestRunner import HTMLTestRunner
from Page_Base import AssistFunction
import threading

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')


if __name__ == '__main__':
    file = open('../TestResult/EHSY_AutoTest.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='EHSY-New自动化测试报告', description='自动化测试详情')
    result = runner.run(discover)
    file.close()

    if result.errors:
        msg = 'Error!'
    elif result.failures:
        msg = 'Failed!'
    else:
        msg = 'Success!'
    dir = '../TestResult/EHSY_AutoTest.html'
    AssistFunction().send_email(dir, msg)

