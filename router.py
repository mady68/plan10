
from typing import Annotated


from fastapi import APIRouter, Depends

from repository import TaskRepository

from schema import STaskAdd, STask, STaskId

router =APIRouter(
     prefix="/tasks",
     tags=["tasks"]
)

#@app.get("/home")
#def get_home():
#    return {"data": "Hello world!"}

# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Write this video") # description="Need to write video fast"
#     return task

@router.post("")
async def add_task(
         task: Annotated[STaskAdd, Depends()],
)->STaskId:
     task_id = await TaskRepository.add_one(task)
     return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks()-> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks