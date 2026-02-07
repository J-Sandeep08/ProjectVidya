from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

#Temporary Database(Prototype)
users_db = {
    "admin": {
        "firstname": "Admin",
        "lastname": "User",
        "email": "admin@example.com",
        "password": "admin123"
    }
}
#login page code block
#****
#Request Model
class LoginRequest(BaseModel):
    username: str
    password: str

#Login Endpoint
@router.post("/login")
def login(user: LoginRequest):

    if user.username not in users_db:
        raise HTTPException(status_code=404, detail="user not found")
    if users_db[user.username]!= user.password:
        raise HTTPException(status_code=401, detail ="Invalid credentials")
    
    return {
        "message": "Login successful",
        "username" : user.username
    }
#***

#SignUp page code block
#***
class SignUpRequest(BaseModel):
    firstname: str
    lastname: str
    email: str
    username: str
    password: str
    confirmpassword: str


#Signup Endpoint
@router.post("/signup")
def signup(user: SignUpRequest):

    #check password match
    if user.password!= user.confirmpassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    #check existing user
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    #Store user details
    users_db[user.username] = {
        "firstname": user.firstname,
        "lastname": user.lastname,
        "email": user.email,
        "password": user.password
    }
    return {"message": "Signup successful"}

