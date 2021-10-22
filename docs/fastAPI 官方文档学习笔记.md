[TOC]

> 官网：https://fastapi.tiangolo.com/zh/tutorial/first-steps/
>
> 环境：`macOS10.13.1 + python3.7.3`

# 基本介绍

`FastAPI` 是一个用于构建 `API` 的现代、快速（高性能）的 `web` 框架，使用 `Python 3.6+` 并基于标准的 `Python` 类型提示。

关键特性：

> **快速**：可与 **`NodeJS`** 和 **`Go`** 比肩的极高性能（归功于 `Starlette` 和 `Pydantic`）；
>
> **高效编码**：提高功能开发速度约 200％ 至 300％；
>
> **更少 bug**：减少约 40％ 的人为（开发者）导致错误；
>
> **智能**：极佳的编辑器支持，处处皆可自动补全，减少调试时间；
>
> **简单**：设计的易于使用和学习，阅读文档的时间更短；
>
> **简短**：使代码重复最小化，通过不同的参数声明实现丰富功能，`bug` 更少；
>
> **健壮**：生产可用级别的代码，还有自动生成的交互式文档；
>
> **标准化**：基于（并完全兼容）`API` 的相关开放标准：`OpenAPI`(以前被称为 `Swagger`) 和 [`JSON Schema`](https://json-schema.org/)。

**Python 3.6+ 版本**加入了对"类型提示"的支持。

# 教程 - 用户指南

## 简介

```bash
# 安装所有的可选依赖及对应功能
(env3.7.3) (base) ☁  ~  pip install fastapi[all]

# 可以分开安装：1）安装fastapi 2）安装uvicorn
(env3.7.3) (base) ☁  ~  pip install fastapi
(env3.7.3) (base) ☁  ~  pip install uvicorn[standard]

# 运行实时服务器
(env3.7.3) (base) ☁  pro_fast_api [master] ⚡  uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [41212] using watchgod
INFO:     Started server process [41214]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

浏览器访问：

> `JSON` 响应：http://127.0.0.1:8000/
>
> 交互式 `API` 文档：http://127.0.0.1:8000/docs
>
> 可选的 `API` 文档：http://127.0.0.1:8000/redoc
>
> 查看 `openapi.json`：http://127.0.0.1:8000/openapi.json

开发 `API` 时，「路径」是用来分离「关注点」和「资源」的主要手段。

**操作**：指的是一种 `HTTP`「方法」。

> `POST`：创建数据；
>
> `GET`：读取数据；
>
> `PUT`：更新数据；
>
> `DELETE` ：删除数据。
>
> `OPTIONS`
>
> `HEAD`
>
> `PATCH`
>
> `TRACE`

所有的数据校验都由 [`Pydantic`](https://pydantic-docs.helpmanual.io/) 在幕后完成，如果你有一个接收路径参数的路径操作，但你希望预先设定可能的有效参数值，则可以使用标准的 `Python Enum` 类型。

## 路径参数

使用与 `Python` 格式化字符串相同的语法来声明路径"参数"或"变量"：

```python
@app.get('/items/{item_id}')
async def read_item(item_id):
    return {'item_id': item_id}
```

使用标准 `Python` 类型注释在函数中声明路径参数的类型：

```python
@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}
```

数据转换：也称为序列化，解析，编组，如运行此示例并在 `http://127.0.0.1:8000/items/3` 上打开浏览器，将看到以下响应：

```json
{
	"item_id": 3
}
```

数据验证：如运行此示例并在 `http://127.0.0.1:8000/items/foo` 上打开浏览器，将看到以下响应：

```json
{
	"detail": [{
		"loc": [
			"path",
			"item_id"
		],
		"msg": "value is not a valid integer",
		"type": "type_error.integer"
	}]
}
```

如果有一个接收路径参数的路径操作，但希望预定义可能的有效路径参数值，则可以使用标准 `Python` 的 `Enum`。



# 参考资料
