#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/15 20:48
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


@pytest.mark.run(order=2)
def test_01():
    print('test_01')


@pytest.mark.run(order=1)
def test_02():
    print('test_02')


@pytest.mark.run(order=3)
def test_03():
    print('test_03')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case03.py'])
