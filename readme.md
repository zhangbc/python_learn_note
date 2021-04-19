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

> `route`：是一个匹配 `URL` 的准则。当 `Django` 响应一个请求时，它会从 `urlpatterns` 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项，注意：这些准则不会匹配 `GET` 和 `POST` 参数或域名；
>
> `view`：当 `Django` 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 [`HttpRequest`](https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/#django.http.HttpRequest) 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入；
>
> `kwargs`：任意个关键字参数可以作为一个字典传递给目标视图函数；
>
> `name` ：为 `URL` 取名能使你在 `Django` 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 `URL` 模式。

## 编写你的第一个 Django 应用，第 2 部分

- 数据库配置

> - [`ENGINE`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-DATABASE-ENGINE) -- 可选值有 `'django.db.backends.sqlite3'`，`'django.db.backends.postgresql'`，`'django.db.backends.mysql'`，或 `'django.db.backends.oracle'`。其它 [可用后端](https://docs.djangoproject.com/zh-hans/3.2/ref/databases/#third-party-notes)。
> - [`NAME`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-NAME) -- 数据库的名称。如果你使用 `SQLite`，数据库将是一个文件，在这种情况下，[`NAME`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-NAME) 应该是此文件完整的绝对路径，包括文件名。默认值 `BASE_DIR / 'db.sqlite3'` 将把数据库文件储存在项目的根目录。

编辑 `mysite/settings.py` 文件前，先设置 [`TIME_ZONE`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TIME_ZONE) 为你自己时区。

 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-INSTALLED_APPS) 默认包括了以下 `Django` 的自带应用：

> [`django.contrib.admin`](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/#module-django.contrib.admin) -- 管理员站点；
>
> [`django.contrib.auth`](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/#module-django.contrib.auth) -- 认证授权系统；
>
> [`django.contrib.contenttypes`](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/contenttypes/#module-django.contrib.contenttypes) -- 内容类型框架；
>
> [`django.contrib.sessions`](https://docs.djangoproject.com/zh-hans/3.2/topics/http/sessions/#module-django.contrib.sessions) -- 会话框架；
>
> [`django.contrib.messages`](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/messages/#module-django.contrib.messages) -- 消息框架；
>
> [`django.contrib.staticfiles`](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/staticfiles/#module-django.contrib.staticfiles) -- 管理静态文件的框架。

创建数据表：

```bash
(base) ☁  mysite [master] ⚡  python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

- 创建模型

模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为。`Django` 遵循 [DRY Principle](https://docs.djangoproject.com/zh-hans/3.2/misc/design-philosophies/#dry) 。它的目标是开发者只需要定义数据模型，然后其它的杂七杂八代码都不用关心，它们会自动从模型生成。

`Django` 的迁移代码是由你的模型文件自动生成的，它本质上是个历史记录，`Django` 可以用它来进行数据库的滚动更新，通过这种方式使其能够和当前的模型匹配。

`polls/models.py`

```python
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

每个模型被表示为 [`django.db.models.Model`](https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/#django.db.models.Model) 类的子类。每个模型有许多类变量，它们都表示模型里的一个数据库字段。

每个字段都是 [`Field`](https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#django.db.models.Field) 类的实例 - 比如，字符字段被表示为 [`CharField`](https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#django.db.models.CharField) ，日期时间字段被表示为 [`DateTimeField`](https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#django.db.models.DateTimeField) 。这将告诉 `Django` 每个字段要处理的数据类型。

每个 [`Field`](https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#django.db.models.Field) 类实例变量的名字（例如 `question_text` 或 `pub_date` ）也是字段名，所以最好使用对机器友好的格式。你将会在 `Python` 代码里使用它们，而数据库会将它们作为列名。

- 激活模型

`mysite/settings.py`

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

执行项目迁移命令：

```bash
(base) ☁  mysite [master] ⚡  python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

[`sqlmigrate`](https://docs.djangoproject.com/zh-hans/3.2/ref/django-admin/#django-admin-sqlmigrate) 命令接收一个迁移的名称，然后返回对应的 `SQL`：

```bash
(base) ☁  mysite [master] ⚡  python manage.py sqlmigrate polls 0001
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

项目检查：

```python
(base) ☁  mysite [master] ⚡  python manage.py check
System check identified no issues (0 silenced).
```

运行迁移命令：

```bash
(base) ☁  mysite [master] ⚡  python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```

- 初识 `API`

```bash
(base) ☁  mysite [master] ⚡  python manage.py shell
In [1]: from polls.models import Choice, Question

In [2]: Question.objects.all()
Out[2]: <QuerySet []>

In [3]: from django.utils import timezone

In [4]: q = Question(question_text="What's new?", pub_date=timezone.now())

In [5]: q.save()

In [6]: q.id
Out[6]: 1

In [7]: q.question_text
Out[7]: "What's new?"

In [8]: q.pub_date
Out[8]: datetime.datetime(2021, 4, 19, 15, 57, 42, 13321, tzinfo=<UTC>)

In [9]: q.question_text="What's up?"

In [10]: Question.objects.all()
Out[10]: <QuerySet [<Question: Question object (1)>]>
```

`polls/models.py`

```python
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

```bash
In [1]: from polls.models import Choice, Question

In [2]: Question.objects.all()
Out[2]: <QuerySet [<Question: What's new?>]>

In [3]: Question.objects.filter(id=1)
Out[3]: <QuerySet [<Question: What's new?>]>

In [6]: from django.utils import timezone

In [7]: current_year = timezone.now().year

In [8]: Question.objects.get(pub_date__year=current_year)
Out[8]: <Question: What's new?>

In [11]: q = Question.objects.get(pk=1)

In [12]: q.was_published_recently()
Out[12]: True

In [22]: c=q.choice_set.filter(choice_text__startswith='Just hacking')

In [23]: c.delete()
Out[23]: (1, {'polls.Choice': 1})
```

- 介绍 `Django` 管理页面

创建管理员账号：

```bash
(base) ☁  mysite [master] ⚡  python manage.py createsuperuser
Username (leave blank to use 'zhangbocheng'): admin
Email address: admin@os-easy.com
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

启动服务：

```bash
(base) ☁  mysite [master] ⚡  python manage.py runserver 8080
```

向管理页面中加入投票应用：

`polls/admin.py`

```python
from django.contrib import admin
from .models import Question


# Register your models here.
admin.site.register(Question)
```

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