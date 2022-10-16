#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 21:35
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


data_1 = ['a', 'b', 'c']
data_2 = [1, 2]


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize_1(a, b):
    print(f'笛卡尔积 测试数据为：{a}, {b}')


tuple_data_1 = (
    {
        'user': 'zhangbc',
        'pwd': 'xxaasbb'
    },
    {
        'user': 'wangwu',
        'pwd': 'xxxxxxxa'
    }
)


@pytest.mark.parametrize('dict_data', tuple_data_1)
def test_parametrize_2(dict_data):
    print(f'user: {dict_data["user"]}, pwd: {dict_data["pwd"]}')


list_data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

ids_1 = ["a: {0} + b: {1} = expect: {2}".format(a, b, expect)
       for a, b, expect in list_data_1]


@pytest.mark.parametrize('a, b, expect', list_data_1, ids=ids_1)
class TestParametrize:
    def test_parametrize_1(self, a, b, expect):
        print(f'测试函数1，测试数据为：{a} - {b}')
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print(f'测试函数2，测试数据为：{a} - {b}')
        assert a + b == expect


@pytest.fixture()
def login(request):
    name = request.param
    print(f'== 账号是：{name} ==')
    return name


list_data_2 = ['tom', 'kite']
ids_2 = [f'login test name is: {name}' for name in list_data_2]


@pytest.mark.parametrize('login', list_data_2, ids=ids_2, indirect=True)
def test_name(login):
    print(f'测试用例的登录账号：{login}')


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--alluredir', 'reports', 'test_case05.py'])
