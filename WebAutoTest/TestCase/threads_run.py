import unittest
from HTMLTestRunner import HTMLTestRunner
from Page_Base import AssistFunction
import threading

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')


if __name__ == '__main__':
    suit_list = [i for i in discover]

    def run_tests(suit):
        file = open('../TestResult/EHSY_AutoTest.html', 'wb')
        runner = HTMLTestRunner(stream=file, title='WWW下单——测试报告', description='测试情况')
        result = runner.run(suit)
        file.close()

    case_threads = []
    for suit in suit_list:
        print(suit)
        case_thread = threading.Thread(target=run_tests, args=(suit))
        case_threads.append(case_thread)
    for i in case_threads:
        i.start()
    for i in case_threads:
        i.join()
