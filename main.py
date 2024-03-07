from fastapi import FastAPI
from models import ToDo

app=FastAPI()

@app.get('/')
async def root():
    return{"message":"Hello World"}

todos=[]
@app.get('/todos')
async def get_todos():
    return{"todos":todos}

@app.get("/todo/{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return {"todo":todo}
    return{"message":"No todos Found"}

@app.post('/todos')
async def create_todos(todo: ToDo):
    todos.append(todo)
    return{"message":"Todos has been appended"}

@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            todos.remove(todo)
            return {"message":f"Deleted {todo} todo"}
    return{"message":"No todos Found"}

