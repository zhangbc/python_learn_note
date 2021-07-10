#!/usr/bin/env python
# coding:utf-8


"""

@Date:         2021/7/10 23:28
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:
"""
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
