[TOC]

# Django 文档学习笔记

> 学习地址：https://docs.djangoproject.com/zh-hans/3.2/contents/
>
> 环境：`macOS10.13.1 + python3.7.3 + Django3.2`

## 初识 Django

`Django` 最初被设计用于具有快速开发需求的新闻类站点，目的是要实现简单快捷的网站开发。

- 设计模型

`Django` 无需数据库就可以使用，它提供了 [对象关系映射器](https://en.wikipedia.org/wiki/Object-relational_mapping)，通过此技术，可以使用 `Python` 代码来描述数据库结构。

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

`Django` 中的视图的概念是 **一类具有相同功能和模板的网页的集合**。

- 编写更多的视图

`polls/views.py`

```python
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question {0}.".format(question_id))


def results(request, question_id):
    resp = "You're looking at the results of question {0}"
    return HttpResponse(resp.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {0}.".format(question_id))
```

`polls/urls.py`

```python
#!/usr/bin/env python
# coding:utf-8


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
```

每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 [`HttpResponse`](https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/#django.http.HttpResponse) 对象，或者抛出一个异常，比如 [`Http404`](https://docs.djangoproject.com/zh-hans/3.2/topics/http/views/#django.http.Http404) 。

`polls/views.py`

````python
from django.http import HttpResponse

from .models import Question


# Create your views here.
def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join(q.question_text for q in lastest_question_list)
    return HttpResponse(output)
````

首先，在 `polls` 目录里创建一个 `templates` 目录。`Django` 将会在这个目录里查找模板文件。

项目的 [`TEMPLATES`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TEMPLATES) 配置项描述了 `Django` 如何载入和渲染模板。默认的设置文件设置了 `DjangoTemplates` 后端，并将 [`APP_DIRS`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-TEMPLATES-APP_DIRS) 设置成了 `True`。这一选项将会让 `DjangoTemplates` 在每个 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/#std:setting-INSTALLED_APPS) 文件夹中寻找 “`templates`" 子目录。

在 `templates` 目录里，再创建一个目录 `polls`，然后在其中新建一个文件 `index.html` 。换句话说，你的模板文件的路径应该是 `polls/templates/polls/index.html` 。因为``app_directories`` 模板加载器是通过上述描述的方法运行的，所以 `Django` 可以引用到 `polls/index.html` 模板。

`polls/templates/polls/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Poll project</title>
</head>
<body>
    {% if latest_question_list %}
        <ul>
            {% for question in latest_question_list %}
                <li><a href="/polls/{{ question.id }}/">{{question.question_text}}</a></li>
            {% endfor %}
        </ul>
    {% else %}
        <p>
            No polls are available.
        </p>
    {% endif %}
</body>
</html>
```

更新视图 `polls/views.py`

```python
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    
    return HttpResponse(template.render(context, request))
```

`render()`：载入模板，填充上下文，再返回由它生成的 [`HttpResponse`](https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/#django.http.HttpResponse) 对象。

`polls/views.py`

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)
```

- 抛出 404 错误

`polls/views.py`

```python
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist!")
    
    return render(request, 'polls/detail.html', {'question': question})
```

`polls/templates/polls/detail.html`

```html
{{ question }}
```

`get_object_or_404()`：尝试用 [`get()`](https://docs.djangoproject.com/zh-hans/3.2/ref/models/querysets/#django.db.models.query.QuerySet.get) 函数获取一个对象，如果不存在就抛出 [`Http404`](https://docs.djangoproject.com/zh-hans/3.2/topics/http/views/#django.http.Http404) 错误。

`polls/views.py`

```python
from django.shortcuts import render, get_object_or_404

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

- 模板系统

去除模板中的硬编码 `URL`， `polls/templates/polls/index.html`：

```html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

为 `URL` 名称添加命名空间

`polls/urls.py`

```python
app_name = 'polls'
```

`polls/templates/polls/index.html`

```html
<li><a href="{% url 'polls:detail' question.id %}/">{{question.question_text}}</a></li>
```

## 编写你的第一个 Django 应用，第 4 部分

- 编写表单

`polls/templates/polls/detail.html`

```html
<h1>{{ question.question_text }}</h1>

{% if error_message %} <p><strong>{{ error_message }}</strong></p>
{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %}
  {% for choice in question.choice_set.all %}
  <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
  <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
  {% endfor %}
  <input type="submit" value="vote">
</form>
```

`polls/views.py`

```python
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))
```

```python
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
```

`polls/templates/polls/results.html`

```html
<h1>{{ question.question_text }}</h1>

<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }} -- {{ choice.votes }} vote {{ choice.votes |pluralize }}</li>
  {% endfor %}
</ul>
<a href="{% url 'polls:detail' question.id %}"> Vote again?</a>
```

- 使用通用视图

`Django` 提供一种快捷方式，叫做“**通用视图**”系统。

改良 `URLconf`：`polls/urls.py`

```python
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
```

改良视图：`polls/views.py`

```python
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
```

默认情况下，通用视图 [`DetailView`](https://docs.djangoproject.com/zh-hans/3.2/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) 使用一个叫做 `<app name>/<model name>_detail.html` 的模板；[`ListView`](https://docs.djangoproject.com/zh-hans/3.2/ref/class-based-views/generic-display/#django.views.generic.list.ListView) 使用一个叫做 `<app name>/<model name>_list.html` 的默认模板

## 编写你的第一个 Django 应用，第 5 部分

- 基本测试脚本编写

**自动化测试** 是由某个系统帮你自动完成的。当你创建好了一系列测试，每次修改应用代码后，就可以自动检查出修改后的代码是否还像你曾经预期的那样正常工作。

`Bug` 复现：

```shell
(/anaconda3) ☁  mysite [master] python manage.py shell 
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import datetime                                                                                                                

