#!/usr/bin/env python
# coding: utf-8


from os.path import expanduser

configs = {
    'mysql': {
        'host': '121.5.107.105',
        'port': 3306,
        'user': 'root',
        'password': 'Wangxinchao@123',
        'db': 'follow_sign'
    },
    'pid': {
        'exchange': expanduser('~/pid/exchange_service.pid'),
    },
    'mode': 'full',  # 运行模式 full:全量计算, increase:增量计算
    'token': 'N05FuUnKzwnPOBrZ869oi8rz20CM6uLN9h7oqcLyMBmQL7bzo-kOVxZQqw6f5iYv'
}
