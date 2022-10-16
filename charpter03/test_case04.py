#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/15 20:55
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


ANDROID_VERSION = 4
SYS_VERSION = 3


@pytest.mark.skip(reason='这个是跳过的原因！')
def test_01():
    print('test_01')


@pytest.mark.skipif(ANDROID_VERSION < 8, reason='Android版本太低')
def test_02():
    print('test_02')


@pytest.mark.xfail(SYS_VERSION < 5, reason='用例标记失败')
def test_03():
    print('test_03')
    assert 1 == 0


@pytest.mark.xfail(SYS_VERSION > 5, reason='用例标记成功')
def test_04():
    print('test_04')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case04.py'])
