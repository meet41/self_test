from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017/"
client = MongoClient(mongo_uri)

db = client["test2"]
users = db["users"]
tasks = db["tasks"]