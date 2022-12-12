#!/usr/bin/env python
# coding:utf-8

"""

@Date:    2022/10/20 01:47
@Author:  zhangbc
@Version: 1.0.0
@Contact: zhangbocheng189@163.com
@Description:
"""
import pytest


# def pytest_addoption(parser):
#     parser.addoption(
#         "--config", action="setup_class", default="", help="option: chrome, safari, firefox"
#     )
#     parser.addoption(
#         "--argv", action="setup_class", default="", help="option: dev, stage, local"
#     )


@pytest.fixture(scope='session')
def setup_opts(request):
    config = request.config.getoption("--config")
    argv = request.config.getoption("--argv")
    setup = [str(config), str(argv)]
    yield setup
