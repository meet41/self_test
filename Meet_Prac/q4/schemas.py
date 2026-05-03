from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    email: str
    password: str

class Userlogin(BaseModel):
    email: str
    password: str

class Task(BaseModel):
    title:str
    priority: str

class TaskUpdate(BaseModel):
    title: str
    priority: str

class Token(BaseModel):
    access_token: str
    token_type: str