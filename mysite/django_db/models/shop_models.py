#!/usr/bin/env python
# coding:utf-8


"""

@Date:         2021/8/29 20:57 
@Author:       zhangbocheng
@Version:      1.0.0
@Contact:      zhangbocheng189@163.com
@Description:  
"""
from django.db import models


class ShopAuthor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'shop_author'


class ShopPublisher(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'shop_publisher'


class ShopBook(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(ShopAuthor)
    publisher = models.ForeignKey(ShopPublisher, on_delete=models.CASCADE)
    pub_date = models.DateField()

    class Meta:
        db_table = 'shop_book'


class ShopStore(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(ShopBook)

    class Meta:
        db_table = 'shop_store'
