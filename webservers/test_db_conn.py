#!/usr/bin/env python
# coding:utf-8


"""
测试数据库连接
@Date:         2021/10/23 00:16
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
from pymysql import Connect

conn = Connect(host='127.0.0.1',
               port=3306,
               user='root',
               password='zbc12300',
               db='mysql',
               charset='utf8')

print('-------连接成功---------')
