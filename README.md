[TOC]

# 项目文档

## 项目文件说明

- `CHANGELOG.md`：用来记录项目的变更，主要是针对每次发布版本的更新。 如果团队使用 `Git` 的话，其实也可以通过 `Git` 来生成。
- `LICENSE` ：如果是开源项目，可以增加这个文件来声明版权。  对于内部项目，不需要创建这个文件。 开源项目可以通过 `GitHub` 来自动创建。
- `README.md` ： 用来介绍项目的一些信息， 比如项目目的 、 开发背景、项目结构和依赖技术等项目参与人员需要了解的信息，它们能帮助大家更快地参与到项目里。
- `requirements.txt` ：这里面放了项目的依赖项 。 每次新增一个依赖，都需要把项目和对应版本放进去。

```bash
# 可以在文件的第一行增加如下语句，使用指定 PyPI 源
－i http://pypi.douban.com/simple/
# 从当前的 setup.py 中查找其他依赖项
-e .
```

## 项目相关命令

```bash
# 创建虚拟机
(django3.2) (base) ☁  typeidea python -m venv
# ～＝表示安装指定版本的最新版，这里会去安装 Django 1.11.x 版本， x 表示 1.11 版本的最新版的小版本号
(django3.2) (base) ☁  typeidea pip install django ~= l.11
# 创建项目
(django3.2) (base) ☁  typeidea  django-admin startproject typeidea
# 项目结构
(django3.2) (base) ☁  typeidea [master] tree
.
├── CHANGELOG.md
├── LICENSE
├── README.md
├── docs
├── requirements.txt
└── typeidea
    ├── db.sqlite3
    ├── manage.py
    └── typeidea
        ├── __init__.py
        ├── asgi.py
        ├── settings
        │   ├── __init__.py
        │   ├── base.py
        │   └── develop.py
        ├── urls.py
        └── wsgi.py
# 数据迁移
(django3.2) (base) ☁  typeidea [master] ⚡  python manage.py makemigrations
(django3.2) (base) ☁  typeidea [master] ⚡  python manage.py migrate
```

## 知识点摘要

1，`＃ NOQA` 这个注释的作用是 ， 告诉 `PEP 8` 规范检测工具 ，这个地方不需要检测。

2，常用的 `QuerySet` 接口

> `Django` 中的 `QuerySet` 本质上是一个 **懒加载** 的对象。

- 支持链式调用的接口

> `all` 接口： 相当于 `SELECT * FROM table_name` 语句，用于查询所有数据；
>
> `filter` 接口：根据条件过滤数据，常用的条件基本上是字段等于、不等于、 大于、小于。当然，还有其他的，比如能改成产生 `LIKE` 查询的：`Model.objects.filter(content_contains ＝ "条件")` ；
>
> `exclude` 接口：同 `filter` ，只是相反的逻辑；
>
> `reverse` 接口：把 `QuerySet` 中的结果倒序排列；
>
> `distinct` 接口：用来进行去重查询，产生 `SELECT DISTINCT` 这样的查询；
>
> `none` 接口：返回空的 `QuerySet`。

- 不支持链式调用的接口

>`get` 接口：比如 `Post.objects.get(id=1)` 用于查询 `id` 为 1 的文章：如果存在，则直接返回对应的 `Post` 实例；如果不存在， 则抛出 `DoesNotExist` 异常；
>
>`create` 接口：用来直接创建一个 `Model` 对象；
>
>`get_or_create` 接口：根据条件查找，如果没查找到，就调用 `create` 创建；
>
>`update_or_create` 接口：同 `get_or_create`，只是用来做更新操作；
>
>`count` 接口：用于返回 `QuerySet` 有多少条记录，相当于 `SELECT COUNT(*) FROM table_name`；
>
>`latest` 接口：用于返回最新的一条记录，但是需要在 `Model` 的 `Meta` 中定义：`get_latest_by = ＜用来排序的字段>`；
>
>`earliest` 接口：同 `latest` ，但是返回最早的一条记录；
>
>`first` 接口：从当前 `QuerySet` 记录中获取第一条；
>
>`last` 接口： 同`first` ，但是获取最后一条；
>
>`exists` 接口： 返回 True 或者 False ，在数据库层面执行 `SELECT (1 ) AS "a" FROM table_name L工MIT 1` 的查询，如果只是需要判断 `QuerySet` 是否有数据，用这个接口是最合适的方式。不要用 `count` 或者 `len(queryset)` 这样的操作来判断是否存在。 相反， 如果可以预期接下来会用到 `QuerySet` 中的数据，可以考虑使用 `len(queryset)` 的方式来做判断，这样可以减少一次 `DB` 查询请求；
>
> `bulk_create` 接口：同 `create`，用来批量创建记录；
>
>`in_bulk` 接口：批量查询，接收两个参数 `id_list`  和 `filed_name`；
>
>`update` 接口：用来根据条件批量更新记录，比如：`Post.objects.filter(owner_name='the5fire') .update(title ＝ '测试更新')` ；
>
>`delete` 接口：同 `update` ，用来根据条件批量删除记录。需要注意的是，`update` 和 `delete` 都会触发 `Dj ango` 的 `signal` ；
>
>`values` 接口：当我们明确知道只需要返回某个字段的值，不需要 `Model` 实例时，可以使用它，用法如下：
>
>```python
># 返回的结果包含 dict 的 QuerySet：＜QuerySet[{ ' title ’: xxx} ,	]>
>title_list= Post.objects.filter(category_id=1).values('title')
>```
>
>`values_list` 接口：同 `values` ，但是直接返回的是包含 `tuple` 的 `QuerySet` :
>
>```python
># 返回结果类似：＜QuerySet [('标题',)]>，flat=True 用于处理只是一个字段的情况
>titles_list = Post.objects.filter(category=1).values_list ('title', flat=True)
>```

