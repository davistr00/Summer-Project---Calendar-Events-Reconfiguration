
from pymongo import MongoClient
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")


db = client["calendar_db"]
collection = db["events"]

# Print all entries
cursor = collection.find()
for record in cursor:
    print(record)
