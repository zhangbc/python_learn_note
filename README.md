[TOC]

# 项目文档

## 项目文件说明

- `CHANGELOG.md`：用来记录项目的变更，主要是针对每次发布版本的更新。 如果团队使用 `Git` 的话，其实也可以通过 `Git` 来生成。
- `LICENSE` ：如果是开源项目，可以增加这个文件来声明版权。  对于内部项目，不需要创建这个文件。 开源项 目可以通过 `GitHub` 来自动创建。 
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
```

## 知识点摘要

1，`＃ NOQA` 这个注释的作用是 ， 告诉 `PEP 8` 规范检测工具 ，这个地方不需要检测。

## TODO

- `mkdocs` ：部署内网在线的文档系统
