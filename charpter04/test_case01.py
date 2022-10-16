#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/15 21:49
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


def setup():
    print('setup')


def teardown():
    print('\nteardown')


def test_01():
    print('test_01')


def test_02():
    print('test_02')


class TestCase01:
    def test_01(self):
        print('testcase01-test_01')

    def test_02(self):
        print('testcase02-test_02')

    def setup(self):
        print('\ntestcase01-setup')

    def teardown(self):
        print('\ntestcase01-teardown')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case01.py'])
