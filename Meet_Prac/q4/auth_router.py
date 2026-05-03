from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from auth import create_access_token,decode_token,verify_passwd
from bson import ObjectId
from database import users
from schemas import User,Token

router = APIRouter(prefix='/auth',tags=['Auth'])

@router.post('/register')
def register(user: User):
    if users.find_one({'email':user.email}):
        raise Exception('Already exists')
    users.insert_one({'email':user.email, 'password': hash(user.password)})

@router.post('/login',response_model = Token)
def login(data: OAuth2PasswordBearer = Depends()):
    user = users.find_one({'email':data.email})
    if not user or verify_passwd(data.password,user['password']):
        raise Exception('Invalid Credentials')
    
    token = create_access_token(str(user['_id']))
    return {'access_token': token,
        'token_type': 'bearer'}