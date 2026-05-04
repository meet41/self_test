from fastapi import FastAPI
# from auth_router import auth_router, create_access_token
# from tasks import tasks_router, create_task, get_current_user
import auth_router
import tasks

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(tasks.router)