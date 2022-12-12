#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/19 22:29
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import sys


class Demo:
    def __init__(self, config):
        self.config = config
        self.name = sys.argv[1]
        self.age = sys.argv[2]

    def print(self, flag):
        print(f'Demo config: {self.config}, '
              f'name: {self.name}, '
              f'age: {self.age},'
              f'flag: {flag}')


if __name__ == '__main__':
    sys.argv.append('zhangbc')
    sys.argv.append('33')
    print(sys.argv)
    demo = Demo('config_demo')
    demo.print('ok')
