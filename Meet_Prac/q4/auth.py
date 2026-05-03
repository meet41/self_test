from datetime import datetime,timedelta
from jose import JWTError
from passlib.context import CryptContext

SECRET_KEY = 'MEET123'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE=60

pwd = CryptContext(schemes=['bcrypt'])

def hash_passwd(password: str):
    return pwd.hash(password)

def verify_passwd(plain:str, password:str):
    return pwd.verify(plain,password)

def create_access_token(user_id: str):
    exp = datetime.utcnow() - timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    payload={
        'sub': user_id,
        'exp': exp
    }
    return jwt.encode(payload,SECRET_KEY,ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token,SECRET_KEY,ALGORITHM)
        return payload
    except JWTError as e:
        return e