# Author: Toni Davis
# Purpose: Create initial events

from pymongo import MongoClient
import json
# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["MainCal_db"]
collection = db["events"]

#Reading in my event file
filepath = 'Data.txt'
with open(filepath, "r") as file:
    lines = file.readlines()

events = [json.loads(line.strip()) for line in lines]

collection.insert_many(events)
# Print all entries
cursor = collection.find()
for record in cursor:
    print(record)
