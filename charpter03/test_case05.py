#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/15 21:13
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import time

import pytest


@pytest.mark.timeout(10)
def test_01():
    time.sleep(5)
    print('test_01')


@pytest.mark.timeout(10)
def test_02():
    time.sleep(11)
    print('test_02')


def test_03():
    print('test_03')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case05.py'])
