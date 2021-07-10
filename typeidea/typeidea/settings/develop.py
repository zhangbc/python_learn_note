#!/usr/bin/env python
# coding:utf-8


"""

@Date:         2021/7/7 23:18
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_typeidea',
        'USER': 'root',
        'PASSWORD': 'zbc12300',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
