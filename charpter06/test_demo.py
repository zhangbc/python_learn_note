#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/19 22:36
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import sys

import pytest

from src.demo import Demo


params = [
    ('config_1', 'wangwu,18'),
    ('config_2', 'lisi,32'),
    ('config_3', 'zhangsan,33')]


class TestDemo:
    def setup_class(self, config='config_1', args='wangwu,33'):
        items = args.split(',')
        sys.argv.append(items[0])
        sys.argv.append(items[1])
        self.demo = Demo(config)
        print(f"setup class:Demo, {self.__name__}")

    @pytest.mark.parametrize('flag', ['flag_1', 'flag_2', 'flag_3'])
    def test_print(self, flag):
        self.demo.print(flag)
        print(id(self.demo), self.demo.name)

    @pytest.mark.parametrize('flag', ['flag_4', 'flag_5', 'flag_6'])
    def test_print_1(self, flag):
        self.demo.print(flag)
        print(id(self.demo), self.demo.name)

    @staticmethod
    def teardown_class():
        print("\nteardown class:Demo")


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_demo.py'])
