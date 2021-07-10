#!/usr/bin/env python
# coding:utf-8


"""

@Date:         2021/7/11 00:58
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
     1. 用来自动补充丈章、分类、标签、侧边栏、友链这些 Model 的 owner 字段
     2 . 用未针对 queryset 过滤当前用户的数据
    """

    exclude = ('owner', )

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
