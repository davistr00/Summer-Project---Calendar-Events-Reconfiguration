# Author: Toni Davis
# Purpose: Create the initial database to store calendar event items and set sample event standard

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Checks connection
print(client)


# Create the database
db = client["MainCal_db"]

# Create the collection
events_collection = db["events"]

# Define a sample event
event = {
    # Required Items
    "Serial": "Serial number of event",
    "What": "Description of Event",
    "Type": "Event Type",
    "start_time": "1-1-2000 12:00:00 AM",
    "end_time": "1-1-2000 12:00:00 AM",
    "status": "Event Status",
    "post_date": "1-1-2000 12:00:00 AM",
    "post_by": "User Who Created The Event",
    "repeat": "Y or N",
    "private": "Y or N",

    # Optional
    "attendees": [],
    "alarm": "1-1-2000 12:00:00 AM",
    "attachment": "Path to Attachment",
    "CaseNo": "Case Number of Case Related to Event"
}


