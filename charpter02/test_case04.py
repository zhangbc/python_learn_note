#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/14 00:02
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


@pytest.fixture(autouse=True)
def my_fixture():
    print('my_fixture')


def test_01():
    print('test_01')


class TestCase01:
    def test_case01(self):
        print('test_case01')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case04.py'])
