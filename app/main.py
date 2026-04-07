from fastapi import FastAPI
from app.routes import user_routes
from app.schema.user_schema import User
from app.database.connection import user_collection

app = FastAPI(title="FastAPI Sample")

# # ✅ Root route so "/" returns 200
# @app.get("/")
# def root():
#     return {"status": "ok", "message": "Service is up"}

# # GET API - Get all users
# @app.get("/users")
# def get_users():
#     users = list(user_collection.find())
#     return {"users": users, "total": len(users)}

# @app.post("/createUsers")
# def create_users():
    

# Include your routers
app.include_router(user_routes.router)