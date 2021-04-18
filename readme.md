[TOC]

# Django 文档学习笔记

> 学习地址：https://docs.djangoproject.com/zh-hans/3.2/contents/
>
> 环境：`macOS10.13.1 + python3.7.3 + Django3.2`

## 初识 Django

`Django` 最初被设计用于具有快速开发需求的新闻类站点，目的是要实现简单快捷的网站开发。

- 设计模型

`Django` 无需数据库就可以使用，它提供了 [对象关系映射器](https://en.wikipedia.org/wiki/Object-relational_mapping) 通过此技术，可以使用 `Python` 代码来描述数据库结构。

- 应用数据模型

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

该 [`makemigrations`](https://docs.djangoproject.com/zh-hans/3.2/ref/django-admin/#django-admin-makemigrations) 命令查找所有可用的模型，为任意一个在数据库中不存在对应数据表的模型创建迁移脚本文件。[`migrate`](https://docs.djangoproject.com/zh-hans/3.2/ref/django-admin/#django-admin-migrate) 命令则运行这些迁移来自动创建数据库表。

- 享用便捷的 `API`

- 一个动态管理接口：并非徒有其表

当模型完成定义，`Django` 就会自动生成一个专业的生产级 [管理接口](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/) ——一个允许认证用户添加、更改和删除对象的 `Web` 站点。

- 规划 `URLs`

- 编写视图

视图函数的执行结果只有两种：返回一个包含请求页面元素的 [`HttpResponse`](https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/#django.http.HttpResponse) 对象，或者是抛出 [`Http404`](https://docs.djangoproject.com/zh-hans/3.2/topics/http/views/#django.http.Http404) 这类异常。至于执行过程中的其它的动作则由你决定。

一个视图的工作就是：从参数获取数据，装载一个模板，然后将根据获取的数据对模板进行渲染。

- 设计模板

`Django` 允许设置搜索模板路径，这样可以最小化模板之间的冗余。在 `Django` 设置中，你可以通过 [`DIRS`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TEMPLATES-DIRS) 参数指定一个路径列表用于检索模板。如果第一个路径中不包含任何模板，就继续检查第二个，以此类推。

## 快速安装指南

- 安装 `Python`

- 设置数据库

- 安装 `Django`

```bash
(base) ☁  demo_django [master] ⚡  pip install django==3.2
>>> import django
>>> print(django.get_version())
3.2
```

## 编写你的第一个 Django 应用，第 1 部分

```bash
(base) ☁  demo_django [master] ⚡  python -m django --version
3.2
```



## 编写你的第一个 Django 应用，第 2 部分

## 编写你的第一个 Django 应用，第 3 部分

## 编写你的第一个 Django 应用，第 4 部分

## 编写你的第一个 Django 应用，第 5 部分

## 编写你的第一个 Django 应用，第 6 部分

## 编写你的第一个 Django 应用，第 7 部分

## 进阶指南：如何编写可重用程序

## 下一步看什么

## 编写你的第一个 Django 补丁

## 项目问题及解决方案

1，`zsh` 问题，具体描述如下：

```bash
(base) ☁  demo_django [master] gitk  
zsh: command not found: gitk
```

解决方案：[zsh: command not found: gitk](https://www.jianshu.com/p/7c6577dec016)

## 参考资料

- [zsh: command not found: gitk](https://www.jianshu.com/p/7c6577dec016)