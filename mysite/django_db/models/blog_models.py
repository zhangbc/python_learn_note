#!/usr/bin/env python
# coding:utf-8


"""

@Date:         2021/8/28 21:47 
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:  
"""
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tag_line = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'web_blog'


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'web_author'


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    head_line = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.head_line

    class Meta:
        db_table = 'web_entry'
