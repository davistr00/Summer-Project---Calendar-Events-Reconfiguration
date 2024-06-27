# Author: Toni Davis
# Purpose: This environment is for me to test queries

from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["MainCal_db"]
collection = db["events"]

'''
# Print all entries
cursor = collection.find()
for record in cursor:
    print(record)
'''


def date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            event_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            return event_date
        except ValueError:
            print("Invalid format. Please enter date YYYY-MM-DD HH:MM:SS")


start_time = date_input("Start Date and Time (YYYY-MM-DD HH:MM:SS): ")

end_time = date_input("End Date and Time (YYYY-MM-DD HH:MM:SS): ")
# Equal Start or End Time
Equal_conflict = collection.find({"$or": [
    {"start_time": start_time},
    {"end_time": end_time}]})
for record in Equal_conflict:
    print(record)

# Range of time
range_conflict = collection.find({"$and": [
    {"start_time": {"$lte": end_time}},
    {"end_time": {"$gte": start_time}}
]})
for record in range_conflict:
    print(record)

client.close()
