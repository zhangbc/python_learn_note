#!/usr/bin/env python
# coding:utf-8


"""

@Date:         2021/10/24 12:21
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
import hashlib
import uuid

from fastapi import FastAPI, Query
from webservers.db import query

user_app = FastAPI(title='爱读书App接口服务',
                   version='1.0',
                   description="面向App, 提交数据的API接口，包含会员、搜索、分类、活动、积分、评论、我的书架、广告等")


@user_app.get('/login')
async def user_login_get(name: str = Query(..., min_length=4, max_length=20, regex=r'^[a-zA-Z]+$'),
                         pwd: str = Query(..., min_length=3, max_length=20)):
    res = query('user', 'id', 'phone', 'nick_name', 'avatar', 'active',
                where='username=%s and auth_string=%s',
                args=(name, hashlib.sha1(pwd.encode('utf8')).hexdigest()),
                one=True)
    if res:
        if not res['active']:
            return {'message': '当前用户未激活，请先激活', 'url': f'/active/{res["id"]}'}

        res['username'] = name
        res['token'] = uuid.uuid4().hex
        # TODO: token & user_id 存储到缓存中
        return {'message': '登录成功', 'data': res}

    return {'user': {
        'name': name,
        'auth_string': f'{pwd}({hashlib.sha1(pwd.encode("utf8")).hexdigest()})',
    },
        'message': '登录失败，用户名或口令错误'}
