from pymongo import MongoClient

URI = 'mongodb://localhost:27017'
client = MongoClient(URI)

print(client)