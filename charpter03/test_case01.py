#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/15 20:20
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


@pytest.mark.cat1
def test_01():
    print('test_01')


@pytest.mark.cat2
def test_02():
    print('test_02')


if __name__ == '__main__':
    pytest.main(['-s', '-v', '-m', 'cat2', 'test_case01.py'])
