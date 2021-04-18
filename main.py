from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}


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
