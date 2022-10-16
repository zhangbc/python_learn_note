#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 23:57
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


def test_assume():
    print('操作1：1==2')
    pytest.assume(1 == 2)
    print('操作2：2==2')
    pytest.assume(2 == 2)
    print('操作3：3==3')
    pytest.assume(3 == 3)


def test_assert():
    print('操作1：1==2')
    assert 1 == 2
    print('操作2：2==2')
    assert 2 == 2
    print('操作3：3==3')
    assert 3 == 3


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case02.py'])
