#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/15 20:31
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


names = ['tom', 'kite', 'rose']


def test_1():
    assert 3 + 5 == 8


def test_2():
    assert 2 + 4 == 6


def test_3():
    assert 6 * 9 == 54


@pytest.mark.parametrize('test_input, expected',
                         [('3+5', 8), ('2+4', 6), ('6*9', 54)])
def test_eval(test_input, expected):
    print(f'测试数据：{test_input}, 期望值：{expected}')
    assert eval(test_input) == expected


@pytest.mark.parametrize('name', names)
def test_print_names(name):
    print(name)


users = [('tom', '123'), ('kite', '456')]


@pytest.mark.parametrize('username,pwd', users)
def test_login(username, pwd):
    print(f'username: {username}, pwd: {pwd}')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case02.py'])
