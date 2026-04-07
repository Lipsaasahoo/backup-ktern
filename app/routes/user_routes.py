from fastapi import APIRouter
from app.schema.user_schema import User
from app.database.connection import user_collection

router = APIRouter()

# ✅ Root route so "/" returns 200
@router.get("/")
def root():
    return {"status": "ok", "message": "Service is up"}


@router.post("/users")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }

@router.get("/users")
def get_users(user: User):
    user_dict = user.dict()
    user_collection.insert_one(user_dict)

    return {
        "message": "Users fetched successfully",
        "data": user.dict()
    }

# ✅ Root route so "/" returns 200
# @router.get("/")
# def root():
#     return {"status": "ok", "message": "Service is up"}

# # GET API - Get all users
# @router.get("/users")
# def get_users():
#     users = list(user_collection.find())
#     return {"users": users, "total": len(users)}

# @router.post("/create-user")
# def create_user(user: User):

#     user_dict = user.dict()

#     user_collection.insert_one(user_dict)

#     return {"message": "User created successfully"}
#     "data": user

