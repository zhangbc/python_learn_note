#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 22:47
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import logging

import pytest


def test_01():
    log = logging.getLogger('test_01')
    log.debug('Testing begin...')
    log.info('Testing begin...')
    log.warning('Testing begin...')
    log.error('Testing begin...')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_case01.py'])