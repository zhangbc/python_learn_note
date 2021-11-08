#!/usr/bin/env python
# coding: utf-8


from os.path import expanduser

configs = {
    'mysql': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'zbc12300',
        'db': 'db_spiders'
    },
    'pid': {
        'exchange': expanduser('~/pid/exchange_service.pid'),
    },

    'mode': 'full',  # 运行模式 full:全量计算, increase:增量计算
    'token': 'N05FuUnKzwnPOBrZ869oi8rz20CM6uLN9h7oqcLyMBmQL7bzo-kOVxZQqw6f5iYv'
}
