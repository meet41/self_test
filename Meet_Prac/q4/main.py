from fastapi import FastAPI
from auth_router import *
from tasks import *
app = FastAPI()

app.include_router(auth_router)
app.include_router(tasks)