- 进阶接口

> `defer` 接口：把不需要展示的字段做延迟加载；当需要用到这个字段时，在使用时会去加载；
>
> `only` 接口：同 `defer` 接口刚好相反，如果只想获取到所有的 `title` 记录，就可以使用 `only` ，只获取 `title` 的内容 ，其他值在获取时会产生额外的查询；
>
> `select_related` 接口：用来解决外键产生的 `N+I` 问题的方案；`N+1` 问题举例：
>
> ```python
> posts = Post.objects.all()
> for post in posts: # 产生数据库查询
>     print(post.owner)  # 产生额外的数据库查询
> ```
>
> 解决方案：
>
> ```python
> post = Post.objects.all().select_related('owner')
> for post in posts:  #产生数据库查询，owner 数据也会一次性查询出未
>     print(post.owner)
> ```
>
> `prefetch_related` 接口： 针对多对多关系的数据，解决 `N+1` 查询问题的方案。

3，常用的字段查询

> `contains` ：包含，用来进行相似查询；
>
> `icontains` ：同 `contains` ，只是忽略大小写；
>
> `exact` ：精确匹配；
>
> `iexact` ：同 `exact` ，忽略大小写；
>
> `in` ：指定某个集合，比如 `Post.objects.filter(id_in＝[1,2,3])` 相当于 `SELECT * FROM blog_post WHERE IN (1, 2, 3)`；
>
> `gt` ：大于某个值；
>
> `gte` ：大于等于某个值；
>
> `lt` ：小于某个值；
>
> `lte` ：小于等于某个值；
>
> `startswith` ：以某个字符串开头，与 `contains` 类似，只是会产生 `LIKE ‘<关键词>%’` 这样的 `SQL`；
>
> `istartswith` ：同 `startswith`，忽略大小写；
>
> `endswith` ：以某个字符串结尾；
>
> `iendswith` ：同 `endswith` ，忽略大小写；
>
> `range` ：范围查询，多用于时间范围。

- 进阶查询

> $F$：$F$ 表达式常用来执行数据库层面的计算，从而避免出现竞争状态；
>
> ```python
> from django.db.models import F
>
> post = Post.objects .get(id=l)
> post.pv = F ('pv') + 1
> post. save ()
> ```
>
> $Q$ ：$Q$ 表达式就是用来解决多条件查询的；
>
> ```python
> from django.db.models import Q
>
> Post.objects.filter(Q(id=1) | Q(id=2))
> Post.objects.filter(Q(id=1) & Q(id=2))
> ```
>
> $Count$ ：用来做聚合查询；
>
> ```python
> from django.db.mdoels import Count
>
> categories = Category.objects.annotate(posts_count=Count('post'))
> print(categories[0].posts_count)
> ```
>
> $Sum$ ：同 $Count$ 类似，只是它是用来做合计的。
>
> ```python
> from django db.models import Sum
>
> Post.objects.aggregate(all_pv=Sum('pv'))
> ```

`reverse` 函数的作用是通过 `name` 反向解析成 `URL`。

`Django` 提供了下面几个 `class-based view`：

> `View` ：基础的 `View` ，实现了基于 `HTTP` 方法的分发（ `dispatch` ）逻辑，比如 `GET` 请求会调用对应的 `get` 方法，`POST` 请求会调用对应的 `post` 方法，但没有实现具体的 `get` 或者 `post` 方法；
>
> `TemplateView`：继承自 `View`，可以直接用来返回指定的模板。 它实现了 `get` 方法，可以传递变量到模板中来进行数据展示；
>
> `DetailView` ：继承自 `View`，实现了 `get` 方法，并且可以绑定某一个模板，用来获取单个实例的数据；
>
> `ListView`：继承自 `View`，实现了 `get` 方法，可以通过绑定模板来批量获取数据。

# 博客项目

> 博客是一个与他人分享和交流的平台，通过书写自己的想法、学习技巧和工作经验，来结 识不同领域的读者，交流和探讨技术、思想、文化或公司等话题。

## 总体需求

博客系统分为两部分：读者访问部分（用户端）和作者创作部分（作者端）。

- 用户端的需求

> 1）要能够通过搜索引擎搜索到博客内容，进而来到博客；
>
> 2）可在博客中进行关键词搜索，然后展示出文章列表；
>
> 3）能够根据某个分类查看所有关于这一分类的文章；
>
> 4）访问首页时，需要能看到由新到旧的文章列表，以便于查看最新的文章；
>
> 5）要能够通过 `RSS` 阅读器订阅博主的文章；
>
> 6）要能够对某一篇文章进行评论；
>
> 7）能够配置友链，方便与网友进行链接。

- 作者端的需求

> 1）博客后台需要登录方可进入；
>
> 2）能够创建分类和标签；
>
> 3）能够以 `Markdown` 格式编写文章；
>
> 4）能够上传文章配图，要有版权声明；
>
> 5）能够配置导航，以便引导读者；
>
> 6）作者更新后，订阅读者能够收到通知 。

- 需求评审目的

> 1）明确所有的需求点，避免出现理解上的歧义；
>
> 2）确认技术可行性，避免延期或者后面再修改需求；
>
> 3）确认工期，是否需要分期开发。



## TODO

- `mkdocs` ：部署内网在线的文档系统
