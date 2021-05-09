[TOC]

# Django 官方文档学习笔记

> 文档地址：https://docs.djangoproject.com/zh-hans/3.2/contents/
>
> 环境：`macOS10.13.1 + python3.7.3 + Django3.2`

本项目为 `Django3.2` 从零开始，记录学习中的点点滴滴。大致分为以下几部分：

## 1，快速入门

- [x] **从零开始：** [概要](https://docs.djangoproject.com/zh-hans/3.2/intro/overview/) | [安装](https://docs.djangoproject.com/zh-hans/3.2/intro/install/)
- [x] **入门教程：** [第 1 节：请求和响应](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial01/) | [第 2 节：模型和管理站点](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial02/) | [第 3 节：视图和模板](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial03/) | [第 4 节：表单和通用视图](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial04/) | [第 5 节：测试](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial05/) | [第 6 节：静态文件](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial06/) | [第 7 节：自定义管理站点](https://docs.djangoproject.com/zh-hans/3.2/intro/tutorial07/)
- [x] **进阶教程：** [如何编写可复用的应用](https://docs.djangoproject.com/zh-hans/3.2/intro/reusable-apps/) | [提交你的第一个 Django 补丁](https://docs.djangoproject.com/zh-hans/3.2/intro/contributing/)

## 2，模型层

`Django` 提供了一个抽象的模型（“`models`”）层，为了构建和操纵你的 `Web` 应用的数据。

- **模型：** [模型介绍](https://docs.djangoproject.com/zh-hans/3.2/topics/db/models/) | [字段类型](https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/) | [索引](https://docs.djangoproject.com/zh-hans/3.2/ref/models/indexes/) | [Meta 选项](https://docs.djangoproject.com/zh-hans/3.2/ref/models/options/) | [Model 类](https://docs.djangoproject.com/zh-hans/3.2/ref/models/class/)
- **QuerySet：** [执行查询](https://docs.djangoproject.com/zh-hans/3.2/topics/db/queries/) | [QuerySet 方法参考](https://docs.djangoproject.com/zh-hans/3.2/ref/models/querysets/) | [查询表达式](https://docs.djangoproject.com/zh-hans/3.2/ref/models/lookups/)
- **模型实例：** [实例方法](https://docs.djangoproject.com/zh-hans/3.2/ref/models/instances/) | [访问关联的对象](https://docs.djangoproject.com/zh-hans/3.2/ref/models/relations/)
- **迁移：** [迁移概述](https://docs.djangoproject.com/zh-hans/3.2/topics/migrations/) | [操作参考](https://docs.djangoproject.com/zh-hans/3.2/ref/migration-operations/) | [SchemaEditor](https://docs.djangoproject.com/zh-hans/3.2/ref/schema-editor/) | [编写迁移](https://docs.djangoproject.com/zh-hans/3.2/howto/writing-migrations/)
- **高级：** [管理器](https://docs.djangoproject.com/zh-hans/3.2/topics/db/managers/) | [原始 SQL](https://docs.djangoproject.com/zh-hans/3.2/topics/db/sql/) | [事务](https://docs.djangoproject.com/zh-hans/3.2/topics/db/transactions/) | [聚合](https://docs.djangoproject.com/zh-hans/3.2/topics/db/aggregation/) | [搜索](https://docs.djangoproject.com/zh-hans/3.2/topics/db/search/) | [自定义字段](https://docs.djangoproject.com/zh-hans/3.2/howto/custom-model-fields/) | [多个数据库](https://docs.djangoproject.com/zh-hans/3.2/topics/db/multi-db/) | [自定义查询](https://docs.djangoproject.com/zh-hans/3.2/howto/custom-lookups/) | [查询表达式](https://docs.djangoproject.com/zh-hans/3.2/ref/models/expressions/) | [条件表达式](https://docs.djangoproject.com/zh-hans/3.2/ref/models/conditional-expressions/) | [数据库函数](https://docs.djangoproject.com/zh-hans/3.2/ref/models/database-functions/)
- **其它：** [支持的数据库](https://docs.djangoproject.com/zh-hans/3.2/ref/databases/) | [旧数据库](https://docs.djangoproject.com/zh-hans/3.2/howto/legacy-databases/) | [提供初始化数据](https://docs.djangoproject.com/zh-hans/3.2/howto/initial-data/) | [优化数据库访问](https://docs.djangoproject.com/zh-hans/3.2/topics/db/optimization/) | [PostgreSQL 的特有功能](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/postgres/)

## 3，视图层

`Django` 具有 “视图” 的概念，负责处理用户的请求并返回响应。

- **基础：** [URL 配置](https://docs.djangoproject.com/zh-hans/3.2/topics/http/urls/) | [视图函数](https://docs.djangoproject.com/zh-hans/3.2/topics/http/views/) | [便捷工具](https://docs.djangoproject.com/zh-hans/3.2/topics/http/shortcuts/) | [装饰器](https://docs.djangoproject.com/zh-hans/3.2/topics/http/decorators/) | [异步支持](https://docs.djangoproject.com/zh-hans/3.2/topics/async/)
- **参考：** [内置视图](https://docs.djangoproject.com/zh-hans/3.2/ref/views/) | [请求／响应对象](https://docs.djangoproject.com/zh-hans/3.2/ref/request-response/) | [TemplateResponse 对象](https://docs.djangoproject.com/zh-hans/3.2/ref/template-response/)
- **文件上传：** [概览](https://docs.djangoproject.com/zh-hans/3.2/topics/http/file-uploads/) | [文件对象](https://docs.djangoproject.com/zh-hans/3.2/ref/files/file/) | [存储 API](https://docs.djangoproject.com/zh-hans/3.2/ref/files/storage/) | [管理文件](https://docs.djangoproject.com/zh-hans/3.2/topics/files/) | [自定义存储](https://docs.djangoproject.com/zh-hans/3.2/howto/custom-file-storage/)
- **基于类的视图：** [概览](https://docs.djangoproject.com/zh-hans/3.2/topics/class-based-views/) | [内置显示视图](https://docs.djangoproject.com/zh-hans/3.2/topics/class-based-views/generic-display/) | [内置编辑视图](https://docs.djangoproject.com/zh-hans/3.2/topics/class-based-views/generic-editing/) | [使用混入](https://docs.djangoproject.com/zh-hans/3.2/topics/class-based-views/mixins/) | [API 参考](https://docs.djangoproject.com/zh-hans/3.2/ref/class-based-views/) | [扁平化索引](https://docs.djangoproject.com/zh-hans/3.2/ref/class-based-views/flattened-index/)
- **高级：** [生成 CSV](https://docs.djangoproject.com/zh-hans/3.2/howto/outputting-csv/) | [生成 PDF](https://docs.djangoproject.com/zh-hans/3.2/howto/outputting-pdf/)
- **中间件：** [概览](https://docs.djangoproject.com/zh-hans/3.2/topics/http/middleware/) | [内建的中间件类](https://docs.djangoproject.com/zh-hans/3.2/ref/middleware/)

## 4，模板层

模板层提供了一个对设计者友好的语法用于渲染向用户呈现的信息。

- **基础：** [概述](https://docs.djangoproject.com/zh-hans/3.2/topics/templates/)
- **对于设计者：** [语法概述](https://docs.djangoproject.com/zh-hans/3.2/ref/templates/language/) | [内建标签及过滤器](https://docs.djangoproject.com/zh-hans/3.2/ref/templates/builtins/) | [人性化](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/humanize/)
- **对于开发者：** [模板 API](https://docs.djangoproject.com/zh-hans/3.2/ref/templates/api/) | [自定义标签和过滤器](https://docs.djangoproject.com/zh-hans/3.2/howto/custom-template-tags/) | [自定义模板后端](https://docs.djangoproject.com/zh-hans/3.2/howto/custom-template-backend/)

## 5，表单

`Django` 提供了一个丰富的框架来帮助创建表单和处理表单数据。

- **基础：** [概览](https://docs.djangoproject.com/zh-hans/3.2/topics/forms/) | [表单 API](https://docs.djangoproject.com/zh-hans/3.2/ref/forms/api/) | [内建字段](https://docs.djangoproject.com/zh-hans/3.2/ref/forms/fields/) | [内建部件](https://docs.djangoproject.com/zh-hans/3.2/ref/forms/widgets/)
- **进阶：** [针对模型的表单](https://docs.djangoproject.com/zh-hans/3.2/topics/forms/modelforms/) | [整合媒体](https://docs.djangoproject.com/zh-hans/3.2/topics/forms/media/) | [表单集](https://docs.djangoproject.com/zh-hans/3.2/topics/forms/formsets/) | [自定义验证](https://docs.djangoproject.com/zh-hans/3.2/ref/forms/validation/)

## 6，开发进程

- **设置：** [概览](https://docs.djangoproject.com/zh-hans/3.2/topics/settings/) | [完整的设置列表](https://docs.djangoproject.com/zh-hans/3.2/ref/settings/)
- **应用程序：** [概览](https://docs.djangoproject.com/zh-hans/3.2/ref/applications/)
- **异常：** [概览](https://docs.djangoproject.com/zh-hans/3.2/ref/exceptions/)
- **django-admin.py 和 manage.py：** [概览](https://docs.djangoproject.com/zh-hans/3.2/ref/django-admin/) | [添加自定义命令](https://docs.djangoproject.com/zh-hans/3.2/howto/custom-management-commands/)
- **测试：** [介绍](https://docs.djangoproject.com/zh-hans/3.2/topics/testing/) | [书写并运行测试](https://docs.djangoproject.com/zh-hans/3.2/topics/testing/overview/) | [包含的测试工具](https://docs.djangoproject.com/zh-hans/3.2/topics/testing/tools/) | [高级主题](https://docs.djangoproject.com/zh-hans/3.2/topics/testing/advanced/)
- **部署：** [概述](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/) | [WSGI 服务器](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/wsgi/) | [ASGI 服务器](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/asgi/) | [部署静态文件](https://docs.djangoproject.com/zh-hans/3.2/howto/static-files/deployment/) | [使用 email 追踪代码错误](https://docs.djangoproject.com/zh-hans/3.2/howto/error-reporting/) | [部署检查清单](https://docs.djangoproject.com/zh-hans/3.2/howto/deployment/checklist/)

## 7，管理

关于自动化管理界面的知识，`Django` 最受欢迎的特性之一：

- [管理站点](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/)
- [管理动作](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/actions/)
- [管理文档生成器](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/admindocs/)

## 8，安全

在 `Web` 应用的发展中，安全是最重要主题，`Django` 提供了多种保护手段和机制。

- [安全概览](https://docs.djangoproject.com/zh-hans/3.2/topics/security/)
- [在 Django 中披露的安全问题](https://docs.djangoproject.com/zh-hans/3.2/releases/security/)
- [点击劫持保护](https://docs.djangoproject.com/zh-hans/3.2/ref/clickjacking/)
- [跨站请求伪造 CSRF 保护](https://docs.djangoproject.com/zh-hans/3.2/ref/csrf/)
- [登录加密](https://docs.djangoproject.com/zh-hans/3.2/topics/signing/)
- [安全中间件](https://docs.djangoproject.com/zh-hans/3.2/ref/middleware/#security-middleware)

## 9，国际化和本地化

`Django` 提供了一个强大的国际化和本地化的框架, 可以在多语言和世界各地区进行应用程序的开发。

- [概览](https://docs.djangoproject.com/zh-hans/3.2/topics/i18n/) | [国际化](https://docs.djangoproject.com/zh-hans/3.2/topics/i18n/translation/) | [本地化](https://docs.djangoproject.com/zh-hans/3.2/topics/i18n/translation/#how-to-create-language-files) | [给 Web 界面及表单输入进行本地化](https://docs.djangoproject.com/zh-hans/3.2/topics/i18n/formatting/)
- [时区](https://docs.djangoproject.com/zh-hans/3.2/topics/i18n/timezones/)

## 10，性能和优化

有各种各样的技术和工具，可以帮助你的代码的运行更高效，更快和使用更少的系统资源.

- [性能和优化概述](https://docs.djangoproject.com/zh-hans/3.2/topics/performance/)

## 11，地理框架

[GeoDjango](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/gis/) 想要成为一个世界级的地理 `Web` 框架。尽可能简化构建 `GIS Web` 应用程序的流程，和利用空间化数据的能力是它的目标。

## 12，常用的 Web 应用程序工具

`Django` 提供了多种开发 `Web` 应用程序所需的常用工具。

- **认证：** [概述](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/) | [使用认证系统](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/default/) | [密码管理](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/passwords/) | [自定义认证](https://docs.djangoproject.com/zh-hans/3.2/topics/auth/customizing/) | [API 参考](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/auth/)
- [缓存](https://docs.djangoproject.com/zh-hans/3.2/topics/cache/)
- [日志](https://docs.djangoproject.com/zh-hans/3.2/topics/logging/)
- [发送邮件](https://docs.djangoproject.com/zh-hans/3.2/topics/email/)
- [资讯聚合 (RSS/Atom)](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/syndication/)
- [分页](https://docs.djangoproject.com/zh-hans/3.2/topics/pagination/)
- [消息框架](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/messages/)
- [序列化](https://docs.djangoproject.com/zh-hans/3.2/topics/serialization/)
- [会话](https://docs.djangoproject.com/zh-hans/3.2/topics/http/sessions/)
- [站点地图](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/sitemaps/)
- [静态文件管理](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/staticfiles/)
- [数据验证](https://docs.djangoproject.com/zh-hans/3.2/ref/validators/)

## 13，其它核心功能

- [有条件的内容处理](https://docs.djangoproject.com/zh-hans/3.2/topics/conditional-view-processing/)
- [内容类型和通用关系](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/contenttypes/)
- [简单页面](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/flatpages/)
- [重定向](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/redirects/)
- [信号](https://docs.djangoproject.com/zh-hans/3.2/topics/signals/)
- [系统检查框架](https://docs.djangoproject.com/zh-hans/3.2/topics/checks/)
- [站点框架](https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/sites/)
- [Django 中的 Unicode](https://docs.djangoproject.com/zh-hans/3.2/ref/unicode/)

## 14，Django 开源项目

- **社区：** [如何参与其中](https://docs.djangoproject.com/zh-hans/3.2/internals/contributing/) | [发布进程](https://docs.djangoproject.com/zh-hans/3.2/internals/release-process/) | [团队组织](https://docs.djangoproject.com/zh-hans/3.2/internals/organization/) | [Django 源代码仓库](https://docs.djangoproject.com/zh-hans/3.2/internals/git/) | [安全政策](https://docs.djangoproject.com/zh-hans/3.2/internals/security/) | [邮件列表](https://docs.djangoproject.com/zh-hans/3.2/internals/mailing-lists/)
- **设计哲学：** [概览](https://docs.djangoproject.com/zh-hans/3.2/misc/design-philosophies/)
- **文档：** [关于本文档](https://docs.djangoproject.com/zh-hans/3.2/internals/contributing/writing-documentation/)
- **第三方发行：** [概览](https://docs.djangoproject.com/zh-hans/3.2/misc/distributions/)
- **Django 时间线：** [API 稳定性](https://docs.djangoproject.com/zh-hans/3.2/misc/api-stability/) | [发行说明和升级说明](https://docs.djangoproject.com/zh-hans/3.2/releases/) | [过时时间表](https://docs.djangoproject.com/zh-hans/3.2/internals/deprecation/)