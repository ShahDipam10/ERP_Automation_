from pymongo import MongoClient
from utilities.mongo_utils import get_latest_user
import webbrowser

# Replace with your actual MongoDB connection string
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.chmukrk.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "global"
COLLECTION_NAME = "users"

def get_verification_url(user):
    base_url = "http://localhost:4000/#/verify-email"
    user_id = str(user["_id"])
    token = user.get("verificationToken")
    return f"{base_url}/{user_id}/{token}"

def main():
    user = get_latest_user()
    if user:
        url = get_verification_url(user)
        print("Verification URL:", url)
        webbrowser.open(url)
    else:
        print("No user found.")

if __name__ == "__main__":
    main()