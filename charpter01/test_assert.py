#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/12 01:39
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


def test_assert01():
    assert True
    assert not False

    items = ['tom', 'kite', 'rose']
    assert 'tom' in items

    assert 1 == 1
    assert 1 != 2


def test_assert02():
    assert True


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_assert.py'])
