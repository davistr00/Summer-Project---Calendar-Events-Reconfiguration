from pymongo import MongoClient
import csv

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["MainCal_db"]
collection = db["events"]

cursor = collection.find({})
for record in cursor:
    print(record)
client.close()