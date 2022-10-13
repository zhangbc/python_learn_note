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


# @pytest.fixture()
# @pytest.fixture(scope='function')
@pytest.fixture(scope='class')
# @pytest.fixture(scope='module')
# @pytest.fixture(scope='package')
# @pytest.fixture(scope='session')
def my_fixture():
    print('my_fixture')


def test_01(my_fixture):
    print('test_01')


def test_02(my_fixture):
    print('test_02')


class TestCase01:
    def test_case01(self, my_fixture):
        print('test_case01')


class TestCase02:
    def test_case02(self, my_fixture):
        print('test_case02')

    def test_case03(self, my_fixture):
        print('test_case03')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case02.py'])
