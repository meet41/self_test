from pymongo import MongoClient

mongo_uri = 'mongodb://localhost:27017'
db = MongoClient(mongo_uri)
users = db['users']
tasks = db['tasks']