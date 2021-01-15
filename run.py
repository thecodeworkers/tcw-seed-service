from pymongo import MongoClient
import os

client = MongoClient(os.environ["DATABASE_HOST"], int(os.environ["DATABASE_PORT"]))
db = client.test_database
collection = db.test_collection

post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
    }

collection.insert_one(post)

print('success')
