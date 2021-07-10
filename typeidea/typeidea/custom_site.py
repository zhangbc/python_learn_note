#!/usr/bin/env python
# coding:utf-8


"""

@Date:         2021/7/10 23:46
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = "Typeidea 管理后台"
    index_title = "首页"


custom_site = CustomSite(name='cus_admin')
