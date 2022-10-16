#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 00:30
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


def setup_function():
    print('setup_function')


def teardown_function():
    print('\nteardown_function')


def test_01():
    print('test_01')


def test_02():
    print('test_02')


class TestCase01:
    def test_01(self):
        print('testcase01-test_01')

    def test_02(self):
        print('testcase02-test_02')

    def setup_method(self):
        print('\ntestcase01-setup_method')

    def teardown_method(self):
        print('\ntestcase01-teardown_method')

    def setup_class(self):
        print('\ntestcase01-setup_class')

    def teardown_class(self):
        print('\ntestcase01-teardown_class')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case02.py'])
