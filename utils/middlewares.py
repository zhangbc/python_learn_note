#!/usr/bin/env python
# coding:utf-8

"""

@Date:         2021/9/29 02:44
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""

from functools import wraps

from funcsigs import signature


def typeassert(*ty_args, **ty_kwargs):
    """
    type checker
    :param ty_args:
    :param ty_kwargs:
    :return:
    """

    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {0} must be {1}'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorate
