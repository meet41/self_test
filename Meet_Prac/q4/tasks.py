from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from database import tasks
from schemas import TaskCreate, TaskUpdate
from deps import get_current_user

router = APIRouter(prefix='/task',tags=['tasks'])

@router.post("/tasks")
def create_task(task: TaskCreate, user: str = Depends(get_current_user)):
    new_task = {
        "title": task.title,
        "priority": task.priority,
        "status": "pending",
        "owner": user
    }
    result = tasks.insert_one(new_task)
    return {"id": str(result.inserted_id), "message": "Task created"}

@router.get("/tasks")
def get_tasks(priority: str = None, user: str = Depends(get_current_user)):
    query = {"owner": user}
    if priority:
        query["priority"] = priority

    tasks = []
    for task in tasks.find(query):
        task["id"] = str(task["_id"])
        del task["_id"]
        tasks.append(task)

    return tasks

@router.patch("/tasks/{task_id}")
def update_task(task_id: str, update: TaskUpdate, user: str = Depends(get_current_user)):
    task = tasks.find_one({"_id": ObjectId(task_id)})

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task["owner"] != user:
        raise HTTPException(status_code=403, detail="Not authorized")

    tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"status": update.status}}
    )

    return {"message": "Task updated"}