#!/usr/bin/env python
# coding:utf-8


"""
数据库基本操作
@Date:         2021/10/24 13:39
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
import hashlib

from pymysql import Connect
from pymysql.cursors import DictCursor

conn = Connect(host='127.0.0.1',
               port=3306,
               user='root',
               password='zbc12300',
               db='db_fast_api',
               charset='utf8')


def save(table, **item):
    # TODO: 存储数据
    pass


def query(table, *field, where=None, args=None, one=False):
    """
    基本查询
    @param table:
    @param field:
    @param where:
    @param args:
    @param one:
    @return:
    """

    sql = "select {0} from {1}".format(','.join(field), table)
    if where:
        sql += " where " + where

    with conn.cursor(DictCursor) as cur:
        cur.execute(sql, args=args)
        res = cur.fetchone() if one else cur.fetchall()

    return res


if __name__ == '__main__':
    r = query('user', 'id', 'phone', 'nick_name', 'avatar',
              where='username=%s and auth_string=%s',
              args=('disen', hashlib.sha1('123'.encode('utf8')).hexdigest()),
              one=True)
    print(r)
