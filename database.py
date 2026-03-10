import pymongo
from pymongo import MongoClient

# 1. Configuration
# REPLACE THE STRING BELOW with your actual Atlas connection string!
# Remember to put your password where it says <db_password>
CONNECTION_STRING = "mongodb+srv://sassyanurag101:hellobro890@anuragdb.ab77s0g.mongodb.net/?appName=anuragDB"

def get_database():
    """Connects to MongoDB and returns the database object."""
    try:
        client = MongoClient(CONNECTION_STRING)
        # This will create the database 'my_project' if it doesn't exist
        return client['my_project']
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None

if __name__ == "__main__":
    db = get_database()
    if db is not None:
        print("Successfully connected to the Cloud!")