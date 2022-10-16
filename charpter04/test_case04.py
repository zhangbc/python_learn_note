#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 21:07
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


@pytest.mark.xfail()
def test_01():
    a, b = 'a', 'b'
    assert a != b


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case04.py'])