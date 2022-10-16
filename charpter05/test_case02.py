#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 23:10
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest

from .src import calculator


class TestCalculator:
    def test_add(self):
        ans = calculator.calculator(1, 2, 3)
        assert ans == 5

    def test_sub(self):
        ans = calculator.calculator(2, 2, 3)
        assert ans == -1

    def test_mul(self):
        ans = calculator.calculator(3, 2, 3)
        assert ans == 6

    def test_div(self):
        ans = calculator.calculator(4, 6, 3)
        assert ans == 2


if __name__ == '__main__':
    pytest.main(['--cov=./src', '--cov-report=html', 'test_case02.py'])
