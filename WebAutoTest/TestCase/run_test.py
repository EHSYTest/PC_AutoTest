import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


if __name__ == '__main__':
    # now = time.strftime("%Y_%m_%d %H_%M_%S")
    file = open('../TestResult/order.html', 'wb')
    runner = HTMLTestRunner(stream=file, title='WWW测试报告', description='测试情况')
    runner.run(discover)
    file.close()

