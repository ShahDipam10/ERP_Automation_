from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_URI = "mongodb+srv://riap133077701:YXM8FfPlzesiaUR5@cluster0.chmukrk.mongodb.net/"
DB_NAME = "global"
COLLECTION_NAME = "users"

def get_latest_user():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    users = db[COLLECTION_NAME]
    # Sort by _id descending to get the latest inserted user
    user = users.find_one(sort=[("_id", -1)])
    if user:
        return user
    return None
