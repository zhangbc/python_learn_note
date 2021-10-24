#!/usr/bin/env python
# coding:utf-8


"""
web service demo
@Date:         2021/10/22 23:31
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
from fastapi import FastAPI
from pydantic import BaseModel

web = FastAPI()


@web.get('/')
async def index():
    return {'data': ['disen', 'jack', 'lucy']}


class LoginUser(BaseModel):
    phone: str
    code: str


class UsernameAndPassword(BaseModel):
    username: str
    password: str
    is_save: bool = False


@web.post('/login')
def user_login_by_phone(user: LoginUser):
    return {'message': '用户已登录', 'phone': user.phone}


@web.post('/login2')
def user_login_by_password(user: UsernameAndPassword):
    return {'message': f'用户登录失败， {user.username}用户不存在！'}
