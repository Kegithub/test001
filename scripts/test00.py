import pytest, allure


class Test:
    allure.description("这是一个测试")
    pytest.mark.usefixtures()
    def test_001(self):
        print("---------------1")
        assert True