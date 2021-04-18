# `Pecan` 学习笔记

> 官网：https://pecan.readthedocs.io/en/latest/#
> 环境：`macOS10.13.1 + python3.7.3 + pecan1.4.0`

## 概述

`Pecan`，是一个受 `CherryPy`、`TurboGears` 和 `Pylons` 启发的精益 `Python Web` 框架。`Pecan` 最初是由 [`ShootQ`](http://shootq.com/) 的开发人员在 [`Pictage`](http://shootq.com/) 工作时创建的。

- 安装

```bash
(env3.7.3) (base) ☁  python_learn_note [pecan] ⚡  pip install pecan
(env3.7.3) (base) ☁  python_learn_note [pecan] ⚡  pip list | grep pecan
pecan                         1.4.0
```

- 创建项目

```bash
(env3.7.3) (base) ☁  python_learn_note [pecan] ⚡  pecan create pro_pecan
```

- 运行应用程序

```bash
# 以开发者模式部署
(env3.7.3) (base) ☁  pro_pecan [pecan] ⚡  python setup.py develop
# 运行服务
(env3.7.3) (base) ☁  pro_pecan [pecan] ⚡  pecan serve config.py
```

- 测试

```bash
(env3.7.3) (base) ☁  pro_pecan [master] ⚡  python setup.py test -q
running test
running egg_info
creating pro_pecan.egg-info
writing pro_pecan.egg-info/PKG-INFO
writing dependency_links to pro_pecan.egg-info/dependency_links.txt
writing requirements to pro_pecan.egg-info/requires.txt
writing top-level names to pro_pecan.egg-info/top_level.txt
writing manifest file 'pro_pecan.egg-info/SOURCES.txt'
reading manifest file 'pro_pecan.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'pro_pecan.egg-info/SOURCES.txt'
running build_ext
....
----------------------------------------------------------------------
Ran 4 tests in 0.012s

OK
```

## 控制器 & 路由

`Pecan` 使用称为**对象分派**的路由策略将 `HTTP` 请求映射到控制器，然后再调用方法。`Object-dispatch` 首先将路径拆分为组件列表，然后从根控制器开始遍历对象路径。您可以将应用程序的控制器想象成一个对象树（对象树的分支直接映射到 `URL` 路径）。

