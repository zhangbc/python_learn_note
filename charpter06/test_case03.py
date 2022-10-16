#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/17 00:10
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


@pytest.mark.dependency()
def test_login():
    assert False


@pytest.mark.dependency(depends=['test_login'])
def test_add_cart():
    assert False


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case03.py'])
