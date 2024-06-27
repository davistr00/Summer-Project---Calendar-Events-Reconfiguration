# Author: Toni Davis
# Purpose: This code allows for a user to enter a new event and check for event conflicts for users

from datetime import datetime
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["MainCal_db"]
collection = db["events"]


# Function for collecting date times
def date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            event_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            return event_date
        except ValueError:
            print("Invalid format. Please enter date YYYY-MM-DD HH:MM:SS")


# Getting Event Details
Serial = input("Serial number of event: ")
What = input("Description of Event: ")
Type = input("Event Type: ")
start_time = date_input("Start Date and Time (YYYY-MM-DD HH:MM:SS): ")
end_time = date_input("End Date and Time (YYYY-MM-DD HH:MM:SS): ")
status = "Scheduled"
post_date = datetime.today()
post_by = input("Your Username: ")
repeat = input("Is this a repeat event (Y or N): ")
private = input("Is this a private event (Y or N): ")

# Optional.
print("The Following fields are optional")
attendees = input("Enter attendees' usernames (comma seperated): ")
attendees = [attendee.strip() for attendee in attendees.split(',')] if attendees else []
alarm = input("Enter date and time of alarm: ")
attachment = input("Path to Attachment: ")
CaseNo = input("Case Number of Case Related to Event: ")
Location = input("Location of Event: ")

# Conflict Check for event times
# Range and users
conflict = collection.find({"$and": [
    {"start_time": {"$lte": end_time}},
    {"end_time": {"$gte": start_time}},
    {"attendees": {"$in": attendees}}
]}, {"_id": False, "What": True, "start_time": True, "end_time": True, "attendees": True})

conflict_count = collection.count_documents({"$and": [
    {"start_time": {"$lte": end_time}},
    {"end_time": {"$gte": start_time}},
    {"attendees": {"$in": attendees}}
]})

if conflict_count > 0:
    print("There is an event conflict please see the information below:")
    for record in conflict:
        print(record)
else:
    event = {
        "Serial": Serial,
        "What": What,
        "Type": Type,
        "start_time": start_time,
        "end_time": end_time,
        "status": status,
        "post_date": post_date,
        "post_by": post_by,
        "repeat": repeat,
        "private": private
    }
    if attendees:
        event["attendees"] = attendees
    if alarm:
        event["alarm"] = alarm
    if attachment:
        event["attachment"] = attachment
    if CaseNo:
        event["CaseNo"] = CaseNo
    if Location:
        event["Location"] = Location
    result = collection.insert_one(event)
    print(f"Inserted document with _id: {result.inserted_id}")

client.close()
