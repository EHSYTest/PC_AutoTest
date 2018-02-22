import pytest, allure

class Test_a():
    # @pytest.fixture('module', autouse=True)
    def setup_method(self, method):
        self.a = 'a'
        print('setup')

    def test_a(self):
        print(self.a)

    def test_b(self):
        print(self.a+'------------')

    @staticmethod
    def teardown_method(method):
        f = open('../testresult/screenshot/test_address_1.png', 'rb').read()
        allure.attach('IMG', f, allure.attach_type.PNG)
        print('teardown')