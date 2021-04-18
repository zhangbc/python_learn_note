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

查看 `Django` 版本：

```bash
(base) ☁  demo_django [master] ⚡  python -m django --version
3.2
```

创建项目：

```bash
(base) ☁  demo_django [master] django-admin startproject mysite
```

```
mysite/              ：项目的容器
    manage.py        ：管理 Django 项目的命令行工具
    mysite/          ：项目包，纯 Python 包
        __init__.py  ：空文件，告诉 Python 这个目录应该被认为是一个 Python 包
        settings.py  ：项目的配置文件
        urls.py      ：项目的 URL 声明
        asgi.py      ：项目运行在 ASGI 兼容的 Web 服务器上的入口
        wsgi.py      ：项目运行在 WSGI 兼容的Web服务器上的入口
```

运行项目：

```bash
(base) ☁  mysite [master] ⚡  python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
April 18, 2021 - 15:57:47
Django version 3.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

# or
(base) ☁  mysite [master] ⚡  python manage.py runserver 8080
```

- 创建投票应用

在 `Django` 中，每一个应用都是一个 `Python` 包，并且遵循着相同的约定。`Django` 自带一个工具，可以帮你生成应用的基础目录结构。

> 应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序；
>
> 项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。

创建 `polls` 应用：

```bash
(base) ☁  mysite [master] ⚡  python manage.py startapp polls
```

编写视图：

1）`polls/views.py`

```python
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

2）`polls/urls.py`

```python
#!/usr/bin/env python
# coding:utf-8


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]
```

3）`mysite/urls.py`

```python
from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path(r'polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

函数 [`path()`](https://docs.djangoproject.com/zh-hans/3.2/ref/urls/#django.urls.path) 具有四个参数，两个必须参数：`route` 和 `view`，两个可选参数：`kwargs` 和 `name`。

> `route` 是一个匹配 `URL` 的准则。当 `Django` 响应一个请求时，它会从 `urlpatterns` 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项，注意：这些准则不会匹配 `GET` 和 `POST` 参数或域名；
>
> 当 `Django` 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 [`HttpRequest`](https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/#django.http.HttpRequest) 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入；
>
> `kwargs`：任意个关键字参数可以作为一个字典传递给目标视图函数；
>
> `name` ：为 `URL` 取名能使你在 `Django` 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 `URL` 模式。

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

2，关联远程仓库

```bash
(base) ☁  demo_django [master] git remote add origin git@github.com:zhangbc/demo_django.git
(base) ☁  demo_django [master] git push origin master
```



## 参考资料

- [zsh: command not found: gitk](https://www.jianshu.com/p/7c6577dec016)