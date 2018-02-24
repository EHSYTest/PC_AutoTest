import pytest, allure


class Test_a():

    # @pytest.fixture('module', autouse=True)
    def setup_method(self, method):
        self.a = 'a'
        print('setup')

    @allure.feature('Feature1')
    @allure.story('Story1')
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_a(self):
        allure.environment(report='Allure report', browser='chrome', version='JiuYiBao2.0.6')
        with pytest.allure.step('打印a'):
            print(self.a)
        with pytest.allure.step('结束'):
            pass

    @allure.feature('Feature1')
    @allure.story('Story2')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_b(self):
        print(self.a+'------------')
        assert self.a == 'b'
    @allure.feature('Feature2')
    @allure.story('Story1')
    @pytest.allure.BLOCKER
    def test_c(self):
        pass

    @allure.feature('Feature1')
    @allure.story('Story3')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_d(self):
        print(self.a + '------------')
        assert self.a == 'b'

    @allure.feature('Feature2')
    @allure.story('Story1')
    @pytest.allure.BLOCKER
    def test_e(self):
        pass
    @staticmethod
    def teardown_method(method):
        f = open('../testresult/screenshot/test.png', 'rb').read()
        allure.attach('IMG', f, allure.attach_type.PNG)
        print('teardown')