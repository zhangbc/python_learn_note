#!/usr/bin/env python
# coding:utf-8


"""
MySQL 基本操作
@Date:         2021/10/24 22:00
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
import logging

import MySQLdb
from config.config import configs
from MySQLdb.connections import Connection, Error
from utils.middlewares import *

logger = logging.getLogger(__name__)


class MysqlUtils(object):
    """
    Mysql 工具类
    """

    @staticmethod
    def connect(conf=None):
        if conf is None:
            conf = configs['mysql']

        try:
            conn = MySQLdb.connect(host=conf['host'],
                                   db=conf['db'],
                                   port=conf['port'],
                                   user=conf['user'],
                                   passwd=conf['password'],
                                   charset='utf8')
            return conn
        except Error as ex:
            logging.error('MySQL connections failed: {0}.'.format(ex))

    """
    工具类方法
    """

    @staticmethod
    @typeassert(conn=Connection, query=str, args=tuple)
    def common_query(conn=None, query='', args=()):
        """
        Common Query
        :param conn:
        :param query:
        :param args:
        :return: cursor
        """

        if not conn or not query:
            raise TypeError
        try:
            cursor = conn.cursor()
            if args:
                cursor.execute(query, args)
            else:
                cursor.execute(query)
            return cursor
        except Exception as error:
            logging.error('Common query error:{0}'.format(error))

    @staticmethod
    @typeassert(conn=Connection, table=str)
    def select_all(conn=None, table=''):
        """
        Select all table data to array of dict_item
        :param conn:
        :param table:
        :return:
        """

        if not conn or not table:
            raise TypeError

        cursor = MysqlUtils.common_query(conn=conn, query="select * from {0};".format(table))
        rows = cursor.fetchall()
        dict_rows = []
        for row in rows:
            dict_item = MysqlUtils.sql_row_to_dict(cursor=cursor, row=row)
            dict_rows.append(dict_item)
        return dict_rows

    @staticmethod
    @typeassert(conn=Connection, table=str, column=str)
    def column_select(conn=None, table='', column='', value=None):
        """
        condition query
        :param conn:
        :param table:
        :param column:
        :param value:
        :return:
        """
        if not conn or not table or not column or not value:
            raise RuntimeError

        try:
            query = 'SELECT * FROM {0} WHERE {1}=%s'.format(table, column)
            args = (value,)
            cursor = MysqlUtils.common_query(conn, query, args)
            return cursor
        except Error as error:
            logging.error('Column_select find all error: {0}.'.format(error))

    @staticmethod
    @typeassert(conn=Connection, table=str, columns=tuple, values=tuple)
    def columns_update(conn=None, table='', columns=(), values=(),
                       select_column='', select_value=None):
        """
        update query
        :param conn:
        :param table:
        :param columns:
        :param values:
        :param select_column:
        :param select_value:
        :return:
        """

        if not conn or not table or not columns or not values:
            raise TypeError

        try:
            columns_sql = MysqlUtils.tuple_to_update_sql(columns)
            query = 'UPDATE {0} SET {1} WHERE {2}=%s;'.format(table, columns_sql, select_column)
            args = tuple(list(values) + [select_value])
            cursor = MysqlUtils.common_query(conn, query, args)
            conn.commit()
            return cursor
        except Exception as error:
            logging.error('Columns_update error: {0}.'.format(error))

    @staticmethod
    @typeassert(conn=Connection, query=str, params=list)
    def batch_insert(conn=None, query='', params=None):
        """
        execute batch insert sql query
        :param conn:
        :param query:
        :param params:
        :return:
        """

        if params is None:
            params = list()

        if not conn or not query:
            raise TypeError
        try:
            cursor = conn.cursor()
            cursor.executemany(query, params)
            conn.commit()
            return cursor
        except Exception as error:
            logging.error('execute batch insert query error:{0}'.format(error))

    @staticmethod
    @typeassert(conn=Connection, table=str, column=str)
    def common_delete(conn=None, table='', column='', value=None):
        """
        delete
        :param conn:
        :param table:
        :param column:
        :param value:
        :return:
        """
        if not conn or not table or not column or not value:
            raise RuntimeError
        try:
            query = 'DELETE FROM ' + table + ' WHERE ' + column + '=%s;'
            args = (value,)
            cursor = MysqlUtils.common_query(conn, query, args)
            conn.commit()
            return cursor
        except Error as error:
            logging.error('delete records error: {0}'.format(error))

    """
    sql拼装
    """

    @staticmethod
    @typeassert(obj=tuple)
    def tuple_to_sql(obj=()):
        """
         Tuple to sql like ('a','b','c')=>"(a,b,c)"
        :param obj:
        :return:
        """
        return str(obj).replace('\'', '')

    @staticmethod
    @typeassert(obj=tuple)
    def tuple_to_plaint_sql(obj=()):
        """
         Tuple to sql like ('a','b','c')=>"a,b,c"
        :param obj:
        :return:
        """
        return str(obj).replace('\'', '').replace('(', '').replace(')', '')

    @staticmethod
    def multiple_str(item='', multiple=0):
        """
        Create str like "%,%@,%@"
        :param item:
        :param multiple:
        :return: item,item,item
        """
        m = []
        m.extend([item] * multiple)
        return ','.join(m)

    @staticmethod
    def tuple_to_update_sql(obj=()):
        """
        Tuple to update sql like ('a','b','c')=>"a=%,b=%,c=%"
        :return:
        """

        new_sql = list()
        for column in obj:
            if not isinstance(column, str):
                column = str(column)
            new_sql.append(column + '=%s')
        new_sql = tuple(new_sql)
        result_sql = str(new_sql).replace('\'', '').replace('(', '').replace(')', '')
        if result_sql.endswith(','):
            result_sql = result_sql[:-1]
        return result_sql

    @staticmethod
    def sql_row_to_dict(cursor=None, row=None):
        """
        Sql result row to dict
        :param cursor:
        :param row:
        :return:
        """

        try:
            result = dict()
            columns = [desc[0] for desc in cursor.description]
            for k, v in zip(columns, row):
                result[k] = v
            return result
        except Error as error:
            logging.error('sql_row_to_dict error: {0}.'.format(error))
