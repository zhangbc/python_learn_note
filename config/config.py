#! /usr/bin/env python
# coding: utf-8


import os
from os import makedirs, path
from os.path import dirname

from config import config_default, config_offline, config_online, env

configs = config_default.configs
LOG_FILE = 'logs'
LOG_FILE = os.path.join(os.path.dirname(os.path.realpath(dirname(__file__))), LOG_FILE)

try:
    ONLINE = env.ENV and env.ENV == 'online'
    OFFLINE = env.ENV and env.ENV == 'offline'

    if ONLINE:
        configs = config_online.configs
    elif OFFLINE:
        configs = config_offline.configs

    for f in configs['pid'].values():
        base_dir = dirname(f)
        if not path.isdir(base_dir):
            makedirs(base_dir)

    if not path.isdir(LOG_FILE):
        makedirs(LOG_FILE)

except ImportError:
    pass
