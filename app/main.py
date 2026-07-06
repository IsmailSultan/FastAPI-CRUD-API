from fastapi import FastAPI
from app.database import db
from app.schemas import User
from bson import ObjectId
from fastapi import HTTPException

app = FastAPI()

# creates user 
@app.post("/users")
async def create_user(user : User):
        result = await db.users.insert_one(
                user.model_dump()
        )
        return {"id": str(result.inserted_id)}

# retreives all users 
@app.get("/users")
async def get_users():
    users = await db.users.find().to_list(length=100)
    for user in users:
           user["_id"] = str(user["_id"])
    return users

# retrieves 1 user 
@app.get("/users/{id}")
async def get_user(id: str):
    try :
        object_id = ObjectId(id)
    except Exception:
          raise HTTPException(status_code=400, detail="Invalid User Id")
    
    user = await db.users.find_one({
            "_id": ObjectId(id)
    })

    if user == None:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    # print(user)
    # print(id)
    user["_id"] = str(user["_id"])
    return user

@app.put("/users/{id}")
async def update_user(id: str, user: User):
    result = await db.users.update_one(
        {"_id": ObjectId(id)},
        {"$set": user.model_dump()}
    )
    # set updates only the fields returned my model_dump

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated successfully"}

@app.delete("/users/{id}")
async def delete_user(id: str):
    result = await db.users.delete_one(
        {"_id": ObjectId(id)}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"message": "User deleted successfully"}