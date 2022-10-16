#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/17 00:38
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import time

import pytest


def test_01():
    time.sleep(1)
    print('test_01')


def test_02():
    time.sleep(1)
    print('test_02')


def test_03():
    time.sleep(1)
    print('test_03')


if __name__ == '__main__':
    time_start = time.time()
    # pytest.main(['-s', '-v', '-n', '2', 'test_case04.py'])
    pytest.main(['-s', '-v', '-n', 'auto', '--html', 'report.html', 'test_case04.py'])
    time_end = time.time()
    print(f'Totally cost: {time_end - time_start}')
