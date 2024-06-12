from fastapi import FastAPI
from pydantic import BaseModel,Field
from datetime import datetime
from db import CRUD

app = FastAPI(
    title= "URL shortener",
    description= "A simple API built using AppWrite's db",
    docs_url="/"
)

crud = CRUD()



class TodoCreateModel(BaseModel):
    name :str
    short_url: str
    url: str
    date_added: str = Field(default=datetime.utcnow().isoformat())


class TodoUpdateModel(BaseModel):
    name :str
    short_url: str
    url: str
    date_added: str = Field(default=datetime.utcnow().isoformat())


@app.get('/url-shortener')
async def get_all_todos():
    result = crud.list_todos()

    return result

@app.get('/url-shortener/{id}')
async def get_todo(id:str):
    result = crud.retrieve_todo(id)

    return result


@app.post('/create-url-shortener',status_code=200)
async def create_todo(todo_data :TodoCreateModel):
    result = crud.create_todo(data= {
        'name' :todo_data.name,
        'short_url' :todo_data.short_url,
        'url' :todo_data.url,
        'date_added':todo_data.date_added
    })

    return result


@app.patch('/update-url-shortener/{todo_id}')
async def Update_todo(todo_id:str,update_data: TodoUpdateModel):
    result = crud.update_todo(
        todo_id=todo_id,
        data = {
            'name' : update_data.name,
            'short_url' :update_data.short_url,
            'url' :update_data.url,
            'date_added':update_data.date_added
        }
    )

    return result


# @app.delete('/todo/{todo_id}',status_code=204)
# async def get_all_todos(todo_id:str):
#     result = crud.delete_todo(
#         todo_id=todo_id
#     )

#     return result