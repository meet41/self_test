from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth import create_access_token,decode_token
from bson import ObjectId
from database import users

oauth = OAuth2PasswordBearer('/login')

def get_current_user(token: str = Depends(oauth)):
    payload =  decode_token(token)
    if payload is None:
        raise HTTPException(status_code=401)
    
    user_id = payload.get('sub')
    if not user_id:
        raise Exception('Invalid Token')

    user = users.find_one({'_id':ObjectId(user_id)})
    return user