#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/12 01:06
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


class TestLogin:

    def test_case01(self):
        print('test_case01')
        assert 1 == 1
        assert 1 != 2


if __name__ == '__main__':

    pytest.main(['-s', '-v'])
