#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/13 23:48
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


@pytest.fixture
def func_1():
    print('func_1')
    return 'hello'


def test_01(func_1):
    print(func_1)
    print('test_case_01')
    assert func_1 == 'hello'


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case01.py'])
