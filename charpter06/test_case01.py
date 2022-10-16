#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 23:42
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


params = [(1, 2, 3), (4, 5, 9), (3, 6, 8)]


# @pytest.mark.flaky(reruns=3, delay=1)
@pytest.mark.parametrize('a,b,result', params)
def test_login(a, b, result):
    assert a + b == result


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case01.py'])
    pytest.main(['--reruns', '3', '--reruns-delay', '1',
                 '-s', '-v', 'test_case01.py'])