In [2]: from django.utils import timezone                                                                                              

In [3]: from polls.models import Question                                                                                              

In [4]: future_qestion = Question(pub_date=timezone.now() + datetime.timedelta(days=30))                                               

In [5]: future_qestion.was_published_recently()                                                                                        
Out[5]: True
```

创建测试：`polls/tests.py`

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        :return:
        """

        time_future = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time_future)
        self.assertIs(future_question.was_published_recently(), False)
```

运行测试：

```shell
(/anaconda3) ☁  mysite [master] ⚡  ppython manage.py test polls 
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/projects/demo_django/mysite/polls/tests.py", line 21, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

修复 `Bug`：`polls/models.py`

```python
def was_published_recently(self):
  time_now = timezone.now()
  return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= time_now
```

- 测试视图

`Django` 提供了一个供测试使用的 [`Client`](https://docs.djangoproject.com/zh-hans/3.2/topics/testing/tools/#django.test.Client) 来模拟用户和视图层代码的交互。

在 [`shell`](https://docs.djangoproject.com/zh-hans/3.2/ref/django-admin/#django-admin-shell) 中配置测试环境：

```shell
(/anaconda3) ☁  mysite [master] ⚡  ppython manage.py shell 
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from django.test.utils import setup_test_environment                                                                           

In [2]: setup_test_environment()                                                                                                       
```

导入 [`django.test.TestCase`](https://docs.djangoproject.com/zh-hans/3.2/topics/testing/tools/#django.test.TestCase) 类：

```shell
In [3]: from django.test import Client                                                                                                 

In [4]: client = Client()   
```

```shell
In [5]: response = client.get('/')                                                                                                     
Not Found: /

In [6]: response.status_code                                                                                                           
Out[6]: 404

In [7]: from django.urls import reverse                                                                                                

In [8]: response = client.get(reverse('polls:index'))                                                                                  

In [9]: response.status_code                                                                                                           
Out[9]: 200

In [10]: response.content                                                                                                              
Out[10]:  ....

In [11]: response.context                                                                                                              
Out[11]: [...]

In [12]: response.context_data                                                                                                         
Out[12]: 
{'paginator': None,
 'page_obj': None,
 'is_paginated': False,
 'object_list': <QuerySet [<Question: What's new?>]>,
 'latest_question_list': <QuerySet [<Question: What's new?>]>,
 'view': <polls.views.IndexView at 0x1098759b0>}


In [13]: response.context['latest_question_list']                                                                                      
Out[13]: <QuerySet [<Question: What's new?>]>

```

改善视图：`polls/views.py`

```python
from django.utils import timezone


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
```

```python
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        )
```

编写测试类：`polls/tests.py`

```python
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    :param question_text:
    :param days:
    :return:
    """

    t = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=t)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        :return:
        """

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        :return:
        """

        question = create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question]
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        :return:
        """

        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_future_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        :return:
        """

        question = create_question(question_text='Past question.', days=-30)
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question]
        )

    def test_two_past_question(self):
        """
        The questions index page may display multiple questions.
        :return:
        """

        question1 = create_question(question_text='Past question 1.', days=-30)
        question2 = create_question(question_text='Past question 2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1]
        )
```

关于测试的建议：

> 1）对于每个模型和视图都建立单独的 `TestClass`；
>
> 2）每个测试方法只测试一个功能；
>
> 3）给每个测试方法起个能描述其功能的名字。

## 编写你的第一个 Django 应用，第 6 部分

 `django.contrib.staticfiles` 存在的意义：将各个应用的静态文件（和一些你指明的目录里的文件）统一收集起来，这样一来，在生产环境中，这些文件就会集中在一个便于分发的地方。

- 自定义应用的界面和风格

在 `polls` 目录下创建一个名为 `static` 的目录，`Django` 将在该目录下查找静态文件。

在刚创建的 `static` 文件夹中创建一个名为 `polls` 的文件夹，再在 `polls` 文件夹中创建一个名为 `style.css` 的文件。

`polls/static/polls/style.css`：

```css
li a {
    color: green;
}

body {
    background: white url("images/background.gif") no-repeat;
}
```

`polls/templates/polls/index.html`：

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{% static 'polls/style.css' %}" type="text/css">
    <title>Poll project</title>
</head>
  ..........
</html>
```

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

3，修改 `git` 历史提交

解决方案：[git 修改已提交的内容](https://blog.csdn.net/sodaslay/article/details/72948722)

## 参考资料

- [zsh: command not found: gitk](https://www.jianshu.com/p/7c6577dec016)
- [git 修改已提交的内容](https://blog.csdn.net/sodaslay/article/details/72948722)

- [PyCharm 2021.1.1 激活码 安装教程 破解版下载 (亲测有用，永久激活，2021年4月30日更新~)](https://www.exception.site/essay/how-to-free-use-pycharm-2020)

