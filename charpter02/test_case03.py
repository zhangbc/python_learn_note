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


@pytest.fixture()
def my_fixture():
    print('my_fixture')


def test_01(my_fixture):
    print('test_01')


class TestCase01:
    def test_case01(self, my_fixture):
        print('test_case01')


@pytest.mark.usefixtures('my_fixture')
def test_02():
    print('test_02')
    print(my_fixture)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case03.py'])
