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

THEME = 'boostrap'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'themes', THEME, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
