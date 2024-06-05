# Author: Toni Davis
# Purpose: Create the inital database to store calendar event items


from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Checks connection
print(client)

# Create the database
db = client["calendar_db"]

# Create the collection
events_collection = db["events"]

# Define a sample event
event = {
    "What": "Description",
    "Type": "Event Type",
    "start_time": "1-1-2000 12:00:00 AM",
    "end_time": "1-1-2000 12:00:00 AM",
    "status": "Event Status",
    "attendees": []
}

# Test Events
ev1 = {'What': "Team Meeting", 'type': "Work", 'start_time': "2024-06-10 09:00:00", 'end_time': "2024-06-10T10:00:00",
       'status': "confirmed", 'attendees': ["JDoe", "JSmith"]}
ev2 = {'What': "Depo", 'type': "Depo", 'start_time': "2024-06-10 09:00:00", 'end_time': "2024-06-10 10:00:00",
       'status': "confirmed", 'attendees': ["tDavis", "BBob", 'KCostner']}

# Insert the event into the collection
event_id = events_collection.insert_one(ev1).inserted_id
print(f"Event inserted with ID: {event_id}")
event_id = events_collection.insert_one(ev2).inserted_id
print(f"Event inserted with ID: {event_id}")

# Retrieve all events
events = events_collection.find()

for record in events:
    print(record)
