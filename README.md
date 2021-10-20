[TOC]

# 项目说明

> 本项目为 `Python` 知识学习库

## `Django` 官方文档

## `FastAPI` 官方文档

## `pecan` 官方文档

## `typeidea`（`blog`）项目

## openstack 学习笔记

# 常见问题

## 1，分支整体迁移问题

> 将 `typeidea` 仓库的 `master` 分支迁移至 `python_learn_note` 仓库的 `typeidea` 分支下

```bash
# 设置 `typeidea` 仓库的远程关联仓库
(django3.2) (base) ☁  typeidea [master] git remote add origin git@github.com:zhangbc/python_learn_note.git
# 创建分支
(django3.2) (base) ☁  typeidea [master] git branch typeidea
# 切换分支
(django3.2) (base) ☁  typeidea [master] git checkout typeidea
# push提交
(django3.2) (base) ☁  typeidea [master] git push origin typeidea
# pull同步本地
(django3.2) (base) ☁  typeidea [master] git pull --rebase
# 处理冲突
# 设置关联分支
(django3.2) (base) ☁  typeidea [master] git branch --set-upstream-to=origin/typeidea typeidea
# 再次pull同步
(django3.2) (base) ☁  typeidea [master] git pull --rebase
# 再次push提交
(django3.2) (base) ☁  typeidea [master] git push origin typeidea
```
