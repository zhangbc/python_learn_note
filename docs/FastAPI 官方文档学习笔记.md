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

`FastAPI` 站在以下巨人的肩膀之上：

- [`Starlette`](https://www.starlette.io/) 负责 `web` 部分。
- [`Pydantic`](https://pydantic-docs.helpmanual.io/) 负责数据部分。

# 教程 - 用户指南

## 简介

```bash
# 安装所有的可选依赖及对应功能
(env3.7.3) (base) ☁  ~  pip install fastapi[all]

# 可以分开安装：1）安装fastapi 2）安装uvicorn
(env3.7.3) (base) ☁  ~  pip install fastapi
(env3.7.3) (base) ☁  ~  pip install uvicorn[standard]

# 运行实时服务器
(env3.7.3) (base) ☁  python_learn_note [master] ⚡  uvicorn main:app --reload
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

可选依赖：

> 用于 `Pydantic`：
>
> > - [`ujson`](https://github.com/esnme/ultrajson) - 更快的 `JSON` 「解析」；
> > - [`email_validator`](https://github.com/JoshData/python-email-validator) - 用于 `email` 校验。
>
> 用于 `Starlette`：
>
> > - [`requests`](https://requests.readthedocs.io/) - 使用 `TestClient` 时安装；
> > - [`aiofiles`](https://github.com/Tinche/aiofiles) - 使用 `FileResponse` 或 `StaticFiles` 时安装；
> > - [`jinja2`](https://jinja.palletsprojects.com/) - 使用默认模板配置时安装；
> > - [`python-multipart`](https://andrew-d.github.io/python-multipart/) - 需要通过 `request.form()` 对表单进行「解析」时安装；
> > - [`itsdangerous`](https://pythonhosted.org/itsdangerous/) - 需要 `SessionMiddleware` 支持时安装；
> > - [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) - 使用 `Starlette` 提供的 `SchemaGenerator` 时安装；
> > - [`graphene`](https://graphene-python.org/) - 需要 `GraphQLApp` 支持时安装；
> > - [`ujson`](https://github.com/esnme/ultrajson) - 使用 `UJSONResponse` 时安装。
>
> 用于 `FastAPI / Starlette`：
>
> > - [`uvicorn`](https://www.uvicorn.org/) - 用于加载和运行你的应用程序的服务器；
> > - [`orjson`](https://github.com/ijl/orjson) - 使用 `ORJSONResponse` 时安装。

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

```python
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'
```

> [枚举（或 `enums`）](https://docs.python.org/3/library/enum.html)从 3.4 版本起在 `Python` 中可用。

使用定义的枚举类（`ModelName`）创建一个带有类型标注的*路径参数*：

```python
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        message = 'Deep Learning FTW!'
    elif model_name.value == 'lenet':
        message = 'LeCNN all the images'
    else:
        message = 'Have some residuals'

    return {'model_name': model_name, 'message': message}

```

使用直接来自 `Starlette` 的选项来声明一个包含*路径*的*路径参数*。

按需对参数排序：（两种方案）

> 1）对参数重新排序，并将不带默认值的值（查询参数 `q`）放到最前面；对 `FastAPI 来说将通过参数的名称、类型和默认值声明（`Query`、`Path` 等）来检测参数，而不在乎参数的顺序；
>
> 2）传递 `*` 作为函数的第一个参数。

- 数值校验

```python
@app.get('/items_path_number/{item_id}')
async def read_items(
        *,
        item_id: int = Path(..., title='The ID of the item to get', ge=1, le=100),
        q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})

    return results
```

> - `gt`：大于（`g`reater `t`han）
> - `ge`：大于等于（`g`reater than or `e`qual）
> - `lt`：小于（`l`ess `t`han）
> - `le`：小于等于（`l`ess than or `e`qual）

## 查询参数

声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数；

查询参数不是路径的固定部分，因此它们可以是可选的，并且可以有默认值；

可以同时声明多个路径参数和查询参数，`FastAPI` 能够识别它们。

- 额外校验

```python
@app.get('/items/')
async def read_item(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$"), skip: int = 0, limit: int = 10):
    results = {"items": fake_items_db[skip: skip + limit]}
    if q:
        results.update({'q': q})

    return results
```

当你使用 `Query` 显式地定义查询参数时，你还可以声明它去接收一组值，或换句话来说，接收多个值。

- 别名参数

```python
@app.get('/item_list/')
async def read_items(q: Optional[List[str]] = Query(None, min_length=3, max_length=50, alias='item-query')):
    query_items = {'q': q}
    return query_items
```

- 弃用参数

现在假设不再喜欢此参数，不得不将其保留一段时间，因为有些客户端正在使用它，但又希望文档清楚地将其展示为已弃用。那么将参数 `deprecated=True` 传入 `Query`：

```python
@app.get('/item_list/')
async def read_items(q: Optional[List[str]] = Query(None, title='Query String',
                                                    min_length=3, max_length=50,
                                                    alias='item-query', deprecated=True)):
    query_items = {'q': q}
    return query_items
```

## 请求体

`FastAPI` 将识别出与路径参数匹配的函数参数应 **从路径中获取**，而声明为 `Pydantic` 模型的函数参数应 **从请求体中获取**；

可以同时声明**请求体**、**路径参数**和**查询参数**，`FastAPI` 会识别它们中的每一个，并从正确的位置获取数据。



## `Header & Cookie` 参数

##  响应模型


# 参考资料
