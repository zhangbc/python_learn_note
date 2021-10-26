from enum import Enum
from typing import Optional, List

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


fake_items_db = [{"item_name": "Foo"},
                 {"item_name": "Bar"},
                 {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})

    return item_dict


@app.get('/item/{item_id}')
async def read_item(item_id: int, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item


@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
    item = {'item_id': item_id}
    if q:
        item.update({'q': q})

    if not short:
        item.update({
            'description': 'This is an amazing item that has a long description.'
        })

    return item


@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})

    if not short:
        item.update({
            'description': 'This is an amazing item that has a long description.'
        })

    return item


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item_name': item.name}


@app.get('/items/')
async def read_item(q: Optional[str] = Query(None, min_length=3,
                                             max_length=50, regex="^fixed-query$"),
                    skip: int = 0, limit: int = 10):
    results = {"items": fake_items_db[skip: skip + limit]}
    if q:
        results.update({'q': q})

    return results


@app.get('/item_list/')
async def read_items(q: Optional[List[str]] = Query(None, title='Query String',
                                                    min_length=3, max_length=50,
                                                    alias='item-query', deprecated=True)):
    query_items = {'q': q}
    return query_items


@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        message = 'Deep Learning FTW!'
    elif model_name.value == 'lenet':
        message = 'LeCNN all the images'
    else:
        message = 'Have some residuals'

    return {'model_name': model_name, 'message': message}


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


@app.get('/items_path/{item_id}')
async def read_items(
        item_id: int = Path(..., title='The ID of the item to get'),
        q: Optional[str] = Query(None, alias='item-query')
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})

    return results


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
