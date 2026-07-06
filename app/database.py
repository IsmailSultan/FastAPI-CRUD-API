from pymongo import AsyncMongoClient

mongoURI = "mongodb://localhost:27017"
client = AsyncMongoClient(mongoURI)

db = client["Fastapi_DB"]