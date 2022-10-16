#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/16 23:04
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""


def calculator(type_calc: int, float_n1: float, float_n2: float) -> float:
    """
    运算器
    :param type_calc: 操作符参数
    :param float_n1: 第一个运算数
    :param float_n2: 第二个运算数
    :return: 运算结果
    """
    if type_calc == 1:
        ans = float_n1 + float_n2
    elif type_calc == 2:
        ans = float_n1 - float_n2
    elif type_calc == 3:
        ans = float_n1 * float_n2
    else:
        ans = float_n1 / float_n2

    return ans
