#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/14 00:39
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest

params = ['case1', 'case2', 'case3', 'case4', 'case5']


@pytest.fixture(params=params, autouse=True)
def my_fixture():
    return params


def test_01():
    print(params)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case05.py'])